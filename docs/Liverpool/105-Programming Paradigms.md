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
- `:module [+/-] M1..[Mn]` load and unload modules
- Camel case usually
- the default module name: Main, use `module <name> where` at the beginning of the file to define it. The name has to be capitalized.

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
- *pattern matching*: `triple_head (x:xs) = 3 * x`
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


# 10/11/2023
- nested list: `f xxs [ [ x | x <- xs, even x ] | xs <- xxs]`

#### Recursive
- Recursive: a function calls the function it self
	- A base case
	- One or more rules moves the program closer to the base case
```haskell
factorial n = 
	if n > 1
	then n * factorial (n-1)
	else 1
```
- *Pattern matching*: Haskell will processes from top to bottom
```haskell
factorial 1 = 1
factorial n = n * factorial (n-1)
```
- each recursive rule makes progress towards the base case, otherwise, it will never terminate
- Every recursive function must have a base case, it will never terminate if no base case
```haskell
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n—2)
```
- multiple recursive rules: comprehensive
```haskell
even_sum 0 = 0
even_sum x = 
	if x `mod` 2 == 0
	then x + even_sum (x - 1)
	else even_sum (x - 1)
```
*Guards*: `| <test> = <expression>` which \<test> evaluates True or False; \<expression>can be anything. Good alternative to a load of nested ifs.
```haskell
even_sum x
	| (x == 0) = 0
	| (x `mod` 2 == 0) = x + even_sum (x—1)
	| otherwise = even_sum (x-1)
```

# 10/12/2023
### Recursion on lists
```haskell
sum’ (x:xs) = x + sum’ xs

length’ (_:xs) = 1 + length’ xs

square_list [] = []
square_list (x:xs) = x*x : square_list xs

take’ 0 list = []
take’ n [] = []
take’ n (x:xs) = x : take’ (n-1) xs

elem’ e [] = False
elem’ e (x:xs)
	| e == x =True
	| otherwise = elem’ e xs

maximum’ [] = error “Called with empty list”
maximum’ [x] = x
maximum’ (x:xs) = 
	let
		max_tail = maximum’ xs
	in
		if (x > maxtail) then x else max_tail

add_adjacent [] = []
add_adjacent [x] = error “Odd number of elements”
add_adjacent (x:y:xs) = x + y :add:adjacent xs

group n [] = []
group n list = 
	let
		first = take n list
		rest = drop n list
	in
		first : group n rest
```

# 10/13/2023
- `where`: bind names across a whole function.
```haskell
remove_twos [] = []
remove_twos (x:xs)
	| x == 2 = rest
	| otherwise x : rest
	where rest = remove_twos xs
```
```haskell
initials first last = [f] ++ “. “ ++ [l] ++ “.”
	where (f:_) = first
		  (l:_) = last
```
#### multiple lists recursion
```haskell
add_lists _ [] = []
add_lists [] _ = []
add_lists (x:xs) (y:ys) = x+y : add_lists xs yes

gt_10 [] = ([], [])
gt_10 (x:xs)
	| x > 10 = (x:gt, lt)
	| otherwise = (gt, x:lt)
	where (gt, lt) = gt_10 xs
```
`zip`: takes two lists and returns a list of pairs, shorter one determines the length
#### mutual recursion
```
events [] = []
events (x:xs) = x : odds xs

odds [] = []
odds (x:xs) = events xs
```
#### multiple recursion
```haskell
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)

fast_fib_help 1 = [1, 0]
fast_fib_help n = x + y : (x:y:xs)
	where (x:y:xs) = fast_fib_help (n-1)

> fast_fib n = head (fast_fifb_help n)
```
#### quick sort
```haskell
qs’ [] = []
qs’ (x:xs) = qs’ lower ++ [x] ++ qs’ upper
	where lower = [e | e <- xs, e < x]
		  upper = [e | e <- xs, e >= x]
```

# 10/18/2023
- Caesar Cipher: shift every letter forward a fixed count
- `import Data.Char`
- `ord`: returns an integer of a character (ascii)
- `chr`: returns a character of an integer
- `fromIntegral`: recieve an `Integral` instance and produce a `Num`
	- convets a value of type a (Integral) to type b (Num), which switch to a larger type could help the calculation operations (different type is not compatible on calculating) 
- chi-squared: distributed similay of two sets
- 尝试所有的密钥（26个），对每一个可能性（解密结果）进行卡方分布运算并于English的标准分布值进行对比，最后选出差异最小的一个结果
- Try all the keys (26), for each possibility (decryption result) perform the chi-square distribution operation and compare it with English's standard distribution value, and finally choose the one with the smallest difference.

