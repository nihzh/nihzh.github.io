## Introduction
Heartbeating messages: no client can be trust
Injection
Hardware flawed

what do i do for only paper work?

*Safety* is concerned with ensuring bad things don't happen **accidently** e.g., maintanace checks

*Security* is concerned with ensuring that bad thins don't happen because of **malicious actions by others** e.g., terrorists

*Design flaws* are likely
*Bugs* seem inevitable
They lead to vulnerabilities which are exploited by attackers
A security risk assessment for a system should consider different attackers and motives

Privacy, Regulations --> Awareness

Attackers have the advantage
- viable attack route
- anticipate all

Frontiers
- Mobile
- Cloud
- Repeating same mistakes
- Cyber resilience
- Datasharing: privacy

## Landscape
*Threat*: should be robust against local and remote attackers
Security advisors

CVE Identifiers: vulnerability or exposure

*Vulnerability*: A mistake that canbe used by a hacker to violate a "reasonable" security policy for a system 系统漏洞
*Exposure*: S system configuration issue or mistake in software that can be used by a hack as a stepping-stone into a system or network 信息收集，暴露信息

#### BSIMM
- Inform risk management decisions
- Clarigy "right thing todo" for those involved
- Reduce costs via standard, repeatable process
- Improve code quality

*SSI*
- 4 domains covering 12 practices, each practices involves numerous activities
	- Goverance
	- Intelligence
- maturity levels 1-3
- 126 activities

## Memory Corruption
"Coding" stage
Exploits is means to "Fix" and "Learn"

Unconstrained read/writing of memories, lead to arbitrary execution, remote command execution
- stack overflows
- heap overflows
- type confusion
- pointer arithmetic
- out-by-one

Low-level programs manipulate memory directly: C or assembler
- pointer, null pointer

### Memory safety
A programming language or analysis tool is said to enforce *memory safety* if it ensures that reads and whites stay within cleaerly defined memory areas, belonging to different parts of the program.

> A programming language enforces *memory safety* if it ensures that reads and writes stary within clearly defined meory areas.

**Memory areas**
*Code* (compiled program, lib)
*Data*: non-local program variables, **global** or **static**, program **heap** for dynamically allocated data
*Stack*: dyamically allocated data for each of the currently executing functions/methods, **local**, **current object** reference and **return** address

![](../img/Pasted%20image%2020250923195401.png)

*Stack overflows* mainly relevant for C, C++ and other unsave languages with raw memory access

> The malicious argument overwrites all of the space allocated for the buffer, all the way to the return address location. The return address is altered to point back into the stack, somewhere before the attack code. Typically, the attack code executes a shell.

*Stack* => Abstract Data Type

Frame pointer may be used to help locate argumetns and local variables
![](../img/Pasted%20image%2020250925192724.png)

*Spatial memory errors*: memory access goes outside the region of memory that a date item is intended to occupy
*Temporal memory errors*: memory access happens in some regions of memory that the program ought not currently have access to

### Buffer overflow
#### Stack overflows
*Stack variable corrption*
Local variables are put close together on the stack
- If a stray write goes beyond the size of one variable, it can corrupt another
- putting m bytes into a buffer of size n, for m > n
- corrupts the surrounding memory

By *overwriting the return address*, set it to points
- known piece of application code
- shared library
- shellcode: own attack code

##### Write code for an attacker
*Shellcode*
- small and self-contained
- position independent
- free of ASCII NUL (0x00) characters

`execve()`: starts a process with the given name and argument list and the environment as the third parameter
- `#include <unistd.h>` in Standard C Library
- `int execve(const char *pathname, char *const argv[], char *const envp[]);`
	- `pathname`: executable file and its path
	- `argv[]`: arguments to the new program, `argv[0]` as program name
	- `envp[]`: environment variable to the new program, in `"KEY=VALUE"`
