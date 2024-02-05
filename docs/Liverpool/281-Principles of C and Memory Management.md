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