### E-Commerce
Hosting online stores and managing transactions, refers to the buying and selling of goods and services over the internet
- Goods: physical products
- Services: things like digital streaming and online banking

### User mode & Kernel mode
![](../img/Pasted%20image%2020250206211854.png)

### Hypervisors
- Directly on the host's hardware, bare-mental
	- High performance and efficiency
	- Hyper-v
- Run on a host operating system
	- VMware workstation

- Efficiency
- Cost savings
- Flexibility
- Isolation

## Webpage

### Dom
Document Object Model is a programming interface for web documents, represents the structure of a document and allows programs to manipulate the document's structure, styles and content

Represents a document as a tree of objects, HTML tags become nodes in the tree, and can be manipulated by JavaScript

*Attributes*
- class
- id
- style
### Taiwind CSS
A utility-first CSS framework, it proveides low-level utility classes that let you build completely custom designs without ever leaving your HTML.

### JavaScript
![](../img/Pasted%20image%2020250206212857.png)
- Block scope: if, for...

False values: false, 0, -0, 0n, "", null, undefined, NaN

Double equals: 1 == "1" is true
Triple equals: 1 === "1" is false, does not perform **type coercion**

null and undefined: both falsy
- null: no value or no object
- undefined: a variable has been decared but no value has been assigned to it

*Object*
```JavaScript
let student = {name: "John", age: 20, grade: "A"}
let name = student.name //John
student.major = "CS"

// destructuring
const {name, age, major} = student
```
Functions are objects too

*Spread operator*: allows an iterable (array or string) to be expanded in places where zero or more argumetns or elements are expected
```JavaScript
const arr1 = [1, 2, 3]
const arr2 = [...arr1, 4, 5]
```

*prototype chains*
```JavaScript
let animal = {
	eats: true
}
let fish = {
	swim: true
	__proto__: animal
}
let rabbit = Object.create(animal)
rabbit.jump = true
```

*For-in loop*
```JavaScript
for (let eachItem in iterator){
	...
}
```

*Function* and *Rest parameters*
```JavaScript
const greet2 = function(...name){
	...
}
const greet3 = (...name) => {
	...
}
```
allows a function to accept any number of arguments as an array

*Classes*
```JS
class Model extends Car{
	constructor(brand, mod){
		super(brand);
		this.model = mod;
	}
}
let myModel = new Model("A", "B")
```

Serealizing JavaScript Objects to JSON

## Docker
`--rm` flag, automatically remove when exit