An algorithm is a sequence of steps for performing a task in a finate amount of time.

### Loop  invariants
*Loop* invariants are useful to show correctness of an alorithm given as pseudo-code
- *Initialisation*: it is true prior to the first iteration of the loop.
- *Maintenance*, if it is true before an iteration of the loop, it remains true before the next iteration
- *Terminaation*: when the loop terminates, the invariant gives is a useful property that help show the algorithm correct

### running - time
#### primitive operations
- asignment, single plus, multiple, compare.....
#### Big-Oh Notation
Given two positive functions *f(n)* and *g(n)*, **f(n) is O(g(n))**, written as `f(n) ∈ O(g(n))`, with constants *c* and *a0*: `f(n) <= c*g(n) for all n >= n0`
- Any polynomial `akn^k + ... + a2n^2 + a1n + a0` with **ak > 0** is `O(n^k)`, also `O(n^j)` for all **j >= k**
Common functions:
- *Logarithmic* O(log n)
- *Linear* O(n)
- *Quadratic* O(n^2)
- *Polynomial* O(n^k) for a positive integer k
- *Exponential* O(a^n), a > 1

g(n) is O(f(n)) and f(n) is O(g(n))

#### Justification Techniques
- *Methemetical induction*
- *Contradiction*: Suppose the proposition is not true
- *Contrapositive argument*: p => q is equivalent to ¬q => ¬p
- *Counterexample* (disproof)

## Divide-and-Conquer
- Merge sort: `O(nlogn)`, dividing/merging is `O(n)`, recursive at most `O(log n)`
- Incremental algorithm
- *Divide*: If the input size is small then solve the problem directly; otherwise, divide the input data into two or more subsets, typically disjoint
- *Recur.*: Recursively solve the sub-problems associated with subsets
- *Conquer*: Take the solutions to sub-problems and merge into a solution to the original problem

- *recurrence relation*: `T(n)`, the worst-possible running time on an input of size **n**, relates T(n) to values of function T for problem sizes smaller than n

![](../img/9c3f036b0e1ef8d7e3654569b514109.jpg)

```
T(n) = 2^j T(n/2^j) + jcn
for j = log n
T(n) = 2^(log n)c + cn log n = Θ(n log n)
```

### Matrix Multiplication
*Volker Strassen (1969)*

### Master method
![master_method](../img/Pasted%20image%2020240522013035.png)


## Data stucture
- Arrays
- Linked List

### Rooted trees
sortable, still efficient for search, insert/delete
- **binary tree**
- max value index at root
- min value index at root

#### Data structures for rooted t-ary trees
For rooted trees where wach node has at most *t* children, and is of **bounded depth**, you can **store the tree in an array A**. This is most useful when you're woring with (almost) complete t-ary trees.

In general, two children of node `A[i]` are in `A[2 * i + 1]` and `A[2 * i + 2]`
The parent of node `A[i]` is the node in position `A[(i-1) / 2]`

#### Binary search tree (BST)
Given a node *v* string the element *e*, all element in the **left subtree** at *v* are **less than** or equal to *e*, and those in the **right subtree** at *v* are **greater than** or equal to *e*
- balanced required for efficiency
- self-balancing BSTs
	- AVL trees
	- red-black trees

#### Heap Data Structure
The elements and their keys are stored in an almost complete binary tree (most of times), every level of the binary tree (expect last), will have the maximum number of children possible.
- *Heap-order* property: In a heap T, for every node v, the key at v is less than(equal) the key stored at its parent

##### Root deletion
1. swap root with last element
2. delete last element (bottom, right-most)
3. bubble root (last) down

#### Merge Sort / Heap Sort
- **O(n log n)**
- comparison-based

## Sorting
### Counting inversions
up to `n(n-1) / 2` for the permutation, number of inversions range starts from 0

*divide-and-conquer*: **O(n log n)**: sort each sublist and merge them recurcively into a single (sorted) list, and count the inversions from each part.

### Quick sort
**Select a pivot element randomly** to avoiding the L and G are ufficiently large

### Interval scheduling
- A collecction of tasks
- A single macchine that can process these tasks
- To selet a subset of the tasks in order to maximize the number of tasks that can schedule on the machine.
- Maximum utilize resources/working completion

- Basic Probability
- Sample space
- Probability spaces
- Probability function
- Independent Events
- Conditional Probability
- Random variables

```
E(X) = Pr(X is heads)*1 + Pr(X is tails)*(1+expected number of additional coin tosses until first heads appears)
```

- Randomised quicksort

### Linear-time algorithms
- Aren't comparison based
- Require a promise that the elements in the input aren't too large

#### Counting sort
Assumes that each of the n input elements is an integer between 0 and k, when k = O(n), counting sort runs in O(n) time
- Input A\[1..n], output B\[1..n], use temp storage C\[1..n]
- **stable**

1. for array *C*, puts content integer of *A* as index, the reffered value is count
2. transfer *C* to new indexes (`C[i] += C[i-1]`)
3. insert values to array *B* by new indexes

#### Radix Sort
First sort by the least significant digit. Next sort by second-least significant digit.
- non-negative integer input required

