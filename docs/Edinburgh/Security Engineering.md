> Security engineering is about building systems to remain dependable in the face of malice, error and mischance

Threat model framework
- *Security policy*: what you are supposed to achieve
	- 可判定、可执行、可审计
- *Protection mechanism*: how to implement policies
- *Assurance*: reliability for assessing combined mechanism
- *Incentives*: motives for attackers and defenders

Individual / Business risks

Quantifying the impact of non-financial harm is hard

> Abuse is the technically correct use of the products we build, to cause harm

Socially engineered rather than hacked

## Who is the Opponent
digital threat modelling is hard

### Criminals: The Crooks
Financially motivated actors willing to break the law
- Ransomware gangs
- botnet operators
- fraud gangs
- malicious insiders

#### Cyber-Dependent Crime
**DDos (~2005)**
Flood a system with traffic

Cash out: hiring
> It's easier to cash out when the adversary pays you than the victim.

**Info stealing + selling (~2005)**
- worth & price gap
- Access to a network or machine with sensitive data
- A market to find buyer, plus a cash out mechanism

**Extortion**
- Access to a network or machine
- Encryption software and/or exfiltration
- Negotiation skills
- cash out

#### Cyber-Enabled Crime: scale, speed, reach
- Cyber investment fraud
- 利用网络进行犯罪：虚假网站，直播诈骗，社工社交

#### Cyber-Assisted Crime

![](../img/Pasted%20image%2020260115182253.png)

### State Actors: The spooks
Potentially motivated actors with near endless resources

The Five Eyes: USA, UK, Canada, Australia and New Zealand share intelligence infra
Russia
China
Third-tier

### Lawful Operators: The geeks
Good actors with technical skills and/or elevated access

Employees (insider), security researchers, competitors
 
Freelance hackers 雇佣安全研究者
- sell vulnerabilities
- sell hacking activities

Responsible Disclosure: *CERT*

### The swamp
Variously motivated actors with few technical skills
Hate crimes, Sex abuse, Bullying

Online mobs: manipulate algorithms by mimicking virality, weaponizing privacy

Children, Family members
Extremists

## Security policy
What are we trying to stop?
How are we trying to stop it?
With what mechanisms?
![](../img/Pasted%20image%2020260119181535.png)

*Discretionary Access Control (DAC)*: regular companies
- asset owners decide who should have access
- public resources are public
- VPN solves offsite work

*Mandatory Access Control (MAC)*: dealing with insider threat

### Multilevel Secrecy (MLS)
- *Top Secret*: compromise could cost many lives or do exceptionally grave damage to operations
- *Secret*: compromise could threaten life directly
- *Confidential*: compromise could damage operations
- *Official*: compromise might embarrass

Resources have classifications
People (principals) have clearances
**Information flows upwards only**

#### Bell-Lapadula
A safe system stays safe
- simple security policy: **no read up**
- \*-policy: **no write down**
Minimize the Trusted Computing Base (set of hardware, software and procedures that can break the security policy) in a reference monitor

Covert-channel info leak
Too much clearance
Classify too much

### Multilateral Secrecy
Not easy to find hierarchy, just stop data flowing down
*The Lattice Model*: manage compartmented data by adding labels
- BLP requires only a partial order
- (level, categories)

*Subject*: a physical person
*Principal*
- a person
- equipment
- a role
- a complex role

### Multilevel Integrity
*Biba model*: info only down from high-integrity to low-integrity

## Banking & Finances
*Clark-Wilson Policy Model*
Triples (subject, TP, CDI) enforce separation of duty

**Transferring: banks move money around**
*Authentication*: SMS, biometric
Geography impacts digital threats: kidnapping...

**When the bank is not directly involved in the transaction**
Contactless

Of Alexa top 500 websites
- 26 use primary account number + exp date
- 37 use PAN + postcode (numeric digits only for some, add door number for others)
- 291 ask for PAN + expdate + CVV

- Forging signature of a physical cheque
- Getting access to victim's banking website account/app
- Impersonating card, stealing/bypassing PIN, manipulating terminal
- Compromise SWIFT to manipulate interbank transfers

![](../img/Pasted%20image%2020260122185440.png)

> If Alice guards a system bug Bob pays the cost of failure, you can expect trouble!

*Principal-Agent problem*
- Principal: pay the cost of the risk
- Agent: actual control, decision and execute the system

### Externalities
A public good: 
- non-rivalrous
- non-excludable

*Information Asymmetries*

*Market Power*
- **Low marginal costs**: reproducing information is close to zero
- **Switching costs**: the net present value of your customer base of the total cost of switching
- **Network externalities**: the value of a network is proportional to the square of the number of users

*Dominance impacts*: 
- 抢占市场资源 + 安全反馈缓慢昂贵且暴露缺陷 = agile，优先发布，security debit

*Monopoly*: 垄断带来的市场生态单一，一处漏洞影响大量主体

## Psychology and Usability
Largest compromise: **Human errors**, often authorized by the victim

People make errors in not following the rules

![](../img/Pasted%20image%2020260129170934.png)

Attacking knowledge-based behaviors
- advance payment fraud: present mark with an opportunity
- CEO fraud

Attacking rule-based behaviors
- Tell finance department that their vendor's bank details have changed
- Malware in app store

Attacking skill-based behaviors
- Motor skill slips: URL typo
- Visual recognition limitations: foreign characters, subdomain manipulation
- Habituation: ads with X

### Safety & Security
Under pressure, humans regress from knowledge -> rule -> skill based control
- safety: stress is an unfortunate byproduct
- security: stress is manufactured
	- time pressure
	- authority

curiosity

Big brains track more relationships
> Machiavellian aspect: if you’re better at deception, and at detecting deception in others, you’re more likely to have descendants

### Behavioural economics
![](../img/Pasted%20image%2020260129172936.png)
*Risk aversion*
*Loss aversion*: loss domain risk-seeking
- People facing losses take more risks

### Defenses with security in mind
*Training*
- often annually with a compliance requirement
- after 8 months, failure rose from 10% to over half of users
- only avoid common cyber risks, threats is correlated with lower incidents

**perimeterisation** is a bad mental model
People are more likely to follow security advice consistent with their mental model
Changing defaults: 安全沟通不是堆知识点，而是**先纠正模型/用用户能接受的类比重建模型**。

*User authentication*
- Something you know: password, knowledge, passphrase
- Something you are: face, fingerprint, retina
- Something you have: phone, token, key

*Warnings Habituation*
Warning: conscious reasoning --> automated reactions
click through often rapid --> skill based (attack)
security should be so normal
learning from flaws

![](../img/Pasted%20image%2020260130010550.png)

## Feedforward
specific about capabilities
enforcement

## Network Security
*Perimeterisation* ==> *Zero-trust Networking*

BGP attacks
Denial of Service
- amplifier attacks 
- synchronisation cookie
Malware

Firewalls
Intrusion Detection System

## Hardware Security
Temper resistance: 
- no way to know the physical system has been attacked
- moving to the digital world

physical form of watermark
blockchain for digital currency

Side channels: ultrasound also captured by devices
tracing