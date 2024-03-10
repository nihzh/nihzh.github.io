### Memory
- stack: growing from higher to lower
- free memory: for growing of stack and heap
- heap: growing from lower to higher
- uninitialised data
- initialised data
- code

### C compiling and running
1. Editor —> 
	1. \*.c files, contain function definitions
	2. \*.h files, contain function declarations, preprocessor statements
3. Preprocessor
	1. preprocessor command: `#include`, `#define`, `#undef`…
4. Compiler —> e.g., gcc
	1. \*.o files, contain function definitions in **binary form**
	2. `-c` for compile but not link, generate object file
5. Linker —>
	1. \*.exe files (no suffix on macOS or Linux), binary executable, made from few object file
	2. `-o` define the name of the output exe
6. Loader
7. CPU(execute)

#### constants
declare by `const` or `#define` keyword
- Integer: `const int MAX_NUM = 999`
- Floating point: `const double a = 1.23e4`
- Character: `const char a = ‘a’`
- Enumeration: `enum City { Manchester, Liverpool, Leeds};`

### Output function
`%[flags][minimum-field-width][.precision]Type`
*flag*: -, +, 0, #, space
- space: a space for positive signed-numeric types
- \#: hash, o for octal, x for hex
*width*: +/-, number, \*
- \*: value that computed at run-time `printf(“|%-*s|”, 5, “abc”);` ==> `|abc  |`

### Switch statement
the condition expression must be a **integer expression**

### Pointer
- A variable holding the **address** of onother variable of same data type, to access memory and manipulate the address
- `%p` format specifier for addresses
- `&x` address of variable x
- stores a referennnde to another value *pointee*
- *Double Pointer (pointer to pointer)*: store the address of a pointer variable
- `*` *dereference operator*, using in an expression, fetch the contents at the that address
- `(*z)++` to increase

#### Pointer to functions
`type (*pointer-name)(parameter)`
```c
#include <stdio.h>
int sum(int x, int y){
	return x + y;
}
int sum6_9(int (*fp2)(int, int)){
	return fp2(6, 9);
}
int (*functionFacroty(int z))(int, int){
	int (*fp)(int, int) = sum;
	return fp;
}
int main(void){
	int (*fp)(int, int);
	fp = &sum;
	printf(“Sum:%d”, (*fp)(6, 9));
	printf(“Sum:%d”, functionfactory(3)(6, 9));
}
```

## Point to struct
```c
typedef struct { /* no name for the struct */
 int x;
 int y;
 double dist;
} Point, *pointPtr;
…
p1.x = 5; p1.y = 6;
pointPtr p = &p1;
printf(“%d:%d\n",p->x,p->y);
```

### union
A special datatype allowing us to store different datatypes in the same physical memory location, can have many members, but only one member can contain a value at any given time.
Similar declare/define with struct, different on memory usages
- to assign a value to a union member, the member name must be linked with the union variable using `.` operator

### string
A sequence of chars that is treated as a single data item and terminated by an additional null char `\0` at the end, actually an array of chars
## Storage classes
- *Automatic* variables (default): `auto int a` == `int a`
- *External* variables: accessible by any function in the program
	- `extern int a`: used with a variable to inform the compiler that this variable sis declared somewhere else. (external file)
- *Static* variables: 
	- `static int a`: initialized once, remains unti end of the program
- *Register* variables: inform the ccompiler to store the variable in CPU register instead of memory
	- `register int a`
	- faster acccessibility
	- cannot address

## Memory Management in C
- *Static-duration* variables: allocated in the main memory, persist for lifetime of the program
- *Automatic-duration*: allocated on the stack, as functions call and return

### Dynamically Memory Allocation
- free memory located at the moddle of stack and heap
![[Pasted image 20240229152121.png]]
- `malloc`: allocate a block of memory on the heap, dyynamic arrays
	- 1 argument: size in types
	- returns `void *`, pointer to anything
- `calloc`: 
	- 2 arguments: number of things, size of each thing in bytes
	- returns a pointer to chunk of memory allocated
	- sets each value to zero
- if `malloc` or `calloc` fail, returns `NULL`
	- `exit(1)`
- `free`: returns the momory to the system, will lead to **memory leak** if not free the memory
- `realloc`

## Stack
- FILO First In Last Out
- Local variables and function arguments, return values
- each function cal generates a new stack frame
- after function returns, teh stack frame release
- push variables to stack when calling other function, pop when return
- recurstion

## Heap
- the general pool of computer memory
- memory is alocated on the heap using `malloc` / `calloc`
- must be explicitly freed using `free`, otherwise memory leak

`sizeof()` is NOT a function, take a type name as an argument
On 64 bit machines, size of all types of pointer is always 8 bytes
- `int*`, `char*`, `float*`, `double*`

When pointer as a function parameter, call by reference, will affect the original variable. Local variables of a function don't have a life outside of the function