# 10/20/2023
### Type of Haskell
	- Int: 64 bits integer
	- Integer: arbitrary size integers
	- Float: 32 bit floating point
	- Double: 64 bit floating point
	- Bool: True or False
	- Char: single character, using ‘’
- Tuple will have various types, separate by comma
- List have just a single type
- Function type is `[input type] -> [output type]`
- Function with multiple argument: `[First input] -> [Second argument] -> [output type]`

### Partial application
- fix some of the arguments; leave other arguments unfixed
- calling the function with fewer arguments

```haskell
func a b c = “Arguments: ” ++ [a,b,c]
func :: Char -> Char -> Char -> [Char]

func2 = func ‘x’
func2 :: Char -> Char -> [Char]

func3 = func ‘x’ ‘y’
func3 :: Char -> [Char]

pow2 = (^) 2
```
infix operators
```haskell
f = (/2)
g = (1/)
```
- function application should be thought of multiple partial applications
	- `multThree x y z = x * y * z`
	- `((multThree 2) 3) 4`
- use a tuple to carry arguments rather than by listed multiple arguments

# 10/25/2023
### Type polymorphism
- The function can be applied to any list
- a will represent the type of the list elements
- Type variable
```haskell
# :type
head :: [a] -> a
tail :: [a] -> [a]
zip :: [a] -> [b] -> [(a,b)]

third_head list = head (head (head list))
third_head :: [[[a]]] -> a

(+) :: Num a => a -> a —> a
(==) :: Eq a => a -> a -> -> Bool
```
- Type annotations
```
<function_name> :: <type>
```
- `Num`
	- `Integral`: whole numbers (Int, Inteer)
	- `Fractional`: rationals (Float, Double, Rational)

# 10/26/2023
- `show`: converts other types to strings
	- `Show`: type class contains types that can be shown
- `read`: converts strings to other types
	- `Read`: type class contains all types that can be read
- `Ord`: type class, all types that can be compared
	- tuples and lists are compared lexicographically, corresponding in sequence, following the shortest item
- higher order function: takes another function as an argument and returns a function
```haskell
apply_twice :: (a -> a) -> a -> a
apply_twice f input = f (f input)
```
- `composition`: applies one function to the output of another
```haskell
compose :: (b -> c) -> (a -> b) —> a -> c
compose f g input = f (g input)

compose (+1) (*2) 4 == 9
compose head head [[1,2], [3,4]]
```
- `.` operator removes the need for nested brackets
```haskell
f list = (length . double . drop_events. tail) list
```
- `$` operator evaluates its input, lowest precedence of all operators
```haskell
(length . tail) [1,2,3,4]
length . tail $ [1,2,3,4]
```
- *Anonymous functions*: define a function inline, also return other functions
	- `\` lambda-functions

```haskell
(\x -> x + 1)

\ [arg1] [arg2] … —> [expression]

—- higher order functions can take and return functions
swap :: (a -> b -> c) -> (b -> a -> c)
swap f = \ x y -> f y x

—-nicker syntax for partically apply a function
drop_six’ = (\ x -> drop 6 x)
```

# 10/27/2023
### Map
- applies a function f to every element in a list
```haskell
map’ :: (a -> b) -> [a] -> [b]
map’ _ [] = []
map’ f (x:xs) = f x : map’ f xs

map (*2) [1..5] == [2,4,6,8,10]
map (\(_:y:_)->y) [“the”, “quick”, “brown]


```

### Filter
- keeps only the element for which f returns True
```haskell
filter’ :: (a -> Bool) -> [a] -> [a]
filter’ _ [] = []
filter’ f (x:xs)
	| f x = x : rest
	| otherwise = rest
```

### Higher order programming
- map&filter
- de-emphasizes recursion
- focuses on applying functions to lists
- available in imperative languages

# 11/01/2023
### Fold
```haskell
foldr’ :: (a —> b -> b) -> b -> [a] -> b
foldr’ _ init [] = init
foldr’ f init (x:xs) = f x (foldr’ f init xs)

sum’’ list = foldr (\ x acc -> acc + x) 0 list


foldr1’ :: (a -> a -> a) -> [a] -> a
foldr1’ _ [] = error “empty list”
foldr1’ _ [x] = x
foldr1’ f (x:xs) = f x (foldr1’ f xs)

sum’ list = foldr1 (+) list
concat’ list = foldr1 (++) list
maximum’ list = folder (\ x acc -> if x > acc then x else acc) list

—- have to define a return value or default in statement


foldr: processes list from the right
foldl: processes list from the left
foldl :: (b -> a -> b) -> b -> [a] -> b

reverse_list list = foldl (\ acc x -> x : acc) [] list
```