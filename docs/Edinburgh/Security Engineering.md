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