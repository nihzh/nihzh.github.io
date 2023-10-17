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


# 10/03/2023
- UPDATE R SET a=a+1 WHERE a=3;
![[Pasted image 20231004232729.png]]
- `on`: defining the corresponding column of "join", `on a.id = b.id`
- `using`: better and easier to use than "on", connecting the attributes which have same name, `using(<column-name>)`

# 10/05/2023
- *Projection(Π)*: to extract values by given column name
- `DISTINCT`: removing duplicated rows
- *Renaming(ρ)*: writing `AS` and type new name after the attribute
- Creating new columns: `a + b AS total`
	- `COUNT()`, `AVG()`, `MIN()`, `MAX()`, `SUM()`
- *Cross product(Х)*: from two or more different tabel directly, multiple result
- *Natural join(⋈)*: To match values in the column with same name (overlap). Same effect with Х and where constrain. Only displays the matching values.
- *Selection(σ)*：Set of all tuples in R that jatisfy the condition
- Never use same column name of different subject in different table
- `WHERE`: used in `select`, `update`, `delete`
	- `IN`: whether the element exests in a list/sub-query
	- `EXISTS`: current row will be kept if returns something in the sub-query (use the constand 1 as the return value in sub-query commonly)
	- *Left/right semi-join(⋉/⋊)*: `IN` and `EXISTS` are exactly semi-join, can just be a single query and must not include UNION, GROUP BY, HAVING
		- The joining table just involve the containing judge but not attend the result of SELECT, which named semi-join
		- (left) `SELECT Employees E WHERE EXISTS (SELECT 1 FROM Transactions T WHERE E.e_id = T.e_id);`
- `GROUP BY`: To collect same value in same column as one value, the rest that not be mentioned by GROUP BY clause will be partly disposed. Usually cooperate with functions such as `COUNT()` to get the number of rows (calculating result) with same value on a given attribute.
- `HAVING`: WHERE, done after GROUP BY, could use functions in it.
- `ORDER BY`: defines how the output is sorted, could not actually in the output. 
	- `ASC`: ascending, default
	- `DESC`: descending
- `UNION`: To combine two SELECT statement as one result. Two query statement must have similar datatypes and same number of columns. It will displays 1 record if there are several records that totally same.
	- ORDER BY can be used 1 time at the end of a group of UNION query to sort the output in whole query
```sql
-- To displays the corresponding relationship expandly in single table
SELECT first_name AS name, e_id
FROM Employees
UNION
SELECT family_name, e_id
FROM Employees
```
- `UNION ALL`: Same effect with UNION, will displays all records including duplicated.
- The order of execution
	1. FROM
	2. WHERE
	3. GROUP BY
	4. HAVING
	5. ORDER BY
	6. SELECT
- `View`

```sql
CREATE[OR REPLACE ]VIEW Employee_transaction_count AS
SELECT first_name, e_id, COUNT(t_id)
FROM Employees NATURAL JOIN Transactions
GROUP BY first_name, e_id;

DROP VIEW Employee_transaction_count;
```

# 10/12/2023
### Transactions
- Transaction: a serious of queries, single and complete
	- Concurrency: serialisable behaviour
	- Partial execution
- Two SQL Statements will produces three transaction operationsm, to three simplified transaction operations

```sql
SELECT salary FROM Employees WHERE e_id = 1234;
UPDATE Employees SET salary = salary * 1.1 WHERE e_id = 1234;

TO

-- abstraction at a low level
read(e_id=1234, salary);
salary = salary * 1.1;
write(e_id = 1234, salary);

TO

-- X in this case is "e_id 1234's salary"
read(X);
X = X * 1.1;
write(X);
```
- Basic operations: consentrate at lower-level details (reads and writes) and their interaction over high-level (queries)
	- read(X): reads a database item X into a program variable
	- write(X): writes the value of program variable X into the database item named X
- logical unit of procdessing using access operations
	- Begin
	- End
	- read(select)
	- write(insert, update, delete)
	- other non-database operations

- ACID: 
	- *Atomicity*: either do the full transaction or nothing
	- *Consistency*: definitions range form must satisfy constrains to must match a real-world event
	- *Isolation*: the transactions should operate as if no other transactions are running at the same time
	- *Durability*: after commit has been done, things that happen later should not undo that..
- SEARIALIZABLE
- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READS
```sql
START TRANSACTION
INSERT INTO R VALUES (3);
SELECT * FROM R;
ROLLBACK;
COMMIT;

SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
```

### Schedules
- hold many transactions for execution, in the right order
- two types
	- Serial Schedules: executes the transactions one after anothery
	- Concurrent Schedules: can interleave operations from the trans actions (still preserving the right order, serial also concurrent)
- `Sid`: schedule (id is the schedule ID)
- `ri(X)`: read(X) in transaction i
- `wi(X)`: write(X) in transaction i
- `ci`: commit in transaction i
- `ai`: abort ("rollback") in transaction i
