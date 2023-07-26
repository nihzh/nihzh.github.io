## Situations
- 在Linux的Docker中安装
- 跟随[安装 (fofapro.github.io)](https://fofapro.github.io/vulfocus/#/INSTALL)
- 使用docker pull直接拉取镜像
- 安装完成后, 在"镜像管理"模块下, 点击"一件同步按钮", 无法同步靶场镜像

## Reasons&Solution
### Method 1
1. 镜像中/vulfocus-api/dockerapi/view.py, 1576行, 网址修改为`https://vulfocus.cn/api/imgs/info`

### Method 2
1. `daemon.json`文件中添加一行`"https://dockerproxy.com/"`
2. 拉取`dockerproxy.com/vulfocus/vulfocus:latest`
3. 创建容器，启动

## References
1. [用docker搭建的Vulfocus镜像管理界面没有镜像可以拉取解决办法](https://edu.hetianlab.com/post/251)
2. SELECT dalao FROM yijinglab WHERE id='微凉'