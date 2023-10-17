# 09/25/2023
- complexity: simply defined by numbers of code lines
- requirements
- good software engineering habit
	- mot making the same mistakes again
	- spend a lot of time on testing
	- predict their own productivity
- **Software process**
	- Specification: what the system should do
	- Development:
	- Validation
	- Evolution
- **Good Software**
	- Maintanability: 自动翻译API参与网页
	- Dependability
	- Efficiency
	- Usability
- **Ethical Responsibility**
	- The software engineer must behave in an hosest and ethically responsible way
	- Confidentiality
	- Competence
	- Intellictual property rights
	- Computer misuse
	- Some Ethical problems: robots and AI, who is responsible.

# 09/26/2023
- **process**: a series of activity
#### Waterfall Model
- bridge building
- complete is complete
- difficulty get back to fix the problem
- Inflexible partitioning
- difficult to respond to changeing customer requirements
- only appropriate when the final requirements are well-understood (rare)

#### Evelutionary Development
- Outline sescription, could be very detailed
- specification and development and validation are interleaved
![[Pasted image 20230926152931.png]]
- lack of proess visibility, we dont know how many time it needs.

#### Agile
- lightweight approach to software development
TODO: learn about

#### Scrum
- the development sand delivery is broken down into increments (sprints)
- the customer requirements is prioritised
- once the develoment of an increment is started, the requirements are frozen.
##### Incremental Development
- Lower risk of overall project failure
- early increments act as a prototype to help elicit requirements for later increments

# 09/28/2023
- Software Specification: The process of establishing what services are required and the constraints on the system's operation and develepment
- **Software design and implementation**: The process of convrting the system specification into an executable system
	- Software design
	- Implementation

#### Requirements
![[Pasted image 20230928102650.png]]
- Design Activities
	- Atchitecturual design(deparate web service modules)
	- abstract specification
	- interface design -- unambiguous
	- component design -- services are allocated to components and interfaces
	- data structure design
	- algorithm design
- models
	- dataflow
	- entity relation attribute
	- structural
	- state transition modes showing system states and triggers
- coding style document
- write small piece of code and determines it, repeat

#### Testing
![[Pasted image 20230928102845.png]]
- sub-system testing
	- integrate modules into sub-system
	- organised as package or JAR library

# 10/02/2023
- Requirements: ensure a software solution correctly coves a particular problem, it may range from a high-level abstract statement or a system constraint to a detailed methematical finctional specification
	- User requirements: natural language, the services of the system provides and its operational constrains, for customers
	- System requirements: details descriptions of the system services.
	- Software requirements: description of the system on designing and implementation
	- Functional requirements: statements of services the system should provide, what should it react and behave in particular situations.
	- Non-functional requirements: process, standars, timing constrains, system properties and constraints, 
		- Organisation: consequence of organisational policies and procedures
		- External requirements: external the system
	- Domain requirements: from application domain of the system, reflect characteristics of the domain.
- Problem arise when requirements are not precisely stated.
- Goas of requirements: 
	- A general intention of the user such as ease of use. are helpfu t developers as they convey the intentions of the system users.
- Conflicts between different non-functional requirements are common in complex systems

# 10/03/2023
- Use cases: Is a task which the actor needs to perform with the help of the system
- Use: how to use the system
- Case: an example
- Use case diagram, an actor is a user of the system, acting in a particular role
- The actor can be human or non-human
- A big rectangle represents a system, all use-cases inside and actors outside, linking the use-cases
- *Inheritance* can be used between actors
- *Include relations*: use `<<includes>>` arrow to point including use-case
- *Extends*: `<<extents>>` arrow, if a use-case has more significantly different outcomes, to re-use the use-case
- don’t describe the internal behaviour; must describe behaviour with external actors

# 10/09/2023
- requirements elicitation: end-users
	- Application domain, services that the system should provide and operational constraints
	- Previous system gathering system
	- Different stakeholders may have conflicting requirements (viewpoints)
	- Organizational and political factors(data protection)
	- Closed/open interview
	- Ethnography: how people actually work, combining prototyping as *Focused ethnography*
		- Project/code management
	- security requirements: 
		- Confidentiality
		- Integrity
		- Authentication and Authorization
		- Non-repudiation
- requirements analysis: classify, priorities and negotiate
- requirements validation: does the system do what the users require
- requirements management: changes to requirements document
- Feasibility study decides whether the proposes system is worthwhile

# 10/10/2023
- Confidentiality requirementg
	- Encryption & Permissions
	- In storage; wire and wireless link
- Integrity requirements
	- HASH + secret key checking(key distribution)
	- HASH asymmetric cipher
- Authentication and Authorization
	- Authentication: who are you
	- Authorization: what are you allowed to do
	- Username, password, hardware(cards, token……), biometrics
	- Is often first point of attack
- security, logs and alerts
	- Login/logouts, database access request
	- Failed action
	- Unusual activity (strategy like high volume transitions)
- Bell-LaPadula model: no read-up; no write-down
	1. Top secret
	2. Secret
	3. Sensitive
	4. Unclassified
- specifying: documents of protocol and method
- checking
	- Validity
	- Consistency
	- Completeness
	- Realism
	- Verifiability