## Dynamic Programming
Primarily used for optimization problems (maximizing or minimizing some function), often applied where a *brute force* search for optimal value is infeasible.

Dynamic programming is efficient only if the problem has a **certain amount of structure** that can be exploited.
- **Simple sub-problems**: can be breaked into smaller sub-problems with similar structure.
- **Sub-problem optimality**: An optimal olution to the global probmen musst be composed of optimal solutions to a sub-problem, or collection of sub-problems.
- **Sub-problem overlap**: Optimal solutions to some sub-problems can themelves contain sub-problems in common.

### Find a recursive solution
Optimization
- first find a recursive recursion solution to the problem

### Fibonacci
![fibonacci](../img/Pasted%20image%2020240522115536.png)
Repeated squaring, gives **O(log n)** time
![repeted squareing](../img/Pasted%20image%2020240522115646.png)

### Greedy method
Solves a given **optimization problem** by going through a sequence of feasible choices, Problems that have greedy solution -> *greedy-choice property*
- start from well-understood config
- iteratively makes the decition (seems best from possibles)
- **Not always lead to an optimal solution**, used for some hard problems in order to generate *appproximate solutions*

#### Interval Scheduling


## Graphs
**G = (V , E)**, is a set
- *V* of vertices
- *E* collection of pairs of vertices from *V* , called *edges*
- An edge (u, v)
	- if the pair is ordered, it is directed from **(u, v)**
	- unordered, it is undirected, **{u, v}**
	- All edges of a graph are directed, refer to *G* as a *digraph*
- *Adjacent vertices*: two vertices are end-points of the same edge
- *Incident to a vertex*: the vertex is one of an edge's end-points
- *Outgoing edge of a vertex*: a directed edge which origin from that vertex
- *Incoming edge of a vertex*: a directed edge which destinate to that vertex
- *Degree of a vertex, deg(v)*, the number of edges incident to v
	- *indeg(v)*
	- *outdeg(v)*
- *Walk*: a squence af alternating vertices and edges, start and end at a vertex
- *Path*: a walk where each vertex is distinct
- *Circuit*: a walk with same start and end vertex
- *Cycle*: a curcuit where each vertex is distinct (except first and last)
- *Directed walk*: a walk which alledges are directed and are traversed along their direction

Let *G* be a dimple graph with *n* vertices and *m* edges
- if *G* is undirected, then *m* <= `n(n-1)/2`
- if *G* is directed, then *m* <= `n(n-1)`

- *Subgraph of G*: a graph H whose vertices and edges are stbsets of the veritces and edges of G
- *Spanning subgraph of G*, a subgraph of G that contains all the vertices of G
- A graph is *Connected* if, for any distinct vertices, there is a path between them. `m >= n-1`
- If G is not connected, its maximal connectedd subgraphs are called the *Connected components* of G

- A *forest* is a graph without cycles, `m <= n-1`
- A *tree* is a connected forest (connected graph without cycles), `m = n-1`
- A tree with a distinguished node is *rooted tree*, otherwise *free(simply) tree*
- *Spanning tree* of a graph: a spanning subgraph that is a free tree

- *Weighted graph*: a graph that has a numerical label *w(e)* associated with each edge *e*, called the weight of *e*

### Graph search methods
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- both **O(n + m)**

### Single Source Shortest Paths
- *Dijkstra's algorithm*: Greedy method, only give correct result when weights are non-negative

#### Bellman-ford algorithm
![bellman-ford](../img/Pasted%20image%2020240522173528.png)
- Total of |V| iterations, each iteration relaxes all of the |E| edges. Each edge relaxation takes O(1) time, total time: *O(|V|\*|E|)*

### All pairs shortest paths
- run Bellman-Ford once for each vertex as source, *O(|V|^2 \* |E|)* => *O(n^4)*
- use dynamic programming
- *O(n^3 log n)*
![APSP_matrix multiplication](../img/Pasted%20image%2020240522180642.png)

## Network Flow
- weight graph w(e) associated with each edge *e*
- Directed graph in which each edge (u,v) has a non-negative integer **capacity** *c(u, v)* >= 0
- **Source** *s*(no in-edges) and **sink** *t*(no out-edges)
- **Capacity constraint**: each edge (u, v) also associated **flow value** *f(u, v)*, which indicates how much flow has been sent along an edge
	- **0 <= f(u, v) <=  c(u, v)**
- **Flow conservation**: for every vertex other than *s* and *t*, the amount of flow into and out must equal

### Maximum flow problem
Given a flow network G, with source *s* and sink *t*, wish to find a flow of maximum value from *s* to *t*.

#### Ford-Fulkerson method
Searches for a flow-srgumentingn path from the source to the sink vertex, then send as much flow as possible along the flow-augmenting path, whilst obeying the capscity constrains of each edge

The maximum flow can be send along the path is limited by the minimum of `c(u, v) - f(u, v)` of an edge on this path

Iterative: 
1. Start with f (u, v ) = 0 for all u, v ∈ V
2. At each iteration, we increase flow by finding an augmenting path from s to t along which we can push more flow. (We consider the residual network when we search for augmenting paths.)
3. repeat until no more augemnting paths can be found
4. the *Max-Fow Min-Cut theorem* shows that this process yields a maximum flow
![](../img/Pasted%20image%2020240522213341.png)

