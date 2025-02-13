## Intro
### E-Commerce
Hosting online stores and managing transactions, refers to the buying and selling of goods and services over the internet
- Goods: physical products
- Services: things like digital streaming and online banking

### User mode & Kernel mode
![](../img/Pasted%20image%2020250206211854.png)

### Virtural machines: Hypervisors
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


## Security
Absolute security in computing systems is unattainable
*vulnerabilities*: software and hardware flaws and human error
*Patch cycle* involves discovering a nulnerability, preparing and publishing a patch, and users installing the patch
*Zero-day* for which no patch is available, can be exploited in potent attacks, even against systems that are up-to-date with all vendor patches.

### Host Defence
The *Principle of Least Privilege (PoLP)*: reducing the impact of zero-days attacks
- user should be given the minimum levels of access necessary to complete her job functions. It can help to minimise the damage if an account is compromised, as the attacker sould have limited access
- user rights, network connections, data access...

Operating systems typically have **two primary levels of authorisation**:
- ordinary users (non-root)
- system administrator (root)

*Sandboxing* involves running programs within cantexts called sandboxes that limit their capabilities
- Security-Enhanced Linux (SELinux)
- can be attacked, can be escaped from

*Mandatory Access Control (MAC)* is a type of access control in which the operating system constrains the ability of a subject or initiator to access or generally perform some sort of operation on an object or target
- user do not have much control over the access control of their files
- only the administrator sets the policy of who can access which file.

*Discretionary Access Control (DAC)*: a program runs with the permissions of the user executing it

### SELinux
A security framework implemented in the linux kernel and provides MAC
Operate three modes: *enforcing*, *permissive* and *disabled*
- *Enforcing mode*: SELinux policies are enforced and access violations are logged
- *Permissive mode*: SELinux policies are not enforces, but access violations are logged
- *Disable mode*: SELinux is disabled and no access violates are logged

SELinux is a *labelling* system, every 
- process
- file
- directory object
- network ports
- devices
- potentially host names
in the operating system has a label

Rules are written to control the access of a process label to an object label, known as *policy*

## Containers and Encapsulation
Containers are designed to encapsulate an application and its dependencies and sit on top of the kernel of a host operating system

![](../img/Pasted%20image%2020250213221126.png)

![](../img/Pasted%20image%2020250213221247.png)

### Docker
containers are created from *images*, which are specified with *Dockerfiles*

**Pull and run**
```sh
docker pull ubuntu:latest
docker run -it ubuntu:latest /bin/bash
```

*Dockerfile*
```Dockerfile
FROM ubuntu:latest
RUN echo "echo Hello, world!" > /hello-world.sh
RUN chmod +x /hello-world.sh

# the command to run when the container starts
CMD ["/hello-world.sh"]
```
Dockerfile Elements:
- *Base image*: Specifies another image upon which the new image is being built
- *Intructions*: Define the steps to build the image: installing dependencies, copying files, configuring environment.
- *Commands*: Execute commands within the image during the build process
- *Exposed ports*: Speciry which ports should be exposed when running a container from the image
- *Entrypoint*: Define the command that should be executed when a container is started from the image

**Built and run**
```sh
# -t option used to specify a name and optionally tag in the 'name:tag' format for the image
docker build -t hello-world .

docker run hello-world
```

*Image layers*
Docker images are made up of **read-only layers**
Each **instructions of Dockerfile** will create a new layer
Each layer specifies a set of differences from the layer before it.
The layers are stacked on top of each other to form a base for a container's file system

*Container layer*
A container runtime will create a **writable layer** above *image layers*
Container private layer

![](../img/Pasted%20image%2020250213223416.png)

### Linux Kernel
A container is just a collection of processes that are running on the host OS, They are isolated from other processes on the host OS with helps from the Linux Kernel
- isolation, resource management and file system abstraction

#### Namespaces
Isolate system resources for a collection of processes, each set of processes sees its own isolated instance of a global resource
- *PID*: process ID number space
- *NET*: network namespaces virtualised the network stack
- *MNT*: manages mount points (file systems)
- *UTS* (UNIX time sharing): Isolates host name and domain name
- *IPC*: Isolates inter-process communication
- *USER*: Provides both privilege isolation and user identification segregation

#### Control Groups (cgroups)
Manage **resource allocation** for containers
Limit and monitor the amount of resources (CPU, memory, disk I/O) that container can use, which ensures that no single container can monopolise system resources and impact other containers

#### Union File Systems
Container Orchestration: provide a **layered file system**, allow containers to share a read-only base file system, while maintaining separate writable layers for each container