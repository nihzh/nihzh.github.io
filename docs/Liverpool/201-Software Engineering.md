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