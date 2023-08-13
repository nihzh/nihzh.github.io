默认使用的shell是每个用户用户账号的一个参数, 一般为`/bin/bash`

### /bin/sh
在不同的系统中, 默认交互命令行和`/bin/sh`可能是不同的东西
#### The Bourne Shell (sh)
- UNIX最初的shell, 由AT&T Bell Labs的Steve Bourne制作, 因高速和紧凑性出名.
- 是Solaris OS的默认shell, 也是其系统管理员 (system administration)的shell (Solaris 10)
- 缺点: 
	- 没有内置逻辑和算术运算的功能
	- 无法恢复之前执行的命令
	- 无法提供全面的交互式功能

#### A POSIX-certified shell
存在于更新的UNIX中, 如Solaris 11 (2010)

#### Almquist Shell (ash)
- 开源的*Bourne/POSIX shell* 克隆版本, 1989发布于Usenet, 然后被贡献给Berkeley的CSRG, 以包含在**第一个不包含AT&T源代码的BSD版本***4.4BSD-Lite*中
- *BSD-lite*作为现在BSD衍生产品的基础, 其中的/bin/sh仍是大多数ash的衍生产品
- 有两个重要的分支
	- *dash*, 2006年之后被Debian和Ubuntu作为默认/bin/sh
	- *BusyBox*中的ash命令, 常用于嵌入式linux, 是dash的后继版本, 派生自Debian的旧dash包 (dash衍生版). 还包括一种功能较弱的替代品*hush*, 在空间非常紧张的情况下.

#### GNU Bash
- 作为sh时, 禁用大多数非POSIX扩展
- 在Linux桌面和服务器(除了Debian及其衍生版)变体上很常见 (Mac OS X)

#### A shell with ksh93 POSIX extensions (ksh93扩展的POSIX)
- OpenBSD 的shell会改变行为以避免和*Bourne*和*POSIX shell*的语法和语义不兼容, 但不会禁用任何不与旧shell冲突的扩展
- *ksh93*的功能并不完全


### The GNU Bourne-Again Shell (bash)
- 与sh完全兼容
- 融合了ksh和csh中一些有用的功能
- 40个内置命令
- 可以自动恢复之前的命令, 使用方向键选择并编辑
- 支持tab补全
- 完整路径名称是`/bin/bash`
- 默认情况下, 对root用户的提示符是`bash-版本号#`, 非root用户是`bash-版本号$`

### C Shell (csh)
- 加利福尼亚大学.Bill Joy
- 包含了编程功能如算数操作, 语法与C语言相似
- 有命令历史记录
- "别名"功能
- 完整路径名称`/bin/csh`
- 默认情况下, 对root用户的提示符是`主机名#`, 非root用户是`主机名%`
#### tcsh
csh的一个增强版本, 与csh完全兼容

### Korn Shell (ksh)
- David Korn @ AT&T Bell Labs
- 为了提升sh, 是sh的超集
- 在sh基础上, 对算数运算的支持和类似csh的交互
- 可以执行sh的所有脚本, 提供类似C语言的字符串,数组和函数操作, 同时也支持csh的脚本
- 比csh在内的大多数其它Linux Shell的运行速度快
- 完整路径名称`/bin/ksh`
- 默认情况下, 对root用户的提示符是`#`, 非root用户是`$`

### The Z Shell (zsh)
- sh的扩展, 含有大量客制化的提升, 更现代化, 更多功能
- 亮点功能
	- 根据条件生成文件名
	- 插件和主题
	- 索引内置函数
	- 自动补全命令
	- ......
	- 

### 功能区分
| Shell  | Complete path-name | Prompt for root user | Prompt for non root user |
| ------ | ------------------ | -------------------- | ------------------------ |
|Bourne Shell (sh)| /bin/sh and /sbin/sh|#|$|
|GNU Bourne-Again shell (bash)| /bin/bash|bash-VersionNumber#|bash-VersionNumber$|
|C Shell (csh)|/bin/csh|#|%|
|Korn Shell (ksh)|/bin/ksh|#|$|
|Z Shell (zsh)|/bin/zsh|\<hostname\>#|\<hostname\>%|


## References
1. [What are the Different Types of Shells in Linux? | DigitalOcean](https://www.digitalocean.com/community/tutorials/different-types-of-shells-in-linux)
2. [shell - What does it mean to be "sh compatible"? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/145522/what-does-it-mean-to-be-sh-compatible)