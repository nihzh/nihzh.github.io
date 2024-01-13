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
## Transaction Management
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
	- *REPEATABLE READ*: The data updated by other transaction after current transaction established is not accessable (gap lock), the reading data is consistancy throughout the transaction, but **new records inserted** by others during current transaction cannot be coverd (**cannot cover phantom read**). (MySQL is fixed phantom read problem in repeatable read level)
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
- `SET tx_isolationn = 'Serializable'`

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

##### Checkpoints
- ARIES:
	- Undo/Redo logging
	- Transactions do not write to buffers before they are sure they want to commit
	- Write `<CHECKPOINT(T1, T2)>` at first; write `<END CHECKPOINT>` after moved the content of the buffer to the disk.
- recovery:
	- find a `<CHECKPOINT(T1,T2)>` with corresponding `<END CHECKPOINT>` and `<START Ti>` for *all mentioned transactions* that are **uncommitted**.
	- only redo part of **committed** transactions in mentioned transaction after `<CHECKPOINT(T1,T2)>`; then undo all of **uncommitted** transactions in mentioned transaction before `<CHECKPOINT(T1,T2)>`
- Robust: works even after system failures

### Concurrency control
#### Recoverable schedules
- *Cascading Rollback*: If a transaction T aborts: Recursively abort all transactions that have read items written by an aborted transaction.
	- abort: break isolation
	- not abort: break durability
- A schedule S is *recoverable* if the following is true:
	- if a transaction T1 commits and has read an item X that was written before by a different transaction T2
	- then T2 must commit before T1 commits
- Additional implicit requirement
	- All log records have to reach disk in the order in which they are written
	- could in principle abort -> cascading rollback
- *Recoverable schedules*: T **commits** only if all transactions that T has read from have commited

#### Cascadeless schedules
- Each transaction in it **reads** only values that were written by transactions that have already committed
	- no dirty data
	- no cascading rollback
	- Log records have to reach disk in the right order
- Cascadeless schedules are *recoverable*
- Cascadeless schedules are in general **not serialisable**

#### Strict schedules
- Each transaction in it **reads and writes** only values that were written by transactons that have already committed
- *Strict Two-Phase Locking* (Strict 2PL)
	- Enforces *conflict-serialisability* and *strict schedules*
	- A transaction T **must not release any lock** (allows T to write data, e.g. *exclusive locks*) until: **T has committed or aborted** AND the commit/abort log recored has been written to disk
- Strict 2PL and deadlocks: two transactions hold the lock that each others requesting, waiting peer for release the lock.

#### Wound-Wait Scheme
- Use timestamp to decide which transaction can wait further and which must abort to prevent deadlock.
- older transactions **never** wait for unlocks, only younger transactions allowed to wait, so no cyclic dependencies created.
- For two transactions T1 and T2, T1 is current transaction
- If T1 is older than T2
	- T2 is rolled back unless it has finished
- If T1 is younger than T2
	- T1 is allowed to wait further for T2 to unlock

#### Timestamp based schedules
- Schedule transactions so that the effect is the same as executing wach transaction instantaneously when it is started.
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

#### MySQL/InnoDB
- Partly ACID compliant (fully requires additional engines like InnoDB)
- strict 2PL at serialisable isolation level
- MVCC on lower isolatoin levels


## Query Processing
- Query compiler --> Execution Engine
- Responsible for
	- transforming SQL quries into sequences of databse operations
	- executing these operations

1. SQL query
2. Parse query & preprocess
	- Logical query plan (relational algebra)
3. Optimise logical qurey plan
	- Optimised logical query plan
4. Select physical query plan
	- Physical query plan
5. Query Execution

### Relational Algebra
Set of **operations** that can be applied to **relations** to **compute new relations**
- *Selection* (𝜎)
- *Projection* (𝜋)
- *Cartesian product* (×)
- *Union* (∪)
- *Renaming* (𝜌)
- *Natural join* (⋈)
- *Semijoin* (⋉)

### Query Plans
- A **relational algebra expression** that is obtained from an SQL query is called a *logical query plan*
- Query plans are typically represented as trees, **evaluate from the leaves to the root**
	- Leaves: input relations
	- Inner nodes: operations
- DBMSs aim to select a beset possible query plan from many different query plans
	- `𝜎condition(R1 ⋈ R2)` = `𝜎condition(R1) ⋈ 𝜎condition(R2)`

