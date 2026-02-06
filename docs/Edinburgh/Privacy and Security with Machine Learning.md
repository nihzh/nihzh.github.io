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