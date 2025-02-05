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