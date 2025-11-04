Introduction to Computer Security

*Security*
- Confidentiality: authorised --> Authenticity
- Integrity: The data is untampered and uncorrupted
- Availability: accessible

*Trust*
- Assurance: The means to know that the system is secure
- Reliability/Resilience: operate intact
- Accountability: The means to verify that the system is operating as designed (securely...)
- Trust/Trustworthy

私钥只存在于本机中

*Privacy*
Concerns individuals and their expectations on how their data behaviours, and interactions are recorded, utilised and spread
- Person gets to control information about themselves
- 不安全的库: 撞库攻击

**Teamwork for making secure system**

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

**SYN Flooding**: sending thousands of SYN requests to the victim, without ack any replies. Bob accumulates more SYN packets than he can handle, runs out of space in **state table**
- attack don't need his own IP address, forge the source of the TCP packet
- attacker's own bandwidth, likely smaller than server's

*Smurfing*
Expoloits ICMP **ping** requests thereby remote hosts respond to echo packets to say they are online. Some network respond to pings to **broadcast** address => *Smurf amplifiers*
- Ping a LAN on a broadcast address, then all hosts on the LAN reply to the sender of the ping

![](../img/Pasted%20image%2020250924170835.png)

### Application Layer
![](../img/Pasted%20image%2020250924171000.png)
Domain name contains not only latin alphabet
DoS attack on major DNS provider
- DNS Servers are soft targets for attackers
- Take out the mapping and the website goes "offline"

Authoritative name server: Stores reference version of DNS records for a zone (prartial tree)

Name Resolver
- Program that retrieves DNS records
- Connect to a nameserver (default, root, or given)
- Caches records received

```sh
ipconfig /displaydns    # view caches
ipconfig /flushdns      # clear caches
```

DNS Cache Poisonoing
Give a DNS server a false address record and get it cached
- UDP on port 53
- 16-bit requeist identifier in payload to match answers
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

### Application layer protection
#### Firewall
prevent unauthorized electronic access
- firewall policies: Blocklist/Allowlist

**packet filters(stateless)**
Each packet attempting to travel through it in isolation without considering packets that it has processed previously

**stateful filters**
maintains records of all connections passing through it and can determine if a packet is either the start of a new connection
- maintaining tables on each active connection
- port scan

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

*Rule-based*: attack pattern signature

## Cryptography
### Symmetric encryption
![](../img/Pasted%20image%2020251001170444.png)

Kerckhosff principle
- E and D algorithms are public
- security relies entirely on the secrecy of the key

![](../img/Pasted%20image%2020251001171006.png)

Frequency Analysis

#### One-Time Pad
![](../img/Pasted%20image%2020251001173136.png)

Perfect secrecy
![](../img/Pasted%20image%2020251001172949.png)
![](../img/Pasted%20image%2020251001173325.png)
same likelyhood of keys behind the ciphertext

*Two-time pad attacks*


Getting treu randomness
- the key should not be gurssable from an attacker
- if the key is not truly random, frequency analysis might again be possible

OTP is mellable
> given the ciphertext 𝑐 = 𝐸(𝑘, 𝑚) with 𝑚 = 𝑡𝑜 𝑏𝑜𝑏 ∶ 𝑚0, it is possible to compute the ciphertext 𝑐′ = 𝐸(𝑘, 𝑚′) with 𝑚′ = 𝑡𝑜 𝑒𝑣𝑒 ∶ 𝑚0 
> 𝑐′ ∶= 𝑐 ⊕ "𝑡𝑜 𝑏𝑜𝑏 ∶ 00 ... 00" ⊕ "𝑡𝑜 𝑒𝑣𝑒 ∶ 00 ... 00"
#### Stream Ciphers
Use a pseudooramdom key rather than a really rondom key
*Pseudo-Random Gernerator*
![](../img/Pasted%20image%2020251001174638.png)

RC4: used in HTTPS and WEP
seed

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
- RSA
- Discrete Logarithm Problem
- Diffie-Hellmam Problem

#### No TTP Asymmetric key distribution
*Diffie-Hellman protocol*: good for ephemeral encrypt
![](../img/Pasted%20image%2020251010171318.png)

raw RSA ==> Man In The Middle

![](../img/Pasted%20image%2020251010174757.png)

加密find解密
算法proof

#### Signatures
Data integrity and origin authenticity in the public-key setting
![](../img/Pasted%20image%2020251013171645.png)

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
- Certificate Revocation Lists (CRLs)
- Online Certificate Status Protocol (OCSP)

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

Multi-users: isolate different users
Multi-tasks: isolate different applications running

*Unix architecture*
- *kernel
	- supports secure sharing of low-level resources between users/applications
	- limits how applications access computer resources
- *Exucution modes*
	- *User mode*: access to resources through syscall to kernel
	- *Kernel mode*: direct access to resources
		- direct interaction with hardware
- *System calls*: programs, C library `libc`

*Processes and process management*
- an instance of a program currently executing
- unique PID for each
- loaded into RAM
- CPU time, meory useage, program name...
- fork: control other processes and **child process inherits context from parent process**

#### RAM: 
- code for the running program
- input data
- working memory
- `%eip` to points to next instruction

Stack: from higher to lower `%esp`
Heap: from lower to higher

*Virtural memory*: a section of the hard drive to emulate RAM
- Memory Management Unit maps logical address -> physical address

![](../img/Pasted%20image%2020251017173451.png)

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

**Open design**
The security of a mechanism **should not** depend on its secrecy
The design and implementation details always get leaked

When designing a security mechanism **keep it simple**
- security researchers: allow verification
- delopers: avoid bugs
- users: avoid misuses

*Security principles*
*Fail-safe defaults*: default configuration should be conservative
*Complete mediation*: every access to a resource must be checked for comliance with security policy
*Usable security*: UIs and security machanisms should be designed with the ordinary user in mind, the users should be supported in interacting in a secure way with the system

### Privilege separation
***Who is allowed to access what and how***

Complete meditation: all requests go to the reference monitor
The **reference monitor** grants permission to users to apply certain opperations to a given resource

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