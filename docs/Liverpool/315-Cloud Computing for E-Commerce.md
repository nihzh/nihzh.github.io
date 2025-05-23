## Intro
### E-Commerce
Hosting online stores and managing transactions, refers to the buying and selling of goods and services over the internet
- Goods: physical products
- Services: things like digital streaming and online banking

### User mode & Kernel mode
![](../img/Pasted%20image%2020250206211854.png)

Kernel Space: where the kernel runs
- code running access to the hardware
- run in protected memory area

User Space: where user applications runs
- processes have limited access to the harware and must communicate with the kernel for resource access

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

Falsy values: false, 0, -0, 0n, "", null, undefined, NaN

Double equals: 1 == "1" is true
Triple equals: 1 === "1" is false, does not perform **type coercion**

null and undefined: both falsy
- null: no value or no object 无对象
- undefined: a variable has been decared but no value has been assigned to it 对象未初始化

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

*Multi-category Security - MCS*: multiple processes with same type
*Multi Level Security - MLS*: controlling processes based on the data level they will be using

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

#### Orchestration Software
Kubernetes: automate the deployment, scaling, and operation of containers It runs on data centre servers and abstracts away the complexity of the underlying hardware to provide a simple interface for running containers.

Pods ==> Deployment

YAML manifest

## Networking


## Ansible
*Configuration as code (CaC)*
Designed for **configuration management**, it helps manage multiple machines by organizing them to an *inventory*, which can be sourced dynamically or from cloud prividers

### Agentless architecture
Core principle: *agentless architecture*, no need to installing and set up
- Communication with managed hosts happens over *SSH*
- *Temporary modules* are deployed and run, then removed when tasks complete
- Resources: 
	- Only consumes **resources on the target node** during configuration
	- **No permanent background processes** remain on the node afterward

### Inventory
*Inventory file* (YAML or INI) to define and track host information upon which is expected to operate:
- Static and defined in text files
- Dynamic, pulling host data from external resources such as cloud APIs
- *Groupings*: selecting subsets of machines for specific tasks

*Idempotency*: If the system is already in the desired state, Ansible will not make any changes, allows safely re-run playbooks without worrying about unintended side effects

### Playbooks
To describe more complicated configurations than with the `ansible` command line
- Written in YAML
```
---
- name: Ping all hosts
  hosts: all                   --group of hosts the play applies to
  becomes: yes                 --escalates root privileges
  tasks:
	- name: Install nginx
	  ansible.builtin.yum:     --Ansible modules for action
	    name: nginx
	    state: present
	- name: Start nginx service
	  ansible.builtin.service:
	    name: nginx
	    state: started
	    enabled: yes
	  when: ansible_selinux.status == "enabled"
...
```

#### Running the play book
```sh
ansible-playbook -i hosts.ini ping-playbook.yml --ask-become-pass
```
`-i hosts.ini`: specifies teh infentory file
`-ask-become-pass`: prompts for the sudo password before executing tasks that require sudo privileges

#### Register and Debug
```Playbook
- hosts: web_servers  
  tasks:  
	- name: Run a shell command and register its output  
	  ansible.builtin.shell: /usr/bin/foo  
	  register: foo_result  
	  ignore_errors: false  
	- name: Run a shell command using output of foo  
	  ansible.builtin.shell: /usr/bin/bar  
	  when: foo_result.rc == 5
	  debug:  
		msg: "debug says: {{ foo_result }}"
```

#### Loops
```Playbook
tasks:  
- name: Check connectivity  
	ping:  
	loop: "{{ range(1, 4) | list }}"  
	loop_control:  
		label: "Ping number {{ item }}"
```
- `| list`: filter, converts the range object into a list, making it iterable
- `loop_control`: customozes the loop behaviour
- `item`: the default name of iterator in each round

### Variables
```Playbook
- name : Create New User  
  hosts: all
  vars:  
	username: lisa
  tasks:
	  - name create a user
	    user:
		  name: "{{ username }}"
```

