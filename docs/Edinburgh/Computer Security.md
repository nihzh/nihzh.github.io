Introduction to Computer Security

Security
- Confidentiality: authorized --> Authenticity
- Integrity: The data is untampered and uncorrupted
- Availability: accessable

Trust
- Assurance: The means to know that the system is secure
- Reliability/Resilience: operate intect
- Accountability: The means to verify thta the system is operating as designed (securely...)
- Trust/Trustworthy

私钥只存在于本机中

Privacy
Concerns individuals and their expectations on how their data behaviouors, and interactions are recorded, utilized and spread
- Person gets to control information about themselves
- 不安全的库: 撞库攻击

**teamwork for making secure system**

Threat Modelling
- Who is the adversary
- What are they allowed to do / What cant we prevent them from doing
- What we want to prevent the adversary from doing or learning
- set of threats we want to pretect against given this

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