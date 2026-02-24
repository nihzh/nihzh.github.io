CIA principles
许可 人因 应用

Bad software: worm, virus
- Potential unwanted Programs: Full programs that provide functionality but **the user may not actually want them**

*Adversaries*
- Malicious actors: could be anyone
- Service providers: company / developers
- Big brother
*Assets*: 
- hardware/software
- physical assets
- information
- emotion, reputation, experience
Risk, *threat* and *vulnerability*
- Risk = asset \* threat \* vulnerability

Gap
- Security updates
- Antivirus software
- Account security: password using
- Mindfulness: unknown links/emails

## Authentication
![](../img/Pasted%20image%2020260120202925.png)

- What you have
- What you know
- Who you are

*Multifactor authentication*

*Usable Authentication*
- User friendly
- Reasonable to implement
- Protects against attacks

![](../img/Pasted%20image%2020260120203613.png)

![](../img/Pasted%20image%2020260120204237.png)

怎么设计界面/反馈来改变行为

### Biometry
- Physiological: DNA, Faceprint, Heartbeat, Palmprint
- Behavioural: Gait, Keystroke, Voiceprint, Signature

Emerging: Earable, Teeth Interface, Bone Conduction

![](../img/Pasted%20image%2020260122203243.png)

*Fingerprint*
1. Image acquisition
2. Image processing
3. Minutiae extraction
![](../img/Pasted%20image%2020260122204659.png)

- Vascular pattern
- Face recognition
- Voice Biometrics
- Hand geometry
- Dynamic signature
- Iris recognition
- Retina recognition

## Cookies
*Third party cookie*: large company and public visible, to constrain

Tracked too many things

*User study*
Assess needs
Examine trade-offs
Evaluate
Finding root causes

*Project lifecycle*
![](../img/Pasted%20image%2020260127203243.png)

*Usability testing*
![](../img/Pasted%20image%2020260127205544.png)

![](../img/Pasted%20image%2020260127205159.png)
*Behavioral* –  measures how people actually behave, what they do.  
*Attitudinal* –  measures what people say they think or how they say they behave
*Qualitative* – unstructured data such as natural language.  
*Quantitative* – numerical data. Anything that can be counted or measured with numbers.

Behavioral & Attitudinal question each

## Survey and Analysis
*Cognitive Walkthrough*: a set of experts review and make an informed guess about what will be problematic
*Lab Study*: ask the participant to perform a set of tasks

### In-place lab user studies
Detailed, how, why

### Questionnaires
- quickly
- how prevalent
- can only gather data you know about

Designing and planning is very important
![](../img/Pasted%20image%2020260129203246.png)

**Quantitative the values**: *Likert*-Type Scale Response Anchors
- Level of acceptability
- System usability scale

![](../img/Pasted%20image%2020260129204553.png)

### Planning a survey
#### Descriptive
Learn something about the whole population
- *Descriptive questions*: learn something about the whole population
- *Descriptive numeric*: fancy term for all the basic measures of numeric data
- *Descriptive qualitative*: use data to learn about a whole population

#### Correlation or Causation
Show that two things are related or one thing causes the other thing
- *Correlation*: two things tend to behave in a way that seems inter-related, where if one thing changes the other thing will also change in a related way
- *Causation*: when one thing changes it causes the other ting to change

#### Dependent or Independent
Does X work in Y situation?
- *Dependent* 因变量: outcome variable, the usability goal
- *Independent* 自变量: anything directly manipulating, pre-existing feature of the participant

![](../img/Pasted%20image%2020260129231220.png)

#### Between / Within Subjects
- *Between subjects*: only shows one interface to one person
	- Lots of variability between participants -> more samples needed
	- 随机使用不同的单个样本，对比随机群体的差别
	- 适合强“暴露不可逆”场景
- *Within subjects*: shows all interfaces to all people
	- Less variability but more learning effects and priming
	- *counterbalancing* 顺序平衡
	- 每人使用所有样本，个人视角比较

#### Numeric / Categorical data
*Numeric*
- Continuous: including decimal
- Discrete: only certain values possible
- Interval: only certain values possible and each has distance
	- Likert

