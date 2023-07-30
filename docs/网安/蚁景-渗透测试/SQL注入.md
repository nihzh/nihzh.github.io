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