#### Executing Query Plans
Proceed a *query plan* from bottom to top
- Compute an intermediate result for each node
- For a **leaf**  relation R, the intermediate result is R
- For an **inner node** operator **op**, get the intermediate result by applying op to the childrens' intermediate results
- Result of the query = intermediate result of the **root**

SELECT AND WHERE
```
𝜎 condition(R) have to read entire file
for each tuple t in R:
	if t satisfies condition:
		output t

𝜋 attribute list(R)
for each tuple t in R:
	output the restriction of t to the attribute in attribute list
```

### Joins
*Natural join* ⋈ for R ⋈ S: Nested loop join algorithm, for each tuple r in R reads entire relation S. Running time: `O(|R| * |S|)`
```
for each tuple r in R:
	for each tuple s in S:
		if r and s have the same values for all common sttributes
			output r ⋈ s
```

*Equijoins*:  On `R ⋈A=B S is defined as 𝜎A=B(R × S)`, If R is sorted on A and S is sorted on B, then R ⋈A=B S can ge computed with one pass over R and S + runtime equal to the size of the output
- For duplicates value in target column, uses `×` to join all records
- Typical running time: `𝑂(|R|log2|R| + |S|log2|S|)`

Join algorithms in practice
- Index joins
- Hash joins
- Multipay joins: join more than two relations at once

### Index
Given the values for one or more attributes of a relation R, provides quick access to the tuples with these values
- Secondary: points to locatoin of records on disk
- Primary: in addition, defines how data is sorted on disk
- Forms on indexes
	- *B+ Trees*: Good for selection dondition specifies a range
	- *Hash tables*: Good for selection involves equality only

### B+ Trees
Multi-level index: distributed across different layers
- *Leaves*:  a1... an, Fields are filled from left to right
	- Line 1: sorted in increasing order `a1... ai` + unused
	- Line 2: Points to tuples with value `a1... ai` + unused pointer + next leaf (pointer)
	- n: at least `(n+1)/2` pointers are used, unless this is the only leaf
- *Inner Nodes*: a1... an
	- Line 1: a1... ai number which is **smallest number in childs-subtree** on the **right** + unused
	- Line 2: a1... ai+1, points to node for values between two (one) numbers on top-left and top-right. for first point, values < a1; last point, values >= ai + null point
	- n: at least `(n+1)/2` pointers are used, unless root, which must use >= 2 pointers

#### Looking Up a Value
Find pointer to the rows with value v
1. Start at the root
2. While current node is not leaf node
	1. Find the largest i with ai <= v and proceed to the associated child node
3. If current node is a leaf
	1. if v occours in the leaf, follow the associated pointer
	2. otherwise, return "v does not exist in index"
- `O(h × log2 n)`, h: height of the B+ tree

#### Inserts value/pointer pairs
1. Find the leaf that should contain the value
2. If the leaf is not full, insert the value/pointer pair
3. If the leaf is full
	1. Split the peaf to make space for the new value/pointer pair and move **half of the pointers** to the new node
	2. Insert the value/pointer pair
	3. Connect the leaf to parent node, split still needed if the parent node is full
- B+ Tree must remains balanced
- `O(h × log2 n)`

#### Value Deletion
1. Find the value
2. Remove the value
3. Let `x` be  
	| 2	    𝑖𝑓 𝐶 𝑖𝑠 𝑟𝑜𝑜𝑡  
	| 𝑛+1/2  𝑖𝑓 𝐶 𝑖𝑠 𝑖𝑛𝑡𝑒𝑟𝑛𝑎𝑙 𝑛𝑜𝑑𝑒  
	| 𝑛+1/2  𝑖𝑓 𝑐 𝑖𝑠 𝑙𝑒𝑎𝑓
4. Let `C` be current node
5. If `C` has above x pointers: fix ancestors and done
6. If `C` is the root: remove it and let its child be the new root
7. If `C` empty after deletion: 
	1. If *adjacent node* has more than `x + 1`
		1. steal a pointer to the empty leaf
		2. fix ancestors and done
	2. If *adjacent node* has no more than `x + 1`
		1. pick an adjacent node and merge together
		2. `C` == parent node
- B+ Tree must remains balanced
- `O(h × log2 n)`

