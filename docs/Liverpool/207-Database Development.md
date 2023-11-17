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
- The "transaction" in MySQL below are under the InnoDB engine; MyISAM did not support transactions
- A basic transaction, start with command `BEGIN` or `START TRANSACTION`; end with `COMMIT` or `ROLLBACK`.
```mysql
[START TRANSACTION | BEGIN];
<SQL-STATEMENTS>
ROLLBACK;
COMMIT;
```
- The taransaction starts since the first line execute, rather than "begin"
- To check the count of transactions opertating
```mysql
SELECT * FROM information_schema.innodb_trx;
```

These two SQL Statements will produces three transaction operationsm, to three simplified transaction operations
```sql
SELECT salary FROM Employees WHERE e_id = 1234;
UPDATE Employees SET salary = salary * 1.1 WHERE e_id = 1234;

-- abstraction at a lower level
read(e_id=1234, salary);
salary = salary * 1.1;
write(e_id = 1234, salary);

-- X in this case is "e_id 1234's salary"
read(X);
X = X * 1.1;
write(X);
```

- Basic operations: consentrate at lower-level details (reads and writes) and their interaction over high-level (queries)
	- `read(X)`: reads a database item X into a program variable
	- `write(X)`: writes the value of program variable X into the database item named X
	- `output(X)`: copy database item X from buffer to database
	- `flush_log`: wuite log intries that are currently residing in main memory (buffer) to log
- logical unit of procdessing using access operations
	- Begin
	- End
	- read(select)
	- write(insert, update, delete)
	- other non-database operations


#### ACID: 
- *Atomicity*: either do the full transaction or nothing, A transaction is an indivisible unit of prosessing, deals with failure aborts, we should **undo** the previous work
- *Consistency*: may not violate constrains, It should correctly transform the database state to reflect of a real-world event
	- serial schedules are consistent
- *Isolation*: the transactions should operate as if no other transactions are running at the same time
	- A schedule satisfies isolation if it is serializable
- *Durability*: after commit has been done, things that happen later should not undo that

#### Isolation levels
Default transaction isolation level for InnoDB is *REPEATABLE READ*
- Read phenomena: 
	- *Dirty read*: A transaction reads the uncommitted data from other transaction, which meas the data may not be stored to the database finally.
	- *Unrepeatable read*: In same transaction, same data reads in different time are inconsistant (structure). Normally deal with *UPDATE*
	- *Phantom read*: A transaction reads the unconsistant data which committed by another transaction. Normally deal with *INSERT*

Read and alter transaction isolation level
```mysql
-- after version 5.7.20
show variables like 'transaction_isolation';
SELECT @@transaction_isolation;

-- before 5.7.20
show variables like 'tx_isolation';
SELECT @@tx_isolation;

-- set
SET <scope> TRANSACTION ISOLATION LEVEL <level-name>
```
The corresponding isolation strategy only activate on the new session which establish after setting the isolation level.
- scope:
	- `SESSION`: only for current session window
	- `GLOBAL`: for all sessions
- Transaction isolation levels: 
	- *READ UNCOMMITTED*: All the operation done (not commited) are exposed to other transactions immediately. **Will lead to all three** phenomena
	- *READ COMMITTED*: The transaction can only reads data that already committed by other transaction. Can **cover the problem of Dirty read**. Is default isolation level of *Oracle*.
	- *REPEATABLE READ*: The data updated by other transaction after current transaction established is not accessable, the reading data is consistancy throughout the transaction, but new records inserted by others during current transaction cannot be coverd (**cannot cover phantom read**). (MySQL is fixed phantom read problem in repeatable read level)
	- *SEARIALIZABLE*: A new transaction can only be execute when the previous transaction commit. **Solves all three** phenomena.

### Schedules
- Hold many transactions for execution, in the right order
- Two types
	- *Serial Schedules*: executes the transactions one after another, can maintain correctly and consistency of the database
	- *Concurrent Schedules*: can interleave operations from many transactions, not guarantee consistency or isolation of the database (still preserving the right order, serial also concurrent). More efficiency
- `Sid`: schedule (id is the schedule ID)
- `ri(X)`: read(X) in transaction i
- `wi(X)`: write(X) in transaction i
- `ci`: commit in transaction i
- `ai`: abort ("rollback") in transaction i

