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