##### Adjacent node
- *Non-leaf nodes*: the immediate preceding and succeeding siblings at the **same parent node level**.
- *Leaf nodes*: the immediate preceding and succeeding **leaf nodes** at the same level


### Optimise logical qurey plan
- Bottom-up
- Efficiency depends on size of intermediate results
- Equivalence laws of relational algebra, examples:
	- 𝜎A=a AND B=b(R) = 𝜎A=a(𝜎B=b(R))
	- 𝜎A=a(R × S) = 𝜎A=a(R) × S
	- 𝜎A=B(R × S) = R ⋈A=B S

1. Push **selections** as far down the tree as possible
2. "Push" **projections** as for down the tree as possible, or insert projections where appropriate
3. If possible, introduce equijoins (`⋈`) for `𝜎` followed by `×`

### Physical query plan
- Algorithm: index, join
- Pass information: disk/memory, piplining operators
- Order for computing joins, unions, etc.
- Additional operations: sorting, etc.

1. Generate many different phpysical query plans
2. Estimate cost of execution for each plan
	- time
	- Disk accesses: selection algorithm, passing method, size of intermediate results; Size of relations, distinct items per attribute per relation; statistics gathering
	- Memory
	- communication
3. Select physical phan with lowest cost estimate
	- Estimate for the size of `𝜎A=a(R)`: `|R| / number of distinct values in column A of relation R`
	- Estimate for the # of blocks required to store `𝜎A=a(R)`: `|R| / nbumber of distinct values in column A of relation R`
	- Estimate `R ⋈ S` (assume A is the only common attribute): `|R| × |S| / max.number of distinct values for A in R or S`
- Generate physical query plans: top-down/bottom-up
- Algorithm for each operator / join order: based on size of intermediate result
- *Pipelining "stream-based processing"*
	- passes the tuples of one operation directly to the next operation without using disk
	- Extra buffer for each pair of adjacent operations to hold tuples passing from one relation to the other

## Distributed databases
- Collection of multiple logically interrelated databses
- Distributed over a computer network
- *Distributed DBMS (DDBMS)*: manages a distributed database
- *Node/site*: a database computer in the network

### Fragmentation
- split database into divfferent parts that can then be stored at different nodes
	- Horizontal (sharding): may overlap, each site stores a relation that contains a subsut of the tuples, **Entire relation = union of relations at the different sites**
	- Vertical: typically should overlap, tuples stored at different sites can be distinguished by the value of one or few attributes, or other conditions
- *Fragmentation transparency*: Users dont see fragmetns, just the full relations
- *Redundancy*: When a site failed, other site stores the copy are allow to answer queries without establishing a connection to the central office
- *Replication*: Wide spectrum of partial replication: limit number of copies of each fragment, replicate only some fragments
- *Transparency*: 
	- *Fragmentation transparency*: 
		- transparent to users, queries for entire database
		- DDBMS translates this into a query plan that fetches the required information from appropriate nodes
	- *Replication transparency*:
		- transparent to users
		- store copies of data items / fragments at different sites
	- *Loacation transparency*:
		- the location where data is stored is transparent to the user
	- *Naming transparency*:
		- a given name has the same meaning everywhere in the system

### Transaction management in DDBMS
- *Concurrency control*: each site with a copy of an item has a local lock that it cal grant transactions for that item, if a transaction gets **over half** the lcoal locks for an item, it has a **global lock** on the item, if so, it must tell the sites with a copy that it has the lock, if it takes too long time, must stop getting the lock.
- Global transaction `T`:
	1. Starts local transaction `T0` at site1
	2. `T0` instructs other sites to start local transactions `T1`, `T2`, `T3`
	3.  `T1`, `T2`, `T3` find out inventory for product X at sites & send it back to `T0`
	4. `T0` determines how to move product X between sites
	5. `T0` instructs `T1`, `T2`, `T3` to move product X accordingly

#### Two-Phase Commit Protocol
- *Coordinator*: executed at some node & decides if and when local transactions can commit, could run at any other node
- *Logging*: each node locally and send to & received from other
- *Phase 1*: Decide when to commit or abor
	1. Coordinator logging `<PREPARE T>`, send `prepare T` if they want to commit
	2. Each node: decide whether to commit or abort, must decide
		- **Commit**: go into *precommitted state* & logging `<READY T>` and send back `ready T`
		- **Abort**: logging `<DON'T COMMIT T>` and send back `don't commit T` and abort local transction
		- *precommitted state*: only the coordinator is allowed to abort the transaction now
