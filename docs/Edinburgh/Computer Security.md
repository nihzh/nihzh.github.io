Introduction to Computer Security

Security
- Confidentiality: authorised --> Authenticity
- Integrity: The data is untampered and uncorrupted
- Availability: accessible

Trust
- Assurance: The means to know that the system is secure
- Reliability/Resilience: operate intact
- Accountability: The means to verify that the system is operating as designed (securely...)
- Trust/Trustworthy

私钥只存在于本机中

Privacy
Concerns individuals and their expectations on how their data behaviours, and interactions are recorded, utilised and spread
- Person gets to control information about themselves
- 不安全的库: 撞库攻击

**teamwork for making secure system**

Threat Modelling
- Who is the adversary
- What are they allowed to do / What cant we prevent them from doing
- What we want to prevent the adversary from doing or learning
- set of threats we want to protect against given this

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