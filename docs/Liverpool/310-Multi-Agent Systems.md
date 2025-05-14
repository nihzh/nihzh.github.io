### Agents
Agents are objects with **attitude**, do for **personal gain**
- Autonomous
- Smart
- Active: inherently multi-threated

*Expert Systems*: capable of solving problems or giving advice in some knowledge-righ domain
- inherently disembodied

Environments
- Fully observable vs. partially
	- agent can obtain complete, accurate, up-to-date infor mation about the environment state
- deterministic vs. non-deterministic
	- any action has a single guaranteed effect
	- the physical world can to all intents and purposes be regarded as non-deterministic
- static vs. dynamic
	- remain unchanged except by the rperformance of actions by the agent
	- has other processed operating on it, and which hence changes in ways beyond the agent's control
- discrete vs. continuous
- episodic vs. non-episodic(sequential)
	- episodic: each state is independent of each other, current action will  not affedct a future action
	- the current decision affects future decisions
- Real time: time plays a curcial part in evaluating an agent's performance

#### Intelligent agents
- *reactive* (encironment aware): maintains an **ongoing interaction** with its environment, and responds to changes that occur in it
	- perceive and respond in timely fashion to changes
- *pro-active* (goal-driven): generating and attepting to achieve goals; not drivent solely by events; taking the initiative
- *social ability*: we cannot go around attempting to achieve goals without taking other into account
	- *cooperation*: working together as a team to ahcieve a shared goal
	- *coordination*: managing inter-dependencies between the activities of agents, recources\*
	- *negotiation*: the ability to reach agreements on matters of common interest

#### Intentional Systems
Having some mental states
- physical stance
- design stance
- intentional stance

> whose behaviour can be predicted by the method of attributing belief, desires and retional acumen

- First-order intentional system: 
	- desires and beliefs
	- no desires and beliefs of desires and beliefs
- Second-order intentional system:
	- has desires and beliefs of desires and beliefs (own)
	- no doubt other intentional states

***low level explainations become impractical***

Intentional stance description useful to understand
- strucure of the machine
- part or future behaviour
- how to repair or improve it
- explain and predict a complex system's behaviour without having to unserstand how the machanism actually works

### Abstract Architectures
![](../img/Pasted%20image%2020250203173527.png)

#### Runs
$R$ be the set of all such possible finite sequences (E and Ac)
$R^{Ac}$ be the subset of these that end with an action
$R^{E}$ be the subset of these that end with an environment state

$r, r', ...$ to represent the members of $R$