- Only return `-1` when failed, then `errno` are set
- 用另一个程序镜像替换当前进程的镜像，调用它的进程回丢弃当前的代码段、堆、栈等用户空间内容，启动一个新的可执行性文件，在同一个PID下运行新程序，如果成功，不会返回
- A exactly to a system call

**Invoking system calls**
Linux calls: 
- store parameters in registers EBX, ECX
- put the desired system call number into AL
- `int 128`
![](../img/Pasted%20image%2020250925233127.png)
`$0x80` equivalent to `128`, the kernel executes the system call according to the value of `EAX`
- `EAX = 11 (0xb)` means `execve` system call
- relavent parameters are set to other registers

**Binary representations**
Encode the hex op code of malicious input
https://shell-storm.org/shellcode
https://www.exploit-db.com/shellcodes

##### Store executable code in memory & implement stack overflow
*shellcode on stack*
*shellcode in another part of the program data*

The overflow uses a **NOP sled** before the shellcode, which the CPU execution "lands on", before being directed to the attack code

![](../img/Pasted%20image%2020250926001729.png)

#### Heap overfows
**Dynamically allocated data** region of memory
- The runtime OS provides *memory management*
- library functions

*Undefined bahavious*
> A programming language specification defines the meaning of progrms. Without memory safety, the specification may say the meaning of an illegal memory access is undefined

`malloc(size)` & `calloc(size)`

##### Spcific heap attacks
![](../img/Pasted%20image%2020250930192747.png)
`strcpy()` function
![](../img/Pasted%20image%2020250930192922.png)
![](../img/Pasted%20image%2020250930192948.png)

might cause crashes

##### General heap attacks
The OS arranges continuously memory chuncks (blocks) to applications

*Heap Blocks Headers*
- size of previous block
- size of this block
- flags (e.g. freeflag)
- if not in use, pointers to next/previous free block

`unlink()` do an arbitrary write

### Out-by-one
字符串的结束符一个字符
Integer overflow: 分配二维矩阵没有检查n\*m数值大小是否溢出，结果会是一个小值或者无效值
### Type confusion errors
*Type safety*
> A programming language, analysis tool or runtime is said to enforce **type safety** if it has a clearly specified typing discipline for data values and it ensures that data values fr types stay within the domain of those during program execution

C
- implicit type conversions
- expllicit type casts

### Memory Corrption Countermeasures
Give devence indepth taht can protect in case of new attacks, malware, regressions to vulnerable code
- Tamper detection in software
- Memory protect in OS and hardware
- Diversification methods

#### Tamper detection
Wrap frame with protective layer, canary sits below return address. Attacker overflows atack buffer to hit return address

Attackers respond to new protection mechanisms by looking for mulnabilities th those mechanisms

#### Memory mode protection
Isolation different processes have different resouces
Sharing resources are shared between processes, partial isolation

Granularity of protection
- *Fencs*: separate memory accesses between OS and user code
- *Base and bounds regiester*: enforce separation between several programs allowing access control on memory ranges
- *Tagged architecture*: tag on each memory locatoin set access rights to stored word, not supported in modern
- *Paging*: split program/data into pieces, mapped onto memory separately

#### Diversification
Make many versions of same program; thwarts general attacks that assume some fixed structure
*ASLR*: randomising layout suring load time makes it harder to find data or code locations
- small amounts could be brute force

#### Defensive programming
*Bounds checking*
- data length
- array subscripts
- boundary conditions: off-by-one
- size of inputs
- dangerous API calls

![](../img/Pasted%20image%2020251007195427.png)

*Automated code review*: code checking tools
- Memory faults
	- Valgrind: Dynamic runtime vulnerability, 
	- AddressSanitizer: compile time

## Injection
*CWE: Common Weakness Enumeration*
25 top

**Always check your inputs!**

Downstream component
- call to a library function
	- picture / movie
	- execute an OS command
- a message sent to another service
	- web query / web API call
	- query database

