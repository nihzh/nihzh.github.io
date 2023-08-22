## Situation
- 使用WindTerm2.6.0, 每静置过一段时间, 会自动锁屏并要求用户输入密码, 在未设置密码时依旧如此, 所以在不知道密码的情况下, 只能关闭软件重新打开

## Solution
### 关闭锁屏
- 在用户目录`.wind/profiles/default.v10/user.config`文件中添加`"application.masterPassword" : false`
	- **新版测试后无效**
- 在安装目录`global/wind.config`文件, 修改`"application.lockScreenTimeout" : 30`后面的值为0或负数, 关闭延时

### 重置锁屏密码
- 用户目录`.wind/profiles/default.v10/terminal/user.session`文件, 将其中所有`autologin`字段全部删除, 重启WindTerm
	- 重启过后默认密码为**空**

## References
1. https://blog.csdn.net/DongShanAAA/article/details/126682154
2. https://blog.csdn.net/cddchina/article/details/130861994