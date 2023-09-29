# 09/26/2023
- The world's most valuable resource os no longer oil, but data.
- Relational DBMS are one of the biggest success stories in computer science, also one of the most comples pieces of software.
![[Pasted image 20230926162722.png]]

#### Table, column and row
- Data is organised in *Tables*
	- *Attributes/columns*
	- *Tuple/row*
		- *Element*: the data
- Each table has a **schema**, the schema of a table is the structure of the table itself.
- A typical table has:
	- Few fixed *columns/attributes*, indicates the column name, type and length (**cannot change**)
	- The number of *rows* depends on the table and **can change**. 
- Typical rows:
	- Each row corresponds to **an entity or similar**, or to a **relationship** between such
	- Rows in **same table represents same entity** or relation
	- The consistancy rules in database is opposite to the identical principle in object-oriented proramming: "If two rows are same, they corresponding the same item"

#### SQL
Rational databases are accessed using *SQL* (Standard Query Language), it's **a standard** and is updated every few years, but usually not be followed by implementations.
- Data Definition Language, *DDL*
	- **Create/alter/delete** databases, towards **tables and their atteributes**
- Data Manipulation Language, *DML*
	- **Add/remove/update/query** **rows** in tables
- Transact-SQL
	- Intuitively, do a **sequence** of SQL statements
- Modify table: 
	- change the datatype of a column`ALTER TABLE <table_name> MODIFY <attribute_name> <datatype>` (MySQL and Oracle only)
	- removes a column `ALTER TABLE <table_name> DROP COLUMN <attribute_name>`