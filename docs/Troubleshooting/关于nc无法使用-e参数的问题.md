## Situation
- Ubuntu22系统, Kali21系统
- nc: *netcat*, Linux自带网络连接工具
- 执行`nc -h`显示帮助文件, 参数列表中没有-e选项, 实际使用`nc -e`提示选项无效

## Reason
- Linux自带的nc版本过老, 还不支持-e参数

## Fixing solution
1. 安装新版本的nc `sudo apt -y install netcat-traditional`
2. 配置默认 `sudo update-alternatives --config nc`, 选择`/bin/nc.traditional`

## Reference
1. [关于nc无法使用-e参数 nc：invalid option -- ‘e’_nc -e 获取输入参数_tonine9的博客-CSDN博客](https://blog.csdn.net/tonine9/article/details/125957207)