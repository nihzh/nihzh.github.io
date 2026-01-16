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
new samples are independent and follow the same underlying ???

high dimensional spaces, lost useful of distances, common in su