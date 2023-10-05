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