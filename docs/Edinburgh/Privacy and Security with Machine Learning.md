> Machine Learning is the study of algorithms that improve their **performance P** at a **task T** with **experience E**

## Introduction
Focus on Algorithms
![](../img/Pasted%20image%2020260113182910.png)

Data acquisition -> Data preparation -> Model training -> Model testing -> Model deployment

Adversaries with ML:
- Automation: lower cost and larger scale
- Synthesis
- Pattern extraction
- Network traffic analysis, Data deanonymisation, Hardware side-channels

Classification of samples ==> threat model extraction
"urgency"

## Basics
### Machine Learning
*Supervised -- Classification*
Given a set of observation with labeled, assign labels to new instances
- measure ***characteristics*** and **features**
- Decision threshold `f(x)`, a hyperplane in linear models
- Give an algorithm to fix the task

#### Non-linear models
Non-linear, introduce new dimension
Non-linear models: Neural networks
- activation function
- loss function: find best `w` which minimise the lost
- gradient descent
- backward propagation

#### Evaluation
- generalisation: bias-variance trade-off
- separate dataset
- confusion matrix & predictive performance metrics
- ROC curve

**Class imbalance**
misleading result for classifying result
the accuracy high, but precision is very low

**IID assumption**
new samples are independent and follow the same underlying distribution 
mapping from inputs (feature vectors) to outputs (classes)
high dimensional spaces, lost useful of distances, common in su

### Computer Security
Policy -- Threat model -- Mechanism
Try to figure out all possible actions attackers can do
**You can never achieve perfect security**

- *Confidentiality*: only *authorized* entities can access the information
- *Integrity*: the data is **untampered** and **uncorrupted**
- *Availability*: both the data and the system that provides access to it are there **when you need** them

Cryptography:
- ensures confidentiality -- only accessible by keys
- authenticating users -- digital signatures
- ensures integrity

Threat modelling in communication systems
- Passive (read) - Active (add, remove or modify)
- Internal (control one or several system components) - External (only control communication links)
- Local (only sees part of the system) - Global (access to the entire system)
- Targeted (compromise a specific set of users) - Untargeted (attempts to compromise any user)

Specification -> Design -> Implementation -> Assurance
- Designed to achieve a security goal
- Defense embedded
- New defensive system alongside an existing, unmodified system

*Trust*
- *Assurance*: the means to know that the system is secure
- *Reliability/Resilience*: they are robust and continue operating intact or gracefully degrade
- *Accountability*: the means to verify that the system is operating as intended

*Privacy*: Concerns individuals and their expectations on how their data, behaviours, and interactions are recorded, utilized, and spread

*Anonymity*: set of individuals that share the same attributes

## Application of ML to Traffic Analysis
Traffic analysis: Passively analyze communication metadata to extract information

*Tor* 
Website / Protocol Fingerprinting (WF)
- attacks can be deployed by a low-resource adversary
- some Tor users are especially vulnerable

Training a model by datasets of fingerprinting, for predict content and routs, driven by ML innovation
![](../img/Pasted%20image%2020260130204141.png)

Closed world/ Open world
![](../img/Pasted%20image%2020260207054832.png)
现实世界很多unmonitored，模型需要先判断是否monitored

The base rate fallacy
![](../img/Pasted%20image%2020260130203423.png)

Defences:
- generate some dummy random package, encrypt and send as normal
- delay the sending
- escape from the pattern

![](../img/Pasted%20image%2020260130204455.png)

## Malware
Intrusive programs, for gaining profit
- cause damage
- steal information
- ransom
- take control of devices

Extract the signature and do blocking: hash, specific bytes...
- Can be overpass by just modify the malware program a little bit

ML classifier: selecting appropriate features
Find efficient representations automatically

Characteristics of the malware
- Static analysis: source code without execute
- Dynamic analysis: program while running
- Hybrid

### Static Analysis
**Drebin**: xml file, disassembled code
Access to hardware components
Permissions
App components: interfaces, activities, services, content providers and broadcast receivers
- suspicious API calls
- used permissions
Network address
Intent filters

Embedding binary features in vector space
- Linear SVM: test is the inner product between point and hyper-plane

### Dynamic malware detection
- **Traces of execution**: malicious behaviour
- **Features to extract**: APIs, IP address connecting, services interacting
- **End-to-end learning**: action sequence -> list of tokens to apply NLP

*Gradient Descent* to find an approximate solution
Find perturbation 𝜹 s.t. perturbed input 𝒙𝟎 + 𝜹 is misclassified
![](../img/Pasted%20image%2020260207061245.png)

*Evasion*: modify input such that it preserves malicious intent but is detected as benign
- The 𝜹 is 'noise' added to the input, but not random
- crafted to maximize the error of the classifier $$\delta^*=\arg\underset{\delta\in\mathcal{C}}{\min}s_{mal}(x+\delta)$$
![](../img/Pasted%20image%2020260207064340.png)

### Modeling assumptions
#### Access to model parameters (unrealistic)
Threat model in ML security/privacy
![](../img/Pasted%20image%2020260207063807.png)

#### Feature mapping is invertible (semantic gap)
*Features space representation*: the abstract representation of software applications as vectors of descriptive features used to train and test machine learning based malware classifiers

*Problem space representation*: the original, unprocessed form of the software application from which features are extracted

Semantic gap: Problem imposes constraints on possible perturbations
在feature space找到$\delta$不代表能在problem space实现
- legit?
- which semantics?
- how to verify automatically
- preprocessing?

#### IID assumption (adversarial drift)
dataset shift, distribution shift, concept drift...
  
