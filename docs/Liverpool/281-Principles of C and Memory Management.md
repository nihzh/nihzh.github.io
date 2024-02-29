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