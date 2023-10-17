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
- `True` `False`, Capital sensitive
- Boolean expressions: `&&` `||` `not`
- Equalities: `==` `/=`(not equal)
- Inequalities: `<` `>` `<=` `>=`
- Brackets: () bind the elements
- Evaluating: min, max
- `div`: integer; `/`: float
- `^`: integer; `**`: float
- mod
- commas-->spaces `<function_name>[<space><attr1>[<space><attr2>]]`
- \`\` infix operator
- () outfix operator
- -- comment; {- multiple line comment -}
- `:load func.hs` load the module, initial as `:l`
- `:reload` relade the module, initial as `:r`
- Camel case usually
- the default module name: Main, use `module <name> where` at the beginning of the file to define it. The name has to be capitaled.

#### IO
- `putStrLn`: to print sth, the displaying form of string is to be surronded by "". **Has side effect!!**
	- It is not pure function so is part of IO in Haskell
- `show`: could show anything, turns its input into a string

#### Compiling run
- `ghc <filename>` to compile the program/module, then execute it directly to run it
- If adding the module name declaration on the top, then a module be compiled; otherwise, a program will be compiled

# 10/04/2023
#### If expression
- no control flow in functional programming
- `gt10 x = if x > 10 then “yes” else “no”`
- `(if True then 1 else 0) + 6`
- Must have a *then* and a *else* statement
- Both branches must have the **same type**
- `if A then B else C
	- A is an expression that evaluates to True or False (only Boolean)
	- B and C are expressions that evaluates to the same type
- You can put ay expression in an if
- Is a function, must always return a value
- It is known as the ternary operator in imperative languages

#### Let expressions
- use the same expression More than once
- `let <bindings> in <expression>`
- `let a = 1; b = 2 in a + b
	- ****in**** in ghci
```Haskell
Cylinder r h=
	let sideArea = 2 * pi * r * h
	    top area = pi * r ** 2
	in sideArea + 2 * topArea
```

#### layout rules
- each definition at the same level should start on exactly the column
- space is suggested, just convert all the tabs into 4 spaces
- You can ignore the layout rule if use `{}`

# 10/05/2023
#### Tuple
- to bind two or more values together
- Using `()` and `,` to create it, can mix types
- `(6, “six”, “words”, 1)`
- Should be thought fixed size when compare two tuples
- **Function syntax**: 
- Curry can invert function with a tuple parameter to several separated parameters
- fst (1,2); snd (1,2) first or second value in the tuple, 2 parameters only.

#### Lists
- all have the **same type**
- Using `[]` and `,` to create it
- `[1, 2, 3, 4, 5]`
- Can have any number of elements
- Using `++` operator to join lists
- *Strings*: string is a list of characters in Haskell
	- `[‘a’, ‘b’, ‘c’]` == “abc”
	- "Hello" ++ “ world!” == “Hello world!”
- `!!` operator gets the specified element from the list, **zero-indexed**
	- `[1, 2, 3, 4] !! 1` == 2
- Internally Haskell will walk the entire list to get the last element
- Character ‘e’ have not same type with a String “e”
- *head* is its first element; *tail* is everything but the first element
- *last* is its last element; *init* is everything but the last element
- 1 : [2, 3, 4, 5] == [1,2,3,4,5]
- *pattern matching*: triple_head (x:xs) = 3 * x
	- *x* matching the *head*; the *xs* matching the *tail*
	- First_two (x:y:xs) = x * y: y is bound to the second element
	- Double_second(\_:y:\_) = 2 * y

# 10/06/2023
#### List functions
- `length` displays the number of element in the list
- `reverse`
- `sum` for integer list only, calculate the summary
- `product` for integer list only, calculate the product
- `take` returns the first x elements of the list
- `drop` returns the rest but first x elements
- `elem` returns True if the specified element is in the list

##### Ranges
- `[1..20]` number between 1 to 20, including the start and the end
- `[‘a’..’z’]`, `[‘A’..’Z’]`
- `[1, 3..10]` == [1, 3, 5, 7, 9]
- `[1..]` infinite list
- `take 5 [1..]` == [1, 2, 3, 4, 5]
- `head (tail [1..])` == 2

- `repeat 5` == [5, 5, 5, 5, 5, 5, ……]
- `take 10 (cycle “abc”)` == “abcabcabca”

#### List comprehension
- `[x*x | x <- [1..10]]` == [1,4,9,16,25,…….]
- could be seen as “for-each”
- `[x*x | x <- [1..10], x*x > 40, x*x < 80]`
- `[x | x <- “hello”, x /= ‘l’]` == “heo”
- `lt10 xs = [if x < 10 then “Yes” else “No” | x <- xs]`
	- `lt10 [8..11]` == [“Yes”, “Yes”, “No”, “No”] 
- `[x*y | x <- [2,5,10], y <- [8,10,11]]` == [16, 20, 22,…110]
- length’ xs = sum [1 | _ <- xs]
- `factors n = [x | x <- [1..n], n `mod` x == 0]`
- `primes n = [x | x <- [1..n], length factors x == 2]