#### Serializable Schedules
- A schedule S is *serializable* if there is a serical schedule S' that has the same effect as S on every initial database state.
- Guarantee the correctness and consistency, but not satisfy isolation.
- Serializability is difficult to test, not only depend on reads, writes and commits, also on the non-database operations, which canbe complex

#### Conflict serializable schedules
- Stronger form of serializability based on the notion of a conflict
- A conflict in a schedule is a pair of operations from different transactions that cannot be swapped without changing the behaviour of at least one of the transactions.
- A conflict:
	- from different transactions
	- access the same item
	- at least one of them is a write operation
- Conflicts: 
	- *write-write conflict*: may lead to dirty write
	- *write-read conflict*: may lead to dirty read
	- *read-write conflict*: may lead to unrepeatable read
- *Conflict-serializable*: If S' can be optained from S by swapping any number of consecutive non-conflict operations
	- "access different item" / "read" (non-conflicting)
	- from different transactions
- A schedule is *conflict-serializable* if it is conflict-equivalent to a serial schedule.
- *Precedence graph*: directed graph, nodes are the transactions in S
	- edge: a conflicting pair op1(Ti) --> op2(Tj), only the operation from tarnsaction 1 being the first occourring one in the schedule
	- If the graph is no cycle, the S is conflict-serializable, otherwise not.
	- All conflict-equivalent schedulers: operation in T1 is before operation in T2


# 10/17/2023
- `SET tx_isolationn = ‘Serializable’`

# 10/19/2023
### Locks
#### Two-phase Locking (2PL)
- A simple locking mechanism that guarantees conflick-serializability
- In each **transaction**, all lock operations precede all unlocks
	- Phase 1: request locks + possibly other read/write operations
	- Phase 2: unlock + posibly other read/write operations
- If S is a chedule containing only 2PL transactions, then S is conflict-serializable
- Might lead to *Deadlock*, transactions be forces to wait forever
	- Two transactions request for lock a item simultaneously which locked by counterpart, are all waiting for releasement (unlock)

#### Shared & Exclusive locks
- *Shared lock* (read lock)
	- requested by transactions to read an item X `s-lock(X)/sli(X)`
	- granted **to several transactions at the same time**
	- granted only no **other transactions** holds **a exclusive** lock on X
- *Exclusive lock* (write lock)
	- requested by transactions to wirte an item X `x-lock(X)/xli(X)`
	- granted to **at most one transaction** at a time
	- granted only no **other transactions** holds **a lock** on X
- A individual transaction may hold both a shared lock and an exclusive lock for the same item X. Can be upgrade from a shared lock to an exclusive lock, it is rick to deadlock.
- *Update lock*: 
	- requested by transactions to read (not write) an item
	- **can be upgraded** later to an exclusive lock (shared lock cant upgrade)
	- granted to **at most one transaction** at a time
- Granularity
	- relations
	- disk blocks
	- tuples
- *Intension locks*: If a transaction wants to lock a item X, must first put an intention lock on the super-items of X
	- *IS*: intension to request a shared lock on a sub-item
	- *IX*: intension to request a exclusive lock on a sub-item

### Relational DBMS Components
1. User/application
2. Transaction manager
3. Logging and recovery / concurrency control
4. Buffers
5. Storage
- Transaction abort: 
	- violation of integrity constrains, other run-time errors
	- deadlocks: concurrency control requests
	- explict request, `ROLLBACK`

### Loggings
#### Undo logging (Atomicity)
- Log records:
- `<START T>` Transaction T has started.
- `<COMMIT T>` Transaction T has committed, must be written to disk as soon as all database elements changed.
- `<ABOUT T>` Transaction T was aborted
- `<T,X,v>` Transaction T has updated the value of database item X, and **the old value was v**. 
	- **Must be written to the log on disk before X is written to disk**
	- direct response to `write(X)`
- undo procedure: traverse the undo log from the last to the first item

