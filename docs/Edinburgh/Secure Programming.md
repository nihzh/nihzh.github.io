
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

**Memory safety**
A programming language or analysis tool is said to enforce *memory safety* if it ensures that reads and whites stay within cleaerly defined memory areas, belonging to different parts of the program.

**Memory areas**
*Code* (compiled program, lib)
*Data*: non-local program variables, **global** or **static**, program **heap** for dynamically allocated data
*Stack*: dyamically allocated data for each of the currently executing functions/methods, **local**, **current object** reference and **return** address

![](../img/Pasted%20image%2020250923195401.png)

*Stack overflows* mainly relevant for C, C++ and other unsave languages with raw memory access

> The malicious argument overwrites all of the space allocated for the buffer, all the way to the return address location. The return address is altered to point back into the stack, somewhere before the attack code. Typically, the attack code executes a shell.

*Stack* => Abstract Data Type