- *Phase 2*: Commit or abort
	 - If all nodes responde `ready T`: logging `<COMMIT T>` and send `commit T` to all nodes, all nodes commit
	 - If some node respondes `don't commit T`: logging `<ABORT T>` send `abort T` to all nodes, all nodes abort

- *Three-Phase Commit Protocol*: divide phase 2 into two parts
	- Phase 2(a): "prepare to commit", send the decision (commit/abort) to all nodes, nodes go into *prepare-to-commit state*
	- Phase 2(b): "commit"

### Query for DDBMS
- Joins `R ⋈ S` at site B: asks site A to send R, A only send data that is actually required, B compute.
- `R ⋉ S := R ⋈ 𝜋common attributes of R and S(S)` on site B: 
	1. site B sends S' := `𝜋common attributes of R and S(S)` to site A
	2. site A sends R' := `R ⋉ S` (= `R ⋈ S’`) to site B
	3. site B outputs `R' ⋈ S`
	- communication cost ≈ |S'| * (size of tuple in S') + |R'|
- In general: |𝜋common attributes(S)| + |R ⋉ S| should be smaller than |R|

### MapReduce
- Divide and conquer a huge number of datasets
- *Map*: the computation ono the smaller chunks of data: **applied to a single key/value pair** and produces a **list of zero or more key/value pairs**
- *Reduce*: how the results are combined to the final result: **group all values by key**
- Easiest (also faster) for MapReduce: use 2 MapReduce computations
- Keys/values can be arbitrary objects
	- keys are typically small
	- values might be larger
##### Selection *𝜎c(R)*:
```python
Map (String tuple, String tuple):
	if tuple satisfies c then output pair (tuple, tuple)

Reduce (String tuple, Iterator <String> tupleCopies):
	output pair (tuple, tuple)
```


### Semistructured Data
*Fully Structured data* (relation model): data has to fit to schema, highly efficient query processing
*Unstructured data*: no description of structure or data, programs have to know how to read & interpret the data
*Semistructured data*:
- *Self-describing*: no schema required
- *Flexible*: e.g., can add & remove attributes on demand
- *Semistructured data model*
	- typically tree or "tree-like"
	- Leaf nodes have associated data types
	- Inner nodes have edges going to other nodes, each edge has a label
	- Root: no incoming edges, is able to reach every nodes
- Forms
	- XML: DTD, Schema, XPath
	- JSON
	- key-value relationships
	- graphs

#### XML
An identical datatype: `XML`, `XML('<XML content>')` when insert

#### XML::XPath
XPath allow us to write queries that return a set of values or nodes from an XML document. Result is returned in document order.
- *Absolute path*: `/E1/E2/.../En`, starts at the root
- *Relative path*: `E1/E2/.../En`, evaluates to another node relatively
- *Attributes*: replace the last tag name by `@A`, shorthand of `attribute::`
- *Wild cards*: `*`, can be used to stand for any tag name or attribute name
- *Previous element*: `..`
- *This element*: `.`

```xpath
-- returns all elements directly below student elements
/students/student/*

-- returns all attributes of modules
/students/student/@
```

##### Navigation Axes
`axis1::E1/axis2::E2/axis3::E3/.../axisn::En`
- `attribute`: an attribute
- `child`: any child, can be omitted
- `parent`: the parent, `parent::*`, **ordered in reverse**
- `descendant`: any proper descendant, `//E`, use it directly to select all elements named "E"
- `descendant-or-self`: any descendant
- `ancestor`: any proper ancestor, **ordered in reverse**
- `following-sibling`: any sibling to the right
- `preceding-sibling`: any sibling to the left, **ordered in reverse**
- `self`: self, `self::*`

##### Conditions
`/axis1::E1[C1]/axis2::E2[C2]/axis3::E3[C3]/.../axisn::En[Cn]`
If the condition is true, follow the path further
- Comparisons: `=`, `<`, `>`, `<=`, `>=`, `!=`
- A value can be **a relative path expression** or **any constant**
- `and`, `or`
- Selection: `[1]`, `[last()]`
- Boolean: 
	- `[category]`, `[@price]`: has a element/attribute with the name
	- `[@price/data()]`: non-empty price attribute