The noise is not stochastic but adversarial: The adversary adapts to stay under the radar -- shifting the concept of malware over time
![](../img/Pasted%20image%2020260207070251.png)

![](../img/Pasted%20image%2020260207070440.png)

**Experimental bias**
Temporal Inconsistency in Train/Test Sets

## Privacy and Anonymization
Sharing data & protect privacy

After anonymized, the interception of multiple datasets acts as a *quasi-identifier* 准识别符，组合后高度可识别

*Personality Identifiable Information (PII)*: any information that can uniquely identify a specific person

Bigdata analysis
Data protection regulation does not apply to anonymized data

> There is no perfect mechanism to fully protect privacy of data

Third parties / public can always have auxiliary information
![](../img/Pasted%20image%2020260207011426.png)

### K-anonymity (Sweeny)
A dataset satisfies k-anonymity of the records associated with each individual in the dataset cannot be distinguished from at least k-1 other individuals in the dataset
- suppression and generalization such that quasi-identifiers map to k or more people 一个准标识符映射到至少k个个体
- enables a **trade-off** between utility and privacy
![](../img/Pasted%20image%2020260207011926.png)
- assumes that auxiliary knowledge is bounded (fixed)
- *l-diversity*, *t-closeness*

> It is unreasonable to expect that a privacy mechanism will provide **utility** and at the same time **prevent all individual inference** for **arbitrary auxiliary knowledge**

**Homogeneity attack**: all k-records have the same sensitive value
**Background knowledge attack**: e.g., low incidence of disease for a demographic

Sparse data: sparsity means that rows are more likely to be unique

> In general, we cannot know the adversary's background knowledge: we cannot bound it!

### Statistical Disclosure Control (SDC)
> nothing about an individual should be learnable from the database that cannot be learned without access to the database

Aux. info: “Alice is 8cm shorter than average”

## Differential Privacy
A randomized algorithm $\mathcal{M}$ is $\varepsilon$-differentially private if for all adjacent datasets $D,D'$ and for all $S\subseteq Range(\mathcal{M})$
$$Pr[\mathcal{M}(D)\in\mathcal{S}]\le e^\varepsilon Pr[\mathcal{M}(D')\in\mathcal{S}]$$
where $\varepsilon$ is a parameter called the *'privacy budget'*

"Distance between output distributions is at most $\varepsilon$"
个体层面被随机化（噪声）保护，但总体统计仍可恢复

*Local DP: Randomized Response*
Parameter `p` (randomizing) adjusts privacy-utility trade-off
以p概率说真话：
- 1: no privacy
- 1/2: perfect privacy

以概率 p 说真话，以概率 1-p 说假话
观测到“回答 Yes 的比例” γ，可反推总体真实比例 x $$\gamma=px+(1-p)(1-x)\Rightarrow x=\frac{\gamma+p-1}{2p-1}$$

**Continuous values f(x)**: add noise sampled from a probability distribution cantered around 0 $$f(x)+Y~where~Y\sim Lap(0,\sigma)$$

**Sensitivity**: 换掉一个人的数据，统计量最多能变多少
$$\Delta f=\underset{D\sim D'}{\max}|f(D)-f(D')|$$

*Local DP*: 数据提供者发送前加噪 (1 query)
*Global DP*: 可信数据库管理者提供查询接口 (n queries)
- n的数量受限于privacy budget

$(\varepsilon,\delta)$-DP
$$Pr[\mathcal{M}(D)\in\mathcal{S}]\le e^\varepsilon Pr[\mathcal{M}(D')\in\mathcal{S}]+\delta$$
where $\delta$ is Failure probability, $M$ is $\varepsilon$-DP with probability $1-\delta$

Mechanisms
- **Robustness to post-processing**: it is safe to apply arbitrary functions on output
- **Composition**: if we run a $(\varepsilon,\delta)$-DP mechanism $k$ times, the resulting mechanism is $(k\varepsilon,k\delta)$-DP
- **Advanced composition**: if $k\lt\frac{1}{\varepsilon^2}$, the resulting mechanism is $(\mathcal{O}(\sqrt{k~log(\frac{1}{\delta'})})\varepsilon,k\delta+\delta')$-DP for all $\delta'\gt0$ 
- **Amplification**: if we sample a fraction $q$ of the data, our mechanism becomes $(q\varepsilon,q\delta)$-DP

A rigorous "worst-case" mathematical definition of privacy, independent of background knowledge of auxiliary data

Hard to interpret, hard to pick Epsilon, privacy budget

*DP-ERM*
- Output perturbation: minimize then perturb
- Objective perturbation: perturb then minimize

*DP-SGD*: calculate gradient over sample iteratively, apply DP at that level
### Private Learning
DP mechanism sits within the learning algorithm, Once the model has been trained, it can be safely released
![](../img/Pasted%20image%2020260224225939.png)

## ML for Intrusion Detection Systems
Intrusion Detection: sensing and analysing system events for the purpose of noticing attempts to access system resources in an unauthorized manner

IDS ??

**Host-based IDS**: run directly on the hosts
**Network-based IDS (NIDS) ??

### Signature detection
look for patterns (signatures of intrusion)
**Rule-based**: 
- network (headers, payloads)
- host (events)

### Anomaly detection
Data point or pattern that does not conform to normal behaviour
- outliers
- abnormalities
- deviations

Classification discriminative

Positive unlabeled: intrusion are positive

![](../img/Pasted%20image%2020260224184057.png)

LUCID
- features: 10 features from the first n packets of a flow
- model: CNN

baseline not reflect real-world settings

label inaccuracy
noise exists, mitigate