#### Redo logging (Durability)
- `<T,X,v>`: Transaction T has updated the value of database item X and **the new value is v**
- haven't changed X on disk yet.
- procedure (Transaction T): 
	1. Identify all the transactions with a COMMIT log record
	2. Traberse the log from first to the last item: If see `<T,X,v>` and T has a COMMIT log record then change the value of X on disk to v
	3. For each incomplete transaction T, write \<ABORT T\> into the log on disk

#### Undo/Redo logging (DBMS using)
- `<T,X,v,w>`: Transaction T has updated teh vcalue of database item X, adn **the old/new value of X is v/w**
- Write all log records for all updates to databse items first
- Ensure Atomicity and Durability without log using No Steal/Force;

### Checkpoints
- ARIES:
	- Undo/Redo logging
	- Transactions do not write to buffers before they are sure they want to commit
	- Write `<CHECKPOINT(T1, T2)>` at first; write `<END CHECKPOINT>` after moved the content of the buffer to the disk.
- recovery:
	- find a `<CHECKPOINT(T1,T2)>` with corresponding `<END CHECKPOINT>` and `<START Ti>` for *all mentioned transactions* that are **uncommitted**.
	- only redo part of **committed** transactions in mentioned transaction after `<CHECKPOINT(T1,T2)>`; then undo all of uncommitted transactions in mentioned transaction before `<CHECKPOINT(T1,T2)>`
- Robust: works even after system failures

### Recoverable schedules
- *Cascading Rollback*: If a transaction T aborts: Recursively abort all transactions that have read items written by an aborted transaction.
	- abort: break isolation
	- not abort: break durability
- A schedule S is recoverable if the following is true:
	- if a transaction T1 commits and has read an item X that was written before by a different transaction T2
	- then T2 must commit before T1 commits
- Additional implicit requirement
	- All log records have to reach disk in the order in which they are written
	- could in principle abort -> cascading rollback
- *Recoverable schedules*: T **commits** only if all transactions that T has read from have commited

### Cascadeless schedules
- Each transaction in it **reads** only values that were written by transactions that have already committed
	- no dirty data
	- no cascading rollback
	- Log records have to reach disk in the right order
- Cascadeless schedules are *recoverable*
- Cascadeless schedules are in general **not serialisable**

### Strict schedules
- Each transaction in it **reads and writes** only values that were written by transactons that have already committed
- *Strict Two-Phase Locking* (Strict 2PL)
	- Enforces *conflict-serialisability* and *strict schedules*
	- A transaction T **must not release any lock** (allows T to write data, e.g. *exclusive locks*) until: **T has committed or aborted** AND the commit/abort log recored has been written to disk
- Strict 2PL and deadlocks: two transactions hold the lock that each others requesting, waiting peer for release the lock.

### Timestamp based schedules
- Schedule transactions so that the effect is the same as executing wach transaction instantaneously when it is started
- The scheduler processing request (`read(X)`, `write(X)`) from transactions in the transaction manager queue, the scheduler can only:
	- Grant request
	- Abort transaction
	- Delay transaction
- *Timestamps*: Each transaction T is assigned a unique integer `TS(T)` when it starts (The timestamp of T)
- T1 started earlier than T2, then TS(T1) < TS(T2)
- Assign a **new timestamp** after a restart
- For each database item X
	- Read Time of X: `RT(X)`: timestamp of **youngest transaction** that read X
	- Write Time of X: `WT(X)`: timestamp of **youngetst transaction** that wrote X
- If T1 requests to **read X**: Abort & restart T1 if **WT(X) > TS(T1)**, grand request otherwise
- If T1 requests to **write X**: Abort & restart T1 if **RT(X) > TS(T1)** OR **WT(X) > TS(T1)**, grand request otherwise
- Schedules enforced by timestamp based schedulers are not strict, additional condition: **Delay read or write** reqeusts until the youngest transaction who **wrote** X before has committed or aborted
- *Multiversion concurrency control* (MVCC): 
	- write operations do not overwrite each other, but instead Wi(X) creates makes a new version X at time TS(Ti)
	- The transaction always reads the latest version before its timestamp
	- which means that a transaction only need to restart if it tries to **write** AND the **read timestamp** is later than its timestamp
	- Only **abort & restart T1** if **RT(X) > TS(T1)** when writes; reads are always granted
		- may let later transaction phantom reads