```xpath
-- finds the element preceding an element containing "Maths", reverse document order
//*[.="Maths"]/preceding-sibling::*[1]

-- finds the grandparent of an element containing "Maths"
//*[.="Maths]/parents::*[2]

/products/book/[ebook[format="epub" and title="Databases"]]/author
```

Not included in this document about XPath
- Datatypes
-  Text nodes (to extract the text enclosed in leaf elements)
- Other node tests
- Built-in functions to perform arithmetic, operations on strings, etc.

#### XML::XQuery
Extension of XPath by SQL-like features: **FLWR expressions**, Return lists of values/nodes in document order
- *Let* clause: `let $doc := doc("test.xml")`, assign **the result of XQery expression** to variable, **at least one**, variable names starts with `$`
- *For* clause: `for <variable> in <XQuery expression>`, Consider each item in the result of the XQery, assign it to variable and execute whatever follows the for clause
- *Where* clause: `where <condition1>[, condition2...]`, optional
	- Existential semantics: **Tags aroud an element are removed before comparision**
	- When comparision two expressions, tags are not necessarily removed, it might **comparissing the level of elements**, `/data()` available for contents.
	- Interpreted as true if the result is non-empty
	- `where some/every <$var> in <XQuery> satisfies <condition>`: like ANY/ALL in SQL
- *Order by* clause
- *Group by* clause: 
- *Return* clause: `return $s/name`, mandatory
- *Distinct values*: `distinct-values(<XQuery expression>)`
- *Branching*: if (...) then ... else ...
A query can include **any number of Let & For clauses, interleaved arbitrarily**
```xquery
-- order by
let $doc := doc("mydoc.xml")  
for $b in $doc/books/book  
for $author in $b/author  
order by $author descending  
return <pair>{$b/title}, {$author}</pair>

<pair><title>...</title>, <author>Ben</author></pair>  
<pair><title>...</title>, <author>Anna</author></pair>


-- group by
let $doc := doc("mydoc.xml")  
for $m in $doc/university/student/module  
group by $mod:=$m  
return <pair>{$mod}, {count($m)}</pair>

<pair>COMP105, 2</pair>  
<pair>COMP207, 1</pair>
```

### NoSQL Databases
Not Relational, not restricted to such applications
- Create for typical web applications
	- fast access, millions users in parallel
	- semi-structured, flexibility in the datatype
	- fill ACID sometimes relaced
- often distributed
- *Availability*: every non-failing node always executes queries
- *Consistency*: every read receives the most recent write or an error  
- *Scalability*: more capacity (users, storage, ...) by adding new nodes  
- *High performance*: often achieved by very simple interface (e.g., support lookups/inserts of keys, but do this fast)  
- *Partition-tolerance*: even if nodes (or messages) fail, the remaining subnetworks can continue their work
- *BASE*: *B*asically *A*vailable, *S*oft state, *E*ventually consistent
![[Pasted image 20240113010831.png]]

Common classification
- *Key-value stores*
- *Document stores*: semistructured data associated with an object ID
	- MangoDB
- *Column stores*: table names/column families fixed, column quelifiers vary
	- Columns referenced as `<column family>:<column qualifier>`
	- HBase
- *Graph databases*: store as a graph

### Key-value stores
- Distributed hash table
- Replication
- Versioning and incomparability-resolution using vector clocks

#### Properties
- *Scalability*:  
	- Adding new nodes to increase capacity is easy  
	- Automatic horizontal fragmentation: Add node to free range(s) and move key-value pairs appropriately
- *Availability & fault-tolerance*:  
	- Due to replication  
	- Can retrieve value for a key, even if a few nodes storing values for that key fail  
- *High performance*:  
	- Retrieving the value for a key is fast: apply the hash function to determine the node, then ask the node  
	- Writing, too  
- Problem: ensuring consistency clashes with availability

#### Consistency
- If a newer version of a data item is not yet available at a node, the older version is used/updated
- Method: assign a vector clock to each version of an item X
	- a list/vector of pairs (node, timestamp)
- Use clock to decide if version V1 originated from version V2
	- V1 originated from V2 if for all nodes in V2's clock the corresponding timestamp is less than or equal to the timestamp in V1's clock
	- If it is incomparable, return all possibilities