*Categorical*
- Binary: true/false
- Ordinal: ordering values
- Nominal: non-ordering values

### Statistical tests
t-test: 
- Independent variable: categorical binary
- Dependent variable: numeric
- Data must be normally distributed

Within subjects, one person gave a confidence answer for both Code Sample A and Code Sample B

## Research Framework
*Inductive coding*: look for any ideas that interest you from different aspects
*Deductive coding*: start with some hypothesis

Reliability
- *Stability* (intra-rater reliability): whether the same coder codes the data in a consistent way throughout the process
- *Reproducibility* (inter-coder reliability): whether different coders code the same piece of data consistently (Cohen's Kappa)

### Frameworks
Frameworks help researchers structure their thinking around problems. Frameworks are proposed by experts in the field and represent how those people think about and break up certain types of problems.

![](../img/Pasted%20image%2020260203205849.png)

#### Communication
安全系统和人的交互
- *Warnings*: alert users to avoid a hazard
- *Notices*: inform users about characteristics
- *Status indicators*: inform users about system info
- *Training*: teaches users about threats and mitigation
- *Policy*: informs users about what they are expected to comply with

#### Communication Impediments
- **Environmental stimuli** may divert users' attention away
- **Interference** prevents communication from being received as intended
	- can be malicious

#### Human Receiver
*Personal Variables*: ability to comprehend and apply communications
*Intentions*: decision of whether to pay attention on a communication
- Attitudes and Beliefs
- Motivation
*Capabilities*: to take proper actions
*Communication delivery*: should pay attention long enough to process it
*Communication processing*: comprehend and acquire knowledge
*Application*: retent the knowledge and knows when it's applicable and to apply it

Users have complex decision making processes around security

### Variables
Attitudinal, Behavioral, Qualitative, Quantitative
![](../img/Pasted%20image%2020260205202012.png)

## Privacy Overview and Privacy by Design
Privacy: The right to control one's own data

### A Taxonomy of Privacy
![](../img/Pasted%20image%2020260206024457.png)

#### Information Processing
- *Aggregation*: 信息收集 combining of various pieces of personal information
	- analyzed, aggregated information can reveal new facts about a person
- *Secondary Use*: 信息二次利用 Using personal information for a purpose other than the purpose for which it was collected
- *Exclusion*: 信息使用不知情 Failing to let an individual know about the information that others have about them and participate in its handling or use
- *Insecurity*: Failing to protect information, potential future harms
- *Identification*: Linking of information to an individual
	- Anonymity and pseudonymity

#### Collection
*Surveillance*: 监视 Watching, listening to or recording of a person's activities
- Continuous monitoring, persistent gawking
*Interrogation*: 审问 Questioning or probing for personal information

#### Invasion
*Intrusion*: 扰人清静 Disturbing a person's tranquility or solitude
*Decisional interference*: 左右决策 Intruding into a person's decision making regarding their private affairs

#### Information Dissemination
*Disclosure*: 披露 Revealing truthful information about a person that impacts their security or the way others judge their character
*Exposure*: 暴露/曝光 Revealing a person's nudity, grief, or bodily functions
*Breach of confidentiality*: 违反保密 Breaking a promise to keep a person's information confidential
- trust issues
*Increased accessibility*: 扩大能见度 Amplifying accessibility of personal information
*Appropriation*: 身份挪用（获取利益） Using an individual's identity to serve the aims and interests of another
*Distortion*: 假信息 Disseminating false of misleading information about a person

### Privacy by Design
- Proactive not Reactive, Preventative, not Remedial
- Privacy as the Default
- Privacy Embedded into Design
- Full Functionality: positive-sum, not zero-sum 隐私$\ne$功能减半
- Lifecycle Protection: End-to-end security
- Visibility and Transparency
- Respect for User Privacy

#### Strategies
![](../img/Pasted%20image%2020260206025232.png)

*Minimize*: Limit as much as possible the processing of personal data
- Select only relevant people and relevant attributes for processing
- Exclude people or attributes in advance of processing it, or better delete it
- Strip away (auto-delete) data as soon as it is no longer needed, complete-destruction system.

*Separate*: Separate the collection and processing of personal data as much as possible
- Isolate: distribute different databases of applications
- Use the equipment of the user

*Abstract*: Limit as much as possible the detail in which personal details processed
- Summarise detailed attributes into more coarse
- Group aggregate information instead of processing individually, present as averages
- Perturb data values to create an approx., e.g. adding random noise

*Hide*: Protect personal data or make it **unlinkable** or **unobservable**, make sure it does not become public or known
- restrict access to personal data, control policy
- obfuscate: encryption, hashes, pseudonym
- Dissociate: break between events, persons and data
- Mix data into larger sets

*Inform*: Inform data subjects about the processing of their personal data in a timely and adequate manner
- Supply resources on the processing of personal data including polices, processes and risks. Provide information about which personal data, how processed, and why processed
- **Notify users** when their data is being processed, shared with third parties or after a data leak

*Control*: Provide data subjects adequate control over the processing of their personal data, offer a real choice
- User **explicit consent** to data processing
- Offer basic functionality available for those who opt-out
- Offer means to review and update their personal data
- All users to retract their personal information

*Enforce*: Commit to processing personal data in a privacy-friendly way, and adequately enforce this
- Make and uphold a policy, assign resources to execute, ensure all technical and org. controls
- Verify policy regularly and adjust implementation

*Demonstrate*: Demonstrate you are processing personal data in a privacy-friendly way
- Document all, record decisions and motivate them
- Regularly audit and review processes and how personal data is processed, provide report to Data Protection Authority

![](../img/Pasted%20image%2020260206064436.png)

### Contextual Integrity
Information flow is appropriate when it conforms with contextual privacy norms

![](../img/Pasted%20image%2020260206070643.png)

## Phishing and Fraud
- Automated
- Impersonation: claims to be from someone trusted
- Direction to a website: look like go to somewhere legitimate
- Contain an attachment: asks for information to be send back / malicious
- Authentication info request: aims to get authentication information

![](../img/Pasted%20image%2020260211003248.png)

### Solutions of Phishing
#### Automatically filter blocks
scan all incoming emails or features
- attachments
- URLs
- address from

Low tolerance for errors, low delay
Encryption + Automation: **Encryption also makes scanning for phishing more challenging**

#### Training users
Sophisticated person surprisingly aware of phishing
- likely due to life experience

Up-front training
- games
- advice web pages
- training videos
Embedded training
- information provided in websites
- feedback given by help desk to phishing reports
Evaluate impact of training
- send out fake phishing emails to test staff
- measure reporting behaviours

- Supports
	- UI indicators: "passive indicators"
	- feedback when phishing is reported or blocked

- Improve protection of authentication credentials

training emotional emails
run tech distributary
Pig butchering scam

### Stanford Fraud Taxonomy (Overview)
- Consumer Investment Fraud（投资/证券）：虚假信息误导投资者
- Consumer Products and Services Fraud（商品与服务：付了钱没得到承诺的东西
- Employment Fraud（招聘/培训类）：虚假就业机会/虚假回报价值
- Prize and Grant Fraud（奖品/补助骗局）：预付款、手续费、税费
- Phantom Debt Collection Fraud（假催收、威胁恐吓）
- Charity Fraud（假慈善募捐）
- Relationship and Trust Fraud： 利用与受害者的个人关系，并且不期望从互动中获得产品或服务。从受害者的角度看，预期的结果式培养个人关系

## Human-Centric Access Control
Subjects: who in control, users
Objects

*Access Control Matrix*
![](../img/Pasted%20image%2020260212201915.png)

*Policies*
- *Discretionary Access Control*: based on identity alone, any propagation of information is allowed
- *Mandatory Access Control*: based on identity and the sensitivity of the object, sharing or any operation on the resource is restricted by security policies
	- Bell-LaPadula: No reads up, no write down
- *Role-based Access Control*: user assigned to groups
	- Mix of DAC and MAC
![](../img/Pasted%20image%2020260212204157.png)

### Permission model
![](../img/Pasted%20image%2020260212204318.png)
Least privilege principle: A system should only have the minimal privileges (i.e., resource access) needed for its intended purposes

hard to read?
how long the permission granted after permitted?

## IoT Security and Privacy
