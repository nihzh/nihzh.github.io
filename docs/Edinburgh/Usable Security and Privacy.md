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

### Privacy
#### Information Processing
- *Aggregation*: 信息收集 combining of various pieces of personal information
- *Secondary Use*: 信息二次利用 Using personal information for a purpose other than the purpose for which it was collected
- *Exclusion*: 信息使用不知情 Failing to let an individual know about the information that others have about them and participate in its handling or use
- *Insecurity*: Failing to protect information
- *Identification*: Linking of information to an individual

#### Collection
*Surveillance*: 监视 Watching, listening to or recording of a person's activities
*Interrogation*: 审问 Questioning or probing for personal information

#### Invasion
*Intrusion*: 扰人清静 Disturbing a person's tranquility or solitude
*Decisional interference*: 左右决策 Intruding into a person's decision making regarding their private affairs

#### Information Dissemination
*Disclosure*: 披露 Revealing truthful information about a person that impacts their security or the way others judge their character
*Exposure*: 暴露/曝光 Revealing a person's nudity, grief, or bodily functions
*Breach of confidentiality*: 违反保密 Breaking a promise to keep a person's information confidential
*Increased accessibility*: 扩大能见度 Amplifying accessibility of personal information
*Appropriation*: 身份挪用（获取利益） Using an individual's identity to serve the aims and interests of another
*Distortion*: 假信息 Disseminating false of misleading information about a person



Privacy by design
- Minimize
- Separate
- Abstract