#### Facts
When run a Ansible, it gathers facts about the hosts in the inventory
`ansible -i hosts.ini local -m`

Print Default IPv4 address
```Playbook
---  
- hosts: all  
  tasks:  
	- name: Print IP Address  
	debug:  
	  msg: >  
	  this host uses IP address  
	  {{ ansible_facts.default_ipv4.address }}  
```


## Hosting
*Forward proxy*: intermediary between a client and the internet
- Caching 

*Reverse proxy*: sites between the internet and web servers
- **Load balancing** to distribute traffic across multiple servers
- **Enhancing security** by hiding backend server IP address
- Caching static content to **improve response times**

### Apache
Dockerfile for an Apache HTTP Server
```Dockerfile
FROM httpd:latest
COPY index.html /user/local/apache2/htdocs/
EXPOSE 80
```
- official Apache HTTP Server image
- copy the index file to the container at the default Apache document root

```sh
docker build -t apache-image .
docker run --name apache-container -p 8081:80 apache-image

docker exec -it apache-container /bin/bash
```
Inside the container, Apache's configuration files can be found at `/usr/local/apache2/conf`, with the config file `httpd.conf`

For copy the conf file to the host machine
`docker cp apache-container:/usr/local/apache2/conf/httpd.conf`

Document root
`/usr/local/apache2/htdocs`

#### HTTPS
Self-signed certificated
```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \  
-out selfsigned.crt -keyout private.key \  
-subj "/C=UK/ST=Merseyside/L=Liverpool/O=MyOrg/CN=www.example.com"
```
- `-x509`: specifies that a self signed certificate is to be generated
- `-subj`: sets the subject name field of the new certificate. The subject name field typically contains information about the organisation that owns the certificate

To enable TLS in Apache, Create a custom SSL configuration file `httpd-ssl.conf`
```conf
Listen 443
<VirtualHost *:443>
	SSLEngine on
	SSLCertificateFile "/usr/local/apache2/conf/selfsigned.crt"
	SSLCertificateKeyFile "/usr/local/apache2/conf/private.key"
	DocumentRoot "/usr/local/apache2/htdocs/"
	ServerName www.example.com
</VirtualHost>
```

Dockerfile for HTTPS
```Dockerfile
FROM httpd:2.4  
COPY index.html /usr/local/apache2/htdocs/  
COPY selfsigned.crt /usr/local/apache2/conf/selfsigned.crt  
COPY private.key /usr/local/apache2/conf/private.key  
COPY httpd-ssl.conf /usr/local/apache2/conf/extra/

# Enable SSL module  
RUN sed -i \  
's|#LoadModule ssl_module modules/mod_ssl.so|\  
LoadModule ssl_module modules/mod_ssl.so|'\  
/usr/local/apache2/conf/httpd.conf && \  
sed -i \  
's|#LoadModule socache_shmcb_module modules/mod_socache_shmcb.so|\  
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so|'\
/usr/local/apache2/conf/httpd.conf

# Include SSL configuration  
RUN echo 'Include conf/extra/httpd-ssl.conf' >> /usr/local/apache2/conf/httpd.conf  
EXPOSE 80 443
```
`sed`: stream editor
- `-i`: in-place, changes the file directly without outputting to terminal
- `'s|old|new|'`: substitute

```sh
docker build -t apache-ssl-image .
docker run --name apache-ssl-container -p 8081:80 -p 8082:443 apache-ssl-image
```
### NGINX
Reverse proxy for the Apache HTTP web server
create a new network on docker
`docker network create web-net`

forward all HTTP requests to `apache-container`
```nginx.conf
http {  
	upstream apache-server {  
			server apache-container:80;  
	}  
	server {  
		listen 80;  
		location / {  
			proxy_pass http://apache-server;  
		}  
	}  
}
```

```dockerfile
# Use the official NGINX image as a base  
FROM nginx:latest  
# Remove the default configuration file  
RUN rm /etc/nginx/conf.d/default.conf  
# Copy the custom configuration file  
COPY nginx.conf /etc/nginx/conf.d/  
# Expose port 80  
EXPOSE 80
```