*Trust assumptions*
Programmers make trust assumptions concerning which parts of the system they believe will behave as expected.

### Command injection
Programmers often insert **system command** calls in application code, interpreted by a **command shell**

Metadata & meta-characters
- In-band representation: embeds metadata into the data stream
- Out-of-band representation: separates metadata from data

separators / delimiters
escape-sequence: describe additional data

*Input validation*
Block lists (characters)
- reject
- filter
- sanitize

Sub-process: risky as they invoke a **shell** to process the commands
- `system()` in C, equivalently to `/bin/sh -c <cmd>`
- `popen()` executes a command as a sub-process, returning a *pipe* to send or read data

Some attacks exploit differences in meta-characters between languages

environment variables

DLL in Windows: search order to PATH environment variables
Unix use a search path which can be defined/overridden by variables
	`LD_LIBRARY_PATH`
	`LD_PRELOAD`

IFS changing CVE-2014-6271
### SQL Injection
Routes
- GET/POST
- Cookie
- 服务器变量（HTTP header）
- 二次注入

提取，修改，绕过认证，执行任意命令

Forms of SQL Injection
- 恒真
- 报错回显
- `UNION`联合查询
- `;`双语句查询
- 布尔盲注、时间盲注
- 数据库存储过程漏洞

Idea: use static analysis pre-processing to generate a dynamic detection tool:  
1. Find SQL query-generation points in code  
2. Build SQL-query model as NDFA which models SQL grammar, transition labels are tokens  
3. Instrument application to call runtime monitor  
4. If monitor detects violation of state machine, triggers error, preventing SQL query  
#### Defence
静态分析 动态监测攻击 SQLRand
## Racing
### Race conditions
多进程和多CPU并行，
![](../img/Pasted%20image%2020251016193515.png)
访问文件的时间窗口差
在检查和open之间对文件修改恶意代码
*Unix*
1. 多次解析相同文件
2. Permission Races: 文件创建时是`0666`
3. Ownership Races
4. Directory Races
5. Temporary File Races
	- `fd = mkstemp(temp);`
### Data Races
两个或多个线程，访问同一共享变量，多次读写导致非确定性结果
Atomic memory accesses
Multi-threaded programs

> A data race occurs when two or more threads access a shared variable:  
1. (potentially) at the same time, and  
2. at least one of the accesses is a write

*No out-of-thin-air*
Write speculation in JAVA

- Ensuring atomicity: enforce mutual exclusion
- Using locks: mutual exclusion for shared resources

Dynamic analysis: monitor every access to every memory location and see whether the access might have reces with a previous access from a different thread
- *Lockset algoorithm*: every shared variable is protected by at least one lock
![](../img/Pasted%20image%2020251021193652.png)
- Eraser tool
![](../img/Pasted%20image%2020251021192935.png)

Static analysis
GuardedBy

## Secure development
*McGraw's Three Pillars*
![](../img/Pasted%20image%2020251021193233.png)

Run security activities alongside traditional

![](../img/Pasted%20image%2020251021193503.png)

### Code review
- industry: economy choices, rush, no extratime
- Manual: -> agile
	- subtle
	- onerous, large code bases
- Automatic: human config, increasingly sophisticated

### Architectural risk analysis
  
- the security threats that attackers pose to assets  
- vulnerabilities that allow threats to be realised  
- the impact and probability of an attack  
- hence the risk, as risk = probability × impact  
- countermeasures that may be put into place
![](../img/Pasted%20image%2020251021195019.png)

![](../img/Pasted%20image%2020251021195000.png)

![](../img/Pasted%20image%2020251021195051.png)

Think adversarily

![](../img/Pasted%20image%2020251021195319.png)

### Penetration testing
Ethical hacking: finds real problems
Modern professional pen testing uses source
last check before deployment, use as regression tests
For repairing software, not deploying work-arounds

### Security testing
*Strategy for security testing*
![](../img/Pasted%20image%2020251021200146.png)