##### Residual Networks
- edges that can admit more net flow
- forward edges: 
- backwards edges

##### Augmenting paths
For a flow network *G = (V, E)* and a flow *f*, an augmenting path *P* is a directed path from *s* to *t* int he residual network Gf, is a path from the source to the sink in which we can send more net flow.

##### Cuts in Networks
A **cut** *(S, T)* in a flow network *G = (V, E)* is a partition if the vertices *V* into *S* and *T = V - S* such that s ∈ S and t ∈ T

The Max-Flow/Min-Cut Theorem mentioned that a flow is maximum if and only if no augmenting path exists.

![flow_of_cut](../img/Pasted%20image%2020240522220951.png)

Capacity of a cut
![capacity_of_a_cut](../img/Pasted%20image%2020240522220800.png)

##### Complexity
*O(n + m) = O(m)*

#### Max-Flow/Min-Cut theorem
The maximum flow is a network is equal to capacity of a minimum cut in the network.

### bipartite graph


## NP-complete problems
### Decision Optimization problems
NP-completeness is fomulated in terms of decision problems
- *Decision problem*: a computational problem for which the output is either **yes** or **no**
- *Optimization problem*: try to maximize or minimize some function
An *optimization problem* can be turned into a *dicition problem* by adding a *parameter k*, and then asking whether the value of the function is at most or at least k

Efficiently answer decisionn questions allows us to efficiently solve the related optimizasation problem. To find the optimal solution by a type of *binary search*.

### Complexity Class P
The set of all decision problems X that can be solved in worst-case polynmomial time

There is an algorithm A that if the answer to a decision problem *s* is *yes*, then this can be determined in time *p(|s|)*, where *|s|* is the size of *s* (typically binary representation), and *p()* is a polynomial

### Efficient certificaion
Check a candidate for a question ==> verifies each boundaries ==> certificate for the decision problem

### Complexity Class NP
Non-deterministic Polynomial time.

All *decision problems* for which there exists an *effcient certifier*

An *efficient certifier* for a decision problem *X* is an algorithm *B* that takes two input strings *s* and *t*. r is the proof

"Efficient" means that B is a polynominal-time algorithm
```text
there is a polynomial function q(·) so that for every input s, then  
s has answer "yes" if and only if there exists a string t such that  
|t| ≤ q(|s|) and B(s, t) = "yes".
```

An algorithm that chooses (by a good guess) some number of *non-deterministic bits* during its execution is called a non-deterministic algorithm.

We say that an algorithm A non-deterministically accepts a problem s if there exists a choice of non-deterministic bits that ultimately leads to the answer “yes.”

The class NP is the set of decision problems X that can be  
non-deterministically accepted in polynomial time. For an input string s, the non-deterministic algorithm can generate a (polynomial length) string t, then we use the algorithm B to check if B(s, t) = “yes.

### The Class co-NP
The set of problems for whic there is an effiecient verification method for when tthe answer is "no"

### NP-hardness
![](../img/Pasted%20image%2020240523002649.png)

![](../img/Pasted%20image%2020240523002530.png)

### Cook-Levin Theorem
***Circuit-SAT is NP-complete***
The computation steps of any (reasonable) algorithm can be simulated by layers in appropriately constructed (polynomial time and size) Boolean Circuit

### Types of reduction
Let M be an NP-complete problem
- *Restriction*: NP-complete problem is a spacial case of problem L
- *Local replacement*: Dividing instances of M and L into basic units, and showing how each basic unit of M can be locally converted into a basic unit of L
- *Component Design*: Building components for an instance of L that will enforce important structural functions on M

## Cryptography
- Public-key cryptosystems
	- E: one-way function\trapdoor function

### Elementary number theory - Divisibility
Theorem: Let a, b, c be integers.  a|b:  b is a multiple of a
1. If a|b and b|c, then a|c. (transitivity)  
2. If a|b and a|c, then a|(i · b + j · c) for all integers i and j.  
3. If a|b and b|a then either a = b or a = −b.

### Modulo and Congruences
*a is congruent to b mod n*: a mod n = b mod n, `a ≡ b (mod n)`
In other words, if a ≡ b (mod n), then a − b = kn for some  
integer k

### Euclid algorithm
A method to find the greatest common divisor of two integers a and b
```text
Theorem: Suppose that a ≥ b > 0. Then  
		gcd(a, b) = gcd(b, a mod b).
```
![](../img/Pasted%20image%2020240523013657.png)
Complexity: *O(log(max{a, b}))*, a, b are positive integers.

### Extended Euclidean algorithm
![extended_euclidean](../img/Pasted%20image%2020240523014321.png)

### RSA encryption algorithm
- Digital signatures
- Complexity: *O(log n)* at each block(encrypt, decrypt, signature, verification, etc.), *O(log k)* arithmetic operations to find `x^k mod n`

### Fast exponentiation
Find xi mod n to keep the results small
![](Pasted%20image%2020240523015334.png)