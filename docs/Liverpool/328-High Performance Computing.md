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

## Parallelism
Split by color (type)
Split by area
- each individual only has to travel in a local area
- could have **load imbalance**
Split by number
- workload is balanced between individuals
- Time is taken sequantially numbering the balls

### Design for parallel performance
Find best possible solution for a given problem, and objective on a given system

> There is a maximim possible performance for a given cimbination of system and problem to be solved. Choices made during design and implementation will lead **Either to the system meeting this maximim, or cause proformance being below expectation**

For a given system, there is no universal best solution for all problems
- ensuring some **performance portability** for your parallelised application whichever system it is run on.

![](../img/Pasted%20image%2020250210231838.png)

### Decomposition
![](../img/Pasted%20image%2020250210232025.png

#### Data parallelism
Given a data set and an operation that can be applied elemet-by-element, Apply the operation cuncurrently to each element

#### Task parallelism
Several independent tasks operations to be applied to the same data

#### Pipelining
![](../img/Pasted%20image%2020250210232641.png)

*Granularity*
- *Coarse-grained parallelism*: A program is split into large tasks to be executed in parallel
	- ok for data parallelism as all threads execute the same instructions, load imbalance reduced
- *Fine-grained parallelism*: A program is split into small tasks to be executed in parallel
	- Fine with data parallelism, no load imbalance
	- Good for task parallelism/pipelining, allows the program to be split into tasks to reduce load imbalance and increase throughput

##### Mixed Solution
**Real problems often have ximed solutions**: combinations of the ideas above
No fixed rule.
Test - change - test again for the best configuration of threads and tasks

### Scalability and Speedup
*Speedup*: ratio of the time it takes to urn a program without parallelism versus teh time it runs in parallel
*Scalability*: a measure of how much speedup the program gets as one adds more processors/cores

A program's performance stops scaling when adding more resources no longer results in additional speedup
![](../img/Pasted%20image%2020250212171150.png)

*Strong scaling*
- problem size fixed
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

#### Domain Decomposition
Equaly splitting data to each core should mean no load imbalance

A *stencil* is an array operation where each element of the output array depends on a small neighourhood of elements from the input array, a kind of *Gather Operation*

*Shared memory*: threads can see each other's memory
halo exchange: explicitly send each other values when in a distributed memory content where these parts live on different nodes.

It is not always about minimising time-to-solution
一点点时间缩减有时可能带来成倍的资源消耗

### Corrctness
#### Round-off error
有效符号位长度限制带来的精度丢失
Since parallel programs run in a different order everytime, this could result in a different numerical result on every run
- use double precision
- Kahan summation algorithm
- Accept some level of tolerance, define error value that acceptable

*Deadlock*: Occours when two or more tasks wait for each other and each will not resume until some action is taken
*Livelock*: Occurs when the tasks involved in a deadlock take action to resole the original deadlock but in suth a way that there is still/another deadlock, No tasks are able to resumt

#### Race Conditions
Occour when a program's behaviour chages depending on the sequence or timing of events outside the control of the program itself
![](../img/Pasted%20image%2020250217232429.png)

##### Multiple Write Race Conditions
hard to debug

- extra memory: Thread-local copy of the variable, to be accumulated in the end
- extra time: only one thread is allowed access at a time
- use underlying suppourt: the underlying system implements the access control to avoid race conditoins

##### Concurrent access and locks
Acquiring a lock gives a process (or thread) an exclusive access to a shared resources, can be used to unsure correct bahaviour of the multiple-threads programs

*Low-level locks*
- OpenMP: `omp_set_lock()`, `omp_unset_lock`, ...
- Fine-grained control
- Easy to end up with a dead lock

*High-level access control*: OpenMP and MPI
OpenMP critical sections: a code section can be marked as critical
- introduce locks
- `#progma omp critical (name) {code}`
OpenMP atomic: restricted to certain operations
- use sections if no hardware support available
- `#pragma omp critical <single assignment>`

*Reduction operators*
An operator that can take multiple inputs and produce a single result
- **associative** and **commutative**
- Reduce an array to a scalar value, can be done in partial steps, where applying the operator to **part of the array** can generate intermediates that can then be reduced further to get the result.
- sum, product, logical AND, OR, maximum, minimum

### Computation Models
- *Single Instruction, Single Data (SISD)*
![](../img/Pasted%20image%2020250219170844.png)


*Single Instruction, Multiple Data (SIMD)*
- Vectorisation
- Some elemnets of OpenMP
- SIMT (Threats) = SIMD + multithreading
- GPUs
![](../img/Pasted%20image%2020250219170956.png)
- *Multiple Instruction, Single Data (MISD)*
![](../img/Pasted%20image%2020250219171043.png)

- *Multiple Instruction, Multiple Data (MIMD)*


#### Shared memory programming
Used within a single node distributed over **cores**, coores have individual memory though all memory is accessable within the shared-memory
- Limited to addressable memory
- Limited by number of cores
- OpenMP: `#pragma omp parallel for <for-loop>`

#### Distributed Memory Programming
Usually **more than one node**, involves explicit communication between nodes over a network. In each node, shared memory programming
- Limited by the network bandwidth / latency (cost of communication)\
- Not limited by number of cores / nodes
- Use MPI for this: declare the variables that shared, not portable

#### SLURM
Only 40 cores and 1 node available on the node
`sbatch [] script.sh`

**cores**
`SLURM_CPUS_PER_TASK`: `-c <n>` request cpus per task
`SLURM_NTASKS`: `-n <n>` request tasks

**nodes**
`-N <n>`: request nodes

`-p <nodes>`: change the partitions of nodes which submitting to

`htop`: monitor CPU usage
`cat /proc/$SLURM_JOB_ID/status`: check CPU binding

#### Makefiles
```sh
{make command}: {target files}
	{compiler instruction}
```

![](../img/Pasted%20image%2020250219173405.png)

## Lab
```sh
#!/bin/bash -l

# Specify the current working directory as the location for executables/files
# This is the default setting.
#SBATCH -D ./

# Export the current environment to the compute node
# This is the default setting.
#SBATCH --export=ALL

# Specific course queue, exclusive use (for timings), max 1 min wallclock time
#SBATCH -p course
#SBATCH --exclusive
#SBATCH -t 1

# load modules 
module load compilers/intel/2019u5

# just 1 thread to run on
export OMP NUM THREADS=1

# GNU no-opt
# echo GNU no-opt
# icc -O3 quad.c func1.c -lm
# time ./a.out
# echo "-------"

for i in'seq 0 3`; do
	echo Level $i optimisation
	icc -O$i -gopenmp -mkl=sequential matrices-mkl.c -o matricesMKLO$i.out
	time ./matricesMKLO$i.out
done

```

*Slurm*
![](../img/Pasted%20image%2020250218171642.png)
`sbatch -c 16` threads setting

*Compilers OpenMP*
gcc: `-fopenmp` to enable the OpenMP
icc: `-qopenmp` to enable the OpenMP

*MKL: Intel Maths Kernel Library*


# OpenMP
### Process and Thread
*Process*
- Basic unit of work of for the OS
- **Big overheads** in creation/deletion/context switch
- **Isolated from other processes**
- All communication between deifferent processes must be **explicit** -- through a mechanism called *Inter-process Communication*
- Each process has its **own stack and heap**

*Thread*
- Part of a program that can be run independently (simultaneously)
- **Small overheads** in creation/deletion/context switch
- **Share memory with other threads in the same process** 
- Communication can be **implicit** since they share memory -- just change the momory of the other thread (or shared) to communicate
- Threads **share a heap** within a process, while each has its **own stack**
- **Files and other resources** are shared between threads of the same process

## OpenMP
Thread-based parallelism
- shared memory and also accelerations
- parallelisation using work-sharing and tasks

Elements of OpenMP
- Dierectives and their data clauses
- Environment variables
- Runtime functions

### OMP_NUM_THREADS
The maximum number of threads for program to use
- when not specified, program will use as many threads as cores

```sh
cores = ${SLURM_CPUS_PER_TASK : -1}
icc -qopenmp file.c -0 output.exe
export OMP_NUM_THREADS = $cores
./output.exe
```

### Parallel region
```c
// serial code
#pragma omp parallel [...]
{
	// parallel code
	int numThreads = omp_get_num_threads();  
	for(int i = 0; i < numThreads; i++){  
		printf(“Thread %d says Hello”, i); 
	}
}
// serial code
```

#### Replication
All threads will execute the for loop from 0 to maxThreads
- Parallel: threads work independently
- Not parallel: same code is executed

#### omp for
`#pragma omp for`
- must exist inside a parallel region
- can only contain a for loop
- **distributes the iterations** of the for loop **across the threads** of the (existing) parallel region: implicit work sharing
- loop: 
	- must standard loop structure
	- cannot branch

#### omp parallel for
`# pragma omp parallel for`
Create a *parallel region* and *workshare* for loop
- Must only contain a for loop
No race condition: Threads vectorisation
The loop iterations are distributed among threads, ensuring correct parallel execution

*Loop workshare*
Dividing work between threads
All threads execute `iters / numThreads` iterations (by default)
OpenMP orders threads implicitly (by default)

#### Nested for loop
```c
#pragma omp parallel for num_thread(4)
for(int i = 0; i < 2; i++){  
	for(int j = 0; j < 4; j++){  
		//...code to do  
	}  
}
```
Only `i` is distributed between threads, only the omp loop is workshared

#### omp for collapse
```c
#pragma omp parallel for collapse(2) num_thread(4)
for(int i = 0; i < 2; i++){  
	for(int j = 0; j < 4; j++){  
		//...code to do  
	}  
}
```
![](../img/Pasted%20image%2020250224235612.png)
The 2 for loops are **collapsed into 1** and all Iterations are distributed to threads.
- Must have a for loop immediately nested after the first for loop

Collapse is good if: 
- There are uneven iterations as above to **reduce load imbalance**
- Micromanaging memory access to **reduce false sharing**
else: will not see major performance gains and may see slower gains

## Data Clauses
By default
- *Shared*:  A variable that is declared outside of a parallel region is shared between all threads implicitly
- *Private*: A variable that is declared inside a palallel region if private between all threads and is only available to that thread

`shared(x)`: the memory location for `x` is shared to all threads, 
`private(x)`: all threads get allocated a memory location for `x` (own copy)
- no correctness
- useful when only writing
- after the parallel region, `x` will be what it was before enterin the region
`firstprivate(x)`: private, with the original value of `x` upon entry into the parallel region is copied to all threads
`lastprivate(x)`: private, with the value will persist after the end of the parallel region
- only use with *omp for*

`default(none)`
`reduction(op:var)`: do the `op` to the `var` after the parallel region

### Schedule
gain performance in places
`schedule(static, <chunk_size>)`: pre-divide the work into chunks and stick to it, deterministic
`schedule(dycamic)`: when a thread finishes its assigned work, it takes the next availbe chunk, load balance, non-deterministic


`#ifdef_OPENMP ... #endif`: portable , execute only defined (compile) with OpenMP

Runtime functions
`omp_get_wtime()`
`omp_get_num_threads()`
`omp_get_max_threads()`
`omp_get_thread_num()`
`omp_set_num_threads()`

`#pragpa omp parallel if(condition)`: enable or disable parallelism conditionally (one region at a time)
`#pragma omp parallel num_threads(<i>)`: set number of threads for this parallel region

## Barriers
There are implicit barriers at the end of work-sharing constructs and parallel sections
`nowait`: remove the barrier after

`#pragma omp master`: execute the following code block only on the mastter thread (thread#0), has no barriers on entry or exit

*Barriers*
Slow down parallel code by sorcing cynchronisation
- sometimes necessary for correctness
- remove while ensuring correctness
`#pragma omp barrier`: Manually place a varrier at some point in a parallel region, any thread that reaches a point in the code where it says `#pragma omp barrier` must wait until all other threads have reached that point

### First touch (NUMA)
The memory addresses in C pointers are *virtual memory address*
Memory is allocated only then first accessed, or **first touched**

`#pragma omp parallel for schedule(static)`: same thread that initialized array will read it in the later loop


OS schedular moves the thread to a core on the other socket

`OMP_SET_DYNAMIC=false`: disables "reserves the right" optimise system usage
- controlling how many threads are running

`OMP_PROC_BIND=true` (pinning, affinity, placement): bind thread to core (prevent migration of thtreads across cores)

`OMP_PLACES=`: hand-pick which thread lives on which core
- Highly-hardware-specific

### Cache Coherence
A value stored in Core#0's cache, assuming Core#0 was the last to update it, must be know to another Core if they want to modify a variable
- must be maintianed for correctness

### FALSE SHARING
Even though both cores are updating different locations, the design of cache (thanks to cache lines) forces every access to skip the cache and most reads are still from main memory. Which can significantly impact perforamnce of a parallel program due to memory contention

`shecule(static, 4)` (the width of cache line)

By defult, no false sharing: 2 threads for multiple number of iterations

*Padding arrays*: to ensure that all memory is aligned
- add some fake iterations (space of array), round up the iterations to **nearest multiples**
- padding for vectorisatoin: additions in a **clock cycle**
`arr[i * 4]` accessing different cache

### Syncronisation constructs
`#pragma omp single [data clauses]`
has a implicit varrier at the end, is a *work-sharing construct*
- connot be nested

`#pragma omp atomic`: protect single variable
`#pragma omp critical`: protect the entire statement

`#pragma omp simd`: override safety checks, vectorise the for loop


# MPI
Message-Passing Interfaces

```sh
module load mpi/intel-mpi/2019u5/bin
module load compilers/intel/2019u5
mpiicc hello.c
mpirun -np 4 ./a.out
```

*Process*: each instance of the code run as an MPI process, typically with 1 MPI process per physical core ornode

*Communicator*: a collection of processes that can send messages to each other
- `MPI_Init()`, as `MPI_COMM_WORLD`

*Rank*: A numerical ID of a process within a communicator (0, 1, 2,...)

```
#include <stdio.h>  
#include <mpi.h>  
int main(int argc, char *argv[] ){  
	MPI_Init(&argc, &argv);  
	mpiRankWorkToDo();  
	MPI_Finalize();  
}
```

GNU: `mpicc`   `mpiexec -n 8 ./a.out`
Intel: `mpiicc`   `mpirun -np 8 ./a.out`

Script MPI: `sbatch -n 4 script.sh`
```
#!/bin/bash –l  
#SBATCH –D ./  
#SBATCH –p course  
#SBATCH –t 5  
module load compilers/intel/2019u5  
procs=${SLURM_NTASKS:-1}  
mpiicc file.c -o output.exe  
mpirun –np $procs ./output.exe
```

Script MPI & OpenMP `sbatch -n 4 -c 4 script.sh`
``` 
#!/bin/bash –l  
#SBATCH –D ./  
#SBATCH –p course  
#SBATCH –t 5  
module load compilers/intel/2019u5  
cores=${SLURM_CPUS_PER_TASK:-1}  
procs=${SLURM_NTASKS:-1}  
mpiicc –qopenmp file.c -o output.exe  
export OMP_NUM_THREADS=$cores  
mpirun –np $procs ./output.exe
```

## MPI Messages
### Point-to-Point communications
One sender, One receiver
- `MPI_Send()`
- `MPI_Recv()`

Returns: `MPI_SUCCESS`

Deadlock problem fixing: change the sequence on even ranks
```c
if(rank % 2 == 0){  
	MPI_Send(items_to_send, num, MPI_INT, next_rank, 0, MPI_COMM_WORLD);  
	MPI_Recv(items_to_recv, num, MPI_INT, prev_rank, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);  
}  
else if(rank % 2 == 1){  
	MPI_Recv(items_to_recv, num, MPI_INT, prev_rank, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);  
	MPI_Send(items_to_send, num, MPI_INT, next_rank, 0, MPI_COMM_WORLD);  
}
```

### Collective communications
- All processes participate