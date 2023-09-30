# 09/28/2023
- Imperative programming language
	- C, C++, Java, Python, PHP......
	- A list of instructions to the computer
- Functional programming language
	- *Haskell*, a pure functional language
	- More **methemetical**
	- Functional programming is **a style of programming**
	- No variables, No loops, No excplict idea of a sequence of instructions, Uses recursion
- A fectorial question:
	- Imperative: declare variables, around a loop, execute one each time.
	- Functional: no variables, no explicit looping (using recursion)
- complex algorithms are mostly functional
- A pure function is a balckbox
- Pure functions **only** influence the world through **return values** -- No changes global state, printing, connect netwoks.....
- Pure functions must be **deterministic**, no random contents
- *Side-effect* is anything changes global state, printing, connect netwoks which cannot **export same output when have same input**.
- same input, always same output.
- one function do one thing only.
- No control flow, everything is juct function application
- IO function has side-effect, call by pure functions

# 09/29/2023
- Interpreter "ghci"

#### Basic use of Haskell
- True False, Capital sensitive
- Boolean expressions: && || not
- Equalities: == /=(not equal)
- Inequalities: < > <= >=
- Brackets: () bind the elements
- Evaluating: min, max
- div: integer; /: float; mod
- commas-->spaces `<function_name>[<space><attr1>[<space><attr2>]]`
- \`\` infix operator
- () outfix operator
- -- comment; {- multiple line comment -}
- `:load func.hs` load the module
- `:reload` relade the module
- Camel case usually
- the default module name: Main, use `module <name> where` at the beginning of the file to define it. The name has to be capitaled.

#### IO
- `putStrLn`: to print sth, the displaying form of string is to be surronded by "". **Has side effect!!**
	- It is not pure function so is part of IO in Haskell
- `show`: could show anything, turns its input into a string

#### Compiling run
- `ghc <filename>` to compile the program/module, then execute it directly to run it
- If adding the module name declaration on the top, then a module be compiled; otherwise, a program will be compiled