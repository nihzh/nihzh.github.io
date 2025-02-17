### HPC programming
- Minimise time to solution (finest dataset)
- Maximize throughput (infinite dataset)
- Ability to solve problems cinsidered too big for available memory
- Maximise resource utilisation - CPU/memory/network/accelerator(GPU)/energy

*Parallelism*: Two or more processes that exicute simultaneously and independently

*Theoretical performance*
![](../img/Pasted%20image%2020250203230408.png)

![](../img/Pasted%20image%2020250130212627.png)

#### Arithmetic Intensity
![](../img/Pasted%20image%2020250203231025.png)
- W is the number of flops carried out by the program
- Q is the number os bytes of bytes transferred frm memory to cache
*upper bound*
- hier AI: memery bound
- lower AI: compute bound

#### Roofline model
![](../img/Pasted%20image%2020250204000051.png)
Horizontal bound: maximum capacity of the processor ($R_{peak}$ and $R_{max}$)
Relates processor performance to **off-chip** memory traffic

#### Von Neumann Architecture
![](../img/Pasted%20image%2020250203231854.png
instructions and data must transport through a same bus
*Pipelining*: Instruction-level parallelism

*Spatial locality*: If a memory location is accessed, it is very likely that its neighbours will be accessed soon
*Temporal locality*: If a variable (memory location) is accessed, it is very likely to be needed again soon.

Possible reasons for sub-optimal pperformance across multiple cores:
- Cache Contention
- Memory Contention
- Interconnect Traffic
- Load balancing

Compilers
- GNU (gcc)
- Intel (icc)
- Portland (pgcc)
- NVIDIA (nvcc)

Plan the program to be parallel

### Compilers
- time optimisations
- space optimisations

#### Memory read/writes
- Row major -- normally used
- Column major

#### Common compilers optimisations
- replace function calls with "inline" code
	- may not do it when containing a loop, static variables and recursive
- dead store\code elimination
- *code hoisting*
	- for loop-variand computations inside a loop
	- move to the incariant computation outside of the loop
- *common sub-expression elimination*: same sub-expression appears multiple times
- *loop unrolling*:
	- replace loop with repeated statements
	- replace momory load/stores and counter increments with constant values

*Vectorisation*
![](../img/Pasted%20image%2020250205174401.png)

***Time space trade-off***

### Profiling
when a function in **different file** with calling function, the inline will not be implements
*inline* keywork with function declaration to force inline
![](../img/Pasted%20image%2020250205174614.png)

![](../img/Pasted%20image%2020250205174712.png)

### Parallelism
Split by color (type)
Split by area
- each individual only has to travel in a local area
- could have **load imbalance**
Split by number
- workload is balanced between individuals
- Time is taken sequantially numbering the balls

#### Design for parallel performance
Find best possible solution for a given problem, and objective on a given system

> There is a maximim possible performance for a given cimbination of system and problem to be solved. Choices made during design and implementation will lead **Either to the system meeting this maximim, or cause proformance being below expectation**

For a given system, there is no universal best solution for all problems
- ensuring some **performance portability** for your parallelised application whichever system it is run on.

![](../img/Pasted%20image%2020250210231838.png)

#### Decomposition
![](../img/Pasted%20image%2020250210232025.png

##### *Data parallelism*
Given a data set and an operation that can be applied elemet-by-element, Apply the operation cuncurrently to each element

##### *Task parallelism*
Several independent tasks operations to be applied to the same data

##### *Pipelining*
![](../img/Pasted%20image%2020250210232641.png)

*Granularity*
- *Coarse-grained parallelism*: A program is split into large tasks to be executed in parallel
	- ok for data parallelism as all threads execute the same instructions, load imbalance reduced
- *Fine-grained parallelism*: A program is split into small tasks to be executed in parallel
	- Fine with data parallelism, no load imbalance
	- Good for task parallelism/pipelining, allows the program to be split into tasks to reduce load imbalance and increase throughput

##### *Mixed Solution*
**Real problems often have ximed solutions**: combinations of the ideas above
No fixed rule.
Test - change - test again for the best configuration of threads and tasks

### Scalability and Speedup
*Speedup*: ratio of the time it takes to urn a program without parallelism versus teh time it runs in parallel
*Scalability*: a measure of how much speedup the program gets as one adds more processors/cores

A program's performance stops scaling when adding more resources no longer results in additional speedup
![](../img/Pasted%20image%2020250212171150.png)

*Strong scaling*
- problem sizefixed
- measure the fastest time for a given problem
- Ideal: linear reduction in runtime
- report time to solution for different number of nodes/cores
*Weak scaling*
- increase problem size with cores/nodes
- measure how time to solution changes with probelm size but increasing compute resources at the same time
- Ideal Constant runtime
- report time to solution

#### Amdahl's Law
A computer program will never go faster than the sum of the prots that do not run in parallel (the serial protions of the program), no matter how many processing elements we have
![](../img/Pasted%20image%2020250212171851.png)
Strong scaling
Practical Parallelism
- Presumes time spend in serial protion remains constant
- May not constant

#### Gustafson's Law
allowing the probelm size to increase as we add more cores/processors, to solve a larger problem in the same time
$$Speedup = \alpha+p(1-\alpha)=p-\alpha(p-1)$$
Weak scaling

### Domain Decomposition
Equaly splitting data to each core should mean no load imbalance

A *stencil* is an array operation where each element of the output array depends on a small neighourhood of elements from the input array, a kind of *Gather Operation*

*Shared memory*: threads can see each other's memory
halo exchange: explicitly send each other values when in a distributed memory content where these parts live on different nodes.

It is not always about minimising time-to-solution
一点点时间缩减有时可能带来成倍的资源消耗