# 10/12/2023
### System Models
- abstract description of systems whose requirements are bending analysed
	- behavioral modeling
	- data modeling
	- object modeling (Unified Modeling Language UML)
- *External perspective*: system’s contest or environment
- *Behavioural perspective*: behaviour of the system
- *Structural perspective*: the system or data architecture
- not including non-functional requirements
- too detailed which difficult for **users** to understand
- model types
	- data processing model
	- composition model
	- architectural model
	- classification model
	- stimulus/response model
- *context models*: illustrate the boundaries of a system, not always straight forward, affect by social and organisational concerns.
	- architectural model, relationship with other system
- *Process Model*: the overall process and the process that are supported by the system, a flow of actions
- *Behavioural models*: describe the overallll behaviour of a system
	- *data processing models*: system’s data processing \*
		- show end-to-end processing of data
	- *state machine models*
- *Data Flow Diagrams*: track and document how the data associated with a process is helpful to develop an overall understanding of the system, showing the data exchange between systems in its environment, usually a top-down process. \*
- *Statechart Diagrams*: the behaviour of the system in response to external and internal events, system sates as nodes and events are arcs, system moves towards next state when an event occours
	- also model sub-models
	- guard: a little pre-condition, used to unsure that the system only moves from one state to other if the expression is satisfied
- use multiple state chars to keep the design simple
- *Finite State Machines, FSM*: the behaviour of a system or complex object, with a limited number of defined conditions or models, mode transitions change with circumstance
	- a set of stated
	- a initial state
	- an input alphabet
	- a transition function that maps input symbols and current states to a next state

# 10/11/2023
- nested list: `f xxs [ [ x | x <- xs, even x ] | xs <- xxs]`

#### Recursive
- Recursive: a function calls the function it self
	- A base case
	- One or more rules moves the program closer to the base case
```haskell
factorial n = 
	if n > 1
	then n * factorial (n-1)
	else 1
```
- *Pattern matching*: Haskell will processes from top to bottom
```haskell
factorial 1 = 1
factorial n = n * factorial (n-1)
```
- each recursive rule makes progress towards the base case, otherwise, it will never terminate
- Every recursive function must have a base case, it will never terminate if no base case
```haskell
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n—2)
```
- multiple recursive rules: comprehensive
```haskell
even_sum 0 = 0
even_sum x = 
	if x `mod` 2 == 0
	then x + even_sum (x - 1)
	else even_sum (x - 1)
```
*Guards*: `| <test> = <expression>` which \<test> evaluates True or False; \<expression>can be anything. Good alternative to a load of nested ifs.
```haskell
even_sum x
	| (x == 0) = 0
	| (x `mod` 2 == 0) = x + even_sum (x—1)
	| otherwise = even_sum (x-1)
```

# 10/12/2023
### Recursion on lists
```haskell
sum’ (x:xs) = x + sum’ xs

length’ (_:xs) = 1 + length’ xs

square_list [] = []
square_list (x:xs) = x*x : square_list xs

take’ 0 list = []
take’ n [] = []
take’ n (x:xs) = x : take’ (n-1) xs

elem’ e [] = False
elem’ e (x:xs)
	| e == x =True
	| otherwise = elem’ e xs

maximum’ [] = error “Called with empty list”
maximum’ [x] = x
maximum’ (x:xs) = 
	let
		max_tail = maximum’ xs
	in
		if (x > maxtail) then x else max_tail

add_adjacent [] = []
add_adjacent [x] = error “Odd number of elements”
add_adjacent (x:y:xs) = x + y :add:adjacent xs

group n [] = []
group n list = 
	let
		first = take n list
		rest = drop n list
	in
		first : group n rest
```

# 10/13/2023
- `where`: bind names across a whole function.
```haskell
remove_twos [] = []
remove_twos (x:xs)
	| x == 2 = rest
	| otherwise x : rest
	where rest = remove_twos xs
```
```haskell
initials first last = [f] ++ “. “ ++ [l] ++ “.”
	where (f:_) = first
		  (l:_) = last
```
#### multiple lists recursion
```haskell
add_lists _ [] = []
add_lists [] _ = []
add_lists (x:xs) (y:ys) = x+y : add_lists xs yes

gt_10 [] = ([], [])
gt_10 (x:xs)
	| x > 10 = (x:gt, lt)
	| otherwise = (gt, x:lt)
	where (gt, lt) = gt_10 xs
```
`zip`: takes two lists and returns a list of pairs, shorter one determines the length
#### mutual recursion
```
events [] = []
events (x:xs) = x : odds xs

odds [] = []
odds (x:xs) = events xs
```
#### multiple recursion
```haskell
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)

fast_fib_help 1 = [1, 0]
fast_fib_help n = x + y : (x:y:xs)
	where (x:y:xs) = fast_fib_help (n-1)

> fast_fib n = head (fast_fifb_help n)
```
#### quick sort
```haskell
qs’ [] = []
qs’ (x:xs) = qs’ lower ++ [x] ++ qs’ upper
	where lower = [e | e <- xs, e < x]
		  upper = [e | e <- xs, e >= x]
```