```sh
docker build -f Nginx.Dockerfile -t nginx-reverse-proxy .

docker run -d --name apache-container --network web-net apache-image
docker run -d --name nginx-proxy --network web-net -p 8083:80 gninx-reberse-proxy
```

## Storage
*Local Server Storage*

*Network Attached Storage (NAS)*

*Storage Area Network (SAN)*: specialiaed computer networks taht store data, consist of multiple disk arrays, network switches and servers.

*Relational Database*

*Non-SQL Databases*: can handle unstructured data: 
- MangoDB stores JSON-like documents
### Graph Databases
Store data in nodes and edges, each can hold any number of attributes
- Nodes: represent entities
- Edges: represent relationships between entites

#### Neo4j
- Neo4j Aura: fully managed cloud service
- Neo4j Desktop: A desktop local application
```sh
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/<passwd>/neo4j
```

```neo4j
# create graph
CREATE (ee:Person {name: 'Emil', from: 'Sweden', kloutScore: 99})

# finding nodes
MATCH (ee:Person) WHERE ee.name = 'Emil' RETURN ee;

# match patterns
MATCH (ee:Person)-[:KNOWS]-(friends)  
WHERE ee.name = 'Emil' RETURN ee, friends
```

## Typescript
Extends JavaScript by adding types
Compiles down to plain JavaScript, run in any JS environment

```typescript
let message:string = 'Hello, world!';
console.log(message)

tsc helloworld.ts
```

Primitive Types
- `any`
- `unknown`: compare but not calculate
- `null`
- `boolean`: `true`, `false`
- `number`: `1234.56`
- `bigint`: `1234n`
- `symbol`

Everything as Code
- Infrastructure as Code
- Configuration as Code

XaaS -- Anything as a Service: 3 levels of access ot the cloud
- infrastructure as a service: IaaS
- platform as a service: PaaS
- software as a service: SaaS

What an object can do

## Kubernetes
clusters made up of nodes (physical or virtual), run containerised applications
- Control plane nodes: managing the cluster, must Linux
	- API server: restful over https
	- cluster store: key-value
	- scheduler: watches API server and selects nodes to run
	- controllers: deployment, statefulset, replicaset
	- controller manager
- Worker nodes: run the containers, Linux or Windows
	- kubelet
	- kube proxy
	- container runtimes

## React

Components
return *JSX elements*
```React
--- ButtonComponent.jsx ---
const ButtonComponent = ({ label }) => {
	alert ('You clicked on ${label}!') ;
	...
};
export default ButtonComponent;

--- App.jsx ---
import ButtonComponent form './ButtonComponent'
function App() {
	return (
	...
	<ButtonComponent label="About" />
	...
);}
export default App;

```

Props
passing data from parent to child components
- read-only
- when changed, re-render with the new value

Hooks
- useState
- useEffect: 接收argument, 执行side effect

## Next.js
Compared to React, Next.js significantly improve:
- initial page load performance
- search engine optimisation (SEO)
- user experience on slower divices or networks

choices of rendering in *React*
- client side rendering (CSR)
	- con: the browser has to download the entire JS bundle
	- pro: fast for small re-renders of pages
- server side rendering (SSR)
	- pro: fast for initial loading of pages
	- con: slower for small re-renders of pages

In Next.js, by default, it performs SSR, generates HTML for each page in advance and associated with a small amout of JS code, when page is loaded by teh browser, the code runs and makes the page fully interactive
- hydration

App router / Pages router
Routing in the context of web frameworks such as Next.js refers to how  
an application handles a client’s request based on its URL.

### File Conventions
.js, .jsx, .tsx can be used
- layout
- poage
- loading (React suspense boundary)
- not-found (React error boundary)
- error (React error boundary)
- global-error
- route
- template
- default

colocation: only the contents returned by `page.js` or `route.js` are publicly addressable

parallel routes
intercepting routes

### Route Handlers
create API endpoints tha chanbe accessed via HTTP