#### Environments
The effect that an agent's actions have on an environment
$$\tau : R^{Ac} \rightarrow 2^E$$
- History dependent: the next state not only dependent ont the actino of the agent, but earlier actions may be dignificant
- Non-deterministic: some uncertainty about the result of an action
$\tau(r)=\Phi$ : There are no possile successor states to `r`, the run has ended, then `Env` is a triple
$$Env=<E,e_0,\tau>$$
Where `E` is a set of states, $\color{#b293f6}e_0\in E$ is an initial state, and $\tau$ is a state transformer function 

#### Agents
A function which map runs to actions
$$Ag:R^E \rightarrow Ac$$
##### Purely Reactive Agents
- do without reference to their history
- base their decision making entirely on the present

#### Systems
A pair containing an agent and an environment
Any system will have associated with it a set of possible runs
$$R(Ag,Env)$$

#### Perception
`see` represents the agent's ability to obtain information from its environment. The agent has soome initernal data structure, which is typically used to record information about the environment state and history
$$see:E\rightarrow Per$$

#### Next state functions
`I` be the set of all internal states of the agent

![](../img/Pasted%20image%2020250204172726.png)

#### Utility functions
- Associate **rewards** with states that we what agensts to bring about
- Associate **utilities** with individual states
	- The utility of a state is a numberic value representing how good a state is
	- The task fo the agent is then to bring about states that maximise utility
$$u:E\rightarrow\mathrm{R}$$
##### Local utility functions


#### Expected utitility
The probability that run `r` occurs when agent `Ag` is placed in environment `Env` $$P(r|Ag,Env)$$
can be computed from the probability of each step
![](../img/Pasted%20image%2020250204174153.png)

Expected utility `EU` of agent `Ag` in environment `Env` (`P`, `u`)
$$EU(Ag,Env)=\sum_{r\in R(Ag,Env)}u(r)P(r|Ag,Env)$$

#### Optimal agents
![](../img/Pasted%20image%2020250204173645.png)

#### Predicate Task Spacifications
A special case of assigning utilities to histories is to assign 0 or 1 to a run, denote $\Psi$
![](../img/Pasted%20image%2020250210171204.png)

#### Task environments
$$<Env, \Psi>$$
- The properties of the system the agent will inhabit
- The criteria by which an agent will be judged to have either failed or succeeded in its task

A set of all runs of the agent in an environment that satisfy $\Psi$
$$R_\Psi(Ag,Env)=\{r|r\in R(Ag,Env)\space and\space\Psi(r)=1\}$$

An agnet `Ag` succeeds in task environment $<Env,\Psi>$ if
$$R_\Psi(Ag,Env)=R(Ag,Env)$$
- $\forall r\in R(Ag,Env)$, we have $\Psi(r)=1$
	- if the agent fails on a single run, we say it has failed overall
- $\exists r\in R(Ag,Env)$, we have $\Psi(r)=1$
	- which counts an agent as successful as soon as it completes a single successful run

#### The probability of Success
If the environment is non-deterministic, the $\tau$ returns a set of possible states
- Let $P(r|Ag,Env)$ denote probability that run `r` occurs if agent `Ag` is placed in environment `Env`
![](../img/Pasted%20image%2020250211003408.png)

#### Achivement and Maintenance Task
The idea of a predicate task
- *achievement tasks*: achive state of affairs $\varphi$. Specified by aset `G` of "good" or "goal" states $G\subseteq E$
	- The agent succeeds if it is **guaranteed to bring out** at least one of these states
	- The agent succeeds in an achivement task if it can **force the environment** into one of the goal states $g\in G$
- *maintanance goal*: maintain state of affairs $\varPsi$. Specified by a set `B` of "bad" states $B \subseteq E$
	- The agent succeeds in a particular environment if it manages to **avoid** all states in `B` -- if it never performs actionswhich result in any state in `B` occurring
	- In terms of games, the agent succeeds in a maintenance task if it ensures that it is **never forced into** one of the fail states $b\in B$

## Deductive Reasoning Agents
### Symbolic Reasoning Agents
Agents make decisions about what to do via *symbol manipulation*
- knowledge-based system
- bring all the associated methodologies of such systems to bear

To use logic to encode a theory stating the best action to perform in any given situation
- $\color{#b293f6}\Delta$ be a logical database that describes the current internal state of an agent
	- *first-order predicate logic*
- $\color{#b293f6}\rho$ be the theory (tylically a set of deduction rules)
- $\color{#b293f6}Ac$ be the set of actions the agent can perform
- $\color{#b293f6}\Delta\vdash_\rho\varphi$ means that $\color{#b293f6}\varphi$ can be proved from $\color{#b293f6}\Delta$ using $\color{#b293f6}\rho$

*Perception function*
$$see:E\rightarrow Per$$

The *next state function* revises the database $\Delta$
$$next:\Delta\times Per\rightarrow\Delta$$

*Action Function*: The agent's action is determined by its deduction rules and current database.
![](../img/Pasted%20image%2020250211010545.png)

decision-making: *deduction*
The agent's decision-making strategy: *logical theroy*
The process of selecting an action reduces to *a problem of proof

#### Agent0 programming language
- A set of *capabilities*: things the agent can do
- A set of *initial beliefs*
- A set of *initial commitments*: things the agent will do
- A set of *commitment rules*
	- a *message condition*
	- a *mental condition*
	- an *action*
An AGENT0 program consists two parts: **initialisation** and **commitment rules**

Decision cycle:
1. To determine condition is matched against the messages the agent has recieved
	- The *message condition* <==> the *messages* the agent has recieved
	- The *mental condition* <==> the *beliefs* of the agent
2. Actions may be 
	- *Private*: internally executed computation
	- *Communicative*: sending messages

Messages constrained:
- **Requests** to commit to actions
- **Unrequests** to refrain from actions
- **Informs**, which pass on information

#### PLACA
Agent's mental states are expanded to include *plans* and *intentions*
The inability of agents to plan, and communicate requests for action via high-level goals

### Practical Reasoning
Reasoning directed towards *actions*, 
- Theoretical resoning: *beliefs*

*Deliberation*
Deciding **what** state of affairs we want to achieve, outputs *intentions*
- *intensions*: the interplay between *beliefs* and *desires*, defines how the model works

*Means-ends reasoning*
Deciding **how** to achieve these states of affairs, outputs *plans*

#### Intensions in Practical Reasoning
Intentions are stronger thatn desire
![](../img/Pasted%20image%2020250219221357.png)
![](../img/Pasted%20image%2020250219221429.png)
![](../img/Pasted%20image%2020250219221501.png)
![](../img/Pasted%20image%2020250219222144.png)

#### Means-ends Reasoning / Planning
The design of a course of action that will achieve some desired goal
Basic ideas to give a planning system, use **logic** to represent:
- goal/intension to achieve
- actions it can perform, each has
	- A *name*, which may have arguments
	- A *pre-condition list*: a list of facts which **must be true** for the action to be executed
	- A *delete list*: a list of facts that are no **longer true** after the action is performed
	- An *add list*: a list of facts made true by executing the action
- the environment: *ontology*
Generate a *plan* to achieve the goal, a sequence of steps (actions)
![](../img/Pasted%20image%2020250220001433.png)
The *goal* is represented as a set of formulate

#### Formal Respresentation
#### Option Generation and Filtering

#### Degrees of Commitment
*Blind commitment*: 
- maintain an intention until it belives that the intention has actually been **achieved**, *fanatical commitment*
*Single-minded commitment*: maintain an intention until it beleves that **either** the intension has been achieved, **or** else that it is no longer possible to achieve the intention.
*Open-minded commitment*: maintain an intension **as long as it is still believed possible**

Commitment to:
- *Ends*: the state of affairs it **wiches to bring about**
- *Means*: **the mechanism** via which the agent wishes to achieve the state of affairs

#### Intention Reconsideration
![](../img/Pasted%20image%2020250514011035.png)

## Reactive and Hybrid Agents
### General Control Architecture
![](../img/Pasted%20image%2020250513223252.png)
- *Perceives* the environment
- *Revises* its internal state, identifying beliefs and desires
- *Selects* actions from its intention and plan
- *Acts*: possibly changing the environment

![](../img/Pasted%20image%2020250217172742.png)

### Behaviours
![](../img/Pasted%20image%2020250217172938.png)
- Behavioural chunks of controls each connecting sensors to actuators
- Implicitly parallel
- Particularly well suited to Autonomous Robots
- each layer is independent, each can independently be coded/tested and assemble into a complete system

#### Emergent Behaviour
### Hybrid Architectures
classical and alternative approaches, to build two or more subsystems:
- A *deliberative* one, containing a *symbolic world model*, which develops plans and makes decisions in the way proposed by symbolic AI
- A *reactive* one, which can **react to events** without complex reasoning

- *Horizontal layering*: layers are each directly connected to the sensory input and action output, each layer acts like an agent
- *Vertical layering*: sensory input and action output are each dealt with by at most one layer each

#### TouringMachines (Ferguson)
Consists *perception* and *action subsystems*, interface directly with the agent's environment 

Three control layers, embedded in a control framework **horizontally**
- *Reactive layer*: situation-action rules, can only make references to the agent's current state
- *Planning layer*: achieves the agent's procative behaviour
- *Modelling layer*: symbolic representations of the 'cognitive state' of other entities in the agent's environment

#### InterRRaP
![](../img/Pasted%20image%2020250513165227.png)
Bottom-up activation
Top-down execution

- Behaviour layer
- Plan layer
- Cooperation layer

## Ontologies & Communication
"Social" ability
- Most work on multi-agent systems assumes communication
- Ontologies: language for understanding

Speech Acts
- Representatives
- Directives
- Commisives
- Expressives
- Declarations

- Performative verb
- Propositional content

### ACLs
Agent Communication Languages
- *KQML*: Knowledge Query and Manipulation Language, Message itself
- *KIF*: Knowledge Interchange Format, **the body of the message**

#### KQML
Defines various acceptable 'communicative verbs' or *performatives*
Each KQML message has a performative and a numberr of parameters
![](../img/Pasted%20image%2020250221192416.png)

#### KIF
A language for expressing **message content** or **domain knowledge**, can be used to writing down *ontologies* and based on first-order logic
- properties of things in a domain
- repationships between things in a domain
- general properties of a domain

### Ontologies
Agents need to **agree on the words** they use to describe a domain
Types of objects:
- *Classes*: collections of things with semilar properties
- *Instances*: specific examples of classes
- *Relations*: describe the properties of objects and connect then together

Different levels of detail: the more specific an ontology, the less reusable it is
- *Upper ontology*: contains the **most general information** about the world
- *Domain ontology*: defines concepts appropriate for a **spacific application domain**
- *Application ontology*: defines concepts used by a specific application

### Cooperative DIstributed Problem Solving
#### Coherence and Coordination
#### Task Sharing and Result Sharing
#### Problem Decomposition
The overall probelm is divided into smaller sub-problems

*Sub-problem Solution*

##### Task Sharing & the Contract Net
Recognition
Announcement
Bidding
Awarding & Ecpediting

##### How to bid

#### Result Sharing
Black board Systems
Subscribe/Notify Pattern

##### Handling Inconsistency

#### Coordination
Coordination is managing inter-dependencies between the activities of agents
- positive coordination may be requested (explicit) or non-requested(implicit)

Decide what to do
make sure their work is coordinated


## Utilities and Preferences
### Multi-Agent Systems
#### Dominant Strategies




option: generate a set of possible alternatives (desires)

filters: chooses between alternatives, commits to achieve them

condorcet paradox: no matter which outcome we choose, a majority of volters will be unhappy with the chosen outcome.

rebuttal: conclusion or premises of one argument contradict with that of another argument

undercut: .... contradicts a proposition within the support of the another argument

Sheply: agent i's average amount that is expected to contribute to a coalition

delibration: what state want to achieve 
means-ends: how to achieve these states of affairs

core
- efficiency: sum of distributed value equal to total value
- individual rationality: each distributed value not lower than its payoff of single action