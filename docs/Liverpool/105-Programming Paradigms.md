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
- *Pure functions* must be **deterministic**; must not including side-effect, no random contents
- *Deterministic*: When given same arguments, it always returns the same value
- *Side-effect* is anything changes global state, printing, connect netwoks which  **cannot export same output when having same input**.
	- Anything the function does that is visible to the outside world
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
- `:` add a element to the head of the list
	- `1 : [2, 3, 4, 5]` = \[1, 2, 3, 4, 5]
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
foldr’ :: (a -> b -> b) -> b -> [a] -> b
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

-- have to define a return value or default in statement


foldr: processes list from the right
foldl: processes list from the left
foldl :: (b -> a -> b) -> b -> [a] -> b

reverse_list list = foldl (\ acc x -> x : acc) [] list
```

# 11/02/2023
`scan`: like fold, outputs the accumulator at each step
```haskell
scanr (+) 0 [1,2,3,4] == [10,9,7,4,0]
scanl (+) 0 [1..10] == [0,1,3,6,10,15,21,28,36,45,55]

scanr’ :: (a -> b -> b) -> b -> [a] -> [b]
scanr’ _ init [] = [init]
scanr’ f init (x:xs) = 
	let
		recursed = scanr’ f init xs
		new = f x (head recursed)
	in
		new: recursed

scanl1: useint the first element in the list to be initial value
```

`takeWhile`: takes from a list while a condition is true
```haskell
takeWhile’ :: (a -> Bool) -> [a] -> [a]
takeWhile’ _ [] = []
takeWhile’ f (x:xs)
	| f x = x : takeWhile’ f xs
	| otherwise = []
```

`dropWhile`: drops from a list while a condition is true
```haskell
dropWhile’ :: (a -> Bool) -> [a] -> [a]
dropWhile’ _ [] = []
dropWhile’ f (x:xs)
	| f x = dropWhile’ f xs
	| otherwise = x:xs
```

`words`: converts a String to a list, elements are words separated by **spaces**
`unwords`: converts a list to a String that separate elements by a **space**

`zipWith`: zips two lists together using a function
```haskell
zipWith’ :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith’ _ [] _ = []
zipWith’ _ _ [] = []
zipWith’ f (x:xs) (y:ys) = f x y : zipWith’ f xs ys

m5 str1 str2 = [head str1] ++ show (length str2)
m6 list = zipWith m5 list list
```


# 11/03/2023
`x <- readFile “marks.csv”`
`lines`: split a String to a list by ‘\\n’
`unlines`: combine a list to a string that separate by ‘\\n’
```haskell
map words $ lines x
```

# 11/08/2023
#### Custom Types
- `type`: New name of existing type
- All types must start with capital letters, meaningful
```haskell
type VoteResults = [(Int, String)]
```

`data`: create an entirely new type, is not part of any type class
- `|` should be read as “or”
- each value is a constructor
- ordering by the order (Ord)
```haskell
data Bool’ = True | False
data Number = Three | Two | One deriving (Eq, Ord, Show, Read)
```
- Type classes
	- `Show`: print out the type as it is in the code
	- `Read`: parse the type as it is in the code
	- `Eq`: the natural definition of equality
	- `Ord`: constructors that come first are smaller

```haskell
data Point = Point Int Int deriving (Show, Read, Eq)
shift_up (Point x y) = Point x (y+1)

move :: Point -> Direction -> Point
```

custom `records`: can be created out of order
```haskell
data Person = Person String String Int String

get_first_name (Person x _ _ _) = x
get_second_name (Person _ x _ _) = x
get_age (Person _ _ x _) = x
get_nationality (Person _ _ _ x) = x
```
Haskell automatically creates getter for each parameter
```haskell
data Person = Person {first name :: String,
						secondName :: String,
						age :: Int
						nationality :: String}
							deriving(Show)
Person "joe" "blogs" 25 "UK"
```

- `fromIntegral` can specialize the type from and to

# 11/10/2023
#### Parameterised Custom Types
```haskell
data Point a = Point a a
:t Point (1::Int) (2::Int) == Point Int
```

`maybe` type: save version for functional code that might fail. This provides a **pure functional way** to deal with computations that might fil, and avoids the use of exceptions which are not pure functional.
```haskell
data Maybe a = Just a | Nothing
```

`case` expression: write all patterns on one line
```haskell
case [expression] of [pattern1] -> [expression]
```

`exceptions`: is **not pure functional**, only be used in IO code
- the `Maybe` type provides **exemption-like** behavior in pure functional code

`Either` type: This prosvedes a way to store two different types in the same data type, useful to store different types in the same list.
```haskell
data Eigher’ a b = Left a | Right b

let list = [Left “One”, Right 2, Left “three”, Right 4]
is_left (Left _) = True
is_left _ = False

map is_left list == [True, False, True, False]
```

Detailed errors: 
```haskell
safe_head_either [] = Right “empty list”
safe_head_either (x:_) = Left x
```

# 11/15/2023
Recursive custom types: constructuors contain the type itself
```haskell
data IntList = Empty | Cons Int IntList deriving(Show)

-- when using variant data types
data List a = Empty | Cons a (List a) deriving(Show)

our_head :: List a -> a
our_head Empty = error "Empty list"
our_head (Cons x _) = x

data TwoList a b = TwoEmpty
				| ACons a (TwoList a b)
				| BCons b (TwoList a b)
							deriving (Show)
```
- `Empty`: the data type represents this word finally, default value, can be any group of letters
- `Cons`: name of the constructor, can be any group of letters
- `Int`: forced data type
- `a`: any data type, it will be determined when instantiate this type
- `Cons a (List a)`: constructor expression, in this case, it can be instantiated recursively by 
	- `Cons 1 (Cons 2 (Cons 3 Empty))`, equivalent `[1,2,3]`, `:t` = `:: Num a => List a` (when the value not be defined precisely, show a greater set)
	- `Cons 1 (Cons (2::Int) (Cons 3 Empty))`, `[1,2,3]`, `:t` = `:: List Int` (any of each is defined precisely, become a certain value)
	- `Cons 1 (Cons 'b' (Cons 3 Empty))`, error, the data type must same all the time
	- `Cons 'a' (Cons 'b' (Cons 'c' Empty))`, equivalent `['a', 'b', 'c']`, `:t` = `List Char`

Trees: a classical data structure
```haskell
data Tree = Leaf | Branch Tree Tree deriving (Show)

size :: Tree -> Int
size (Leaf) = 1
size (Branch x y) = 1 + size x + size y
```

Trees with data
```haskell
data DTree a = DLeaf a
			| DBranch a (DTree a) (DTree a)
							deriving (Show)

-- Recursion on trees with data
tree_sum :: Num a => DTree a -> a
tree_sum (DLeaf x) = x
tree_sum (DBranch x l r) = x + tree_sum l + tree_sum r


-- formulate the file directory as a data tree, find a file
find_file file (DLeaf x)
	| x == file = Just file
	| otherwise = Nothing

fild_file file (DBranch x l r) = 
	let 
		left = fild_file file l
		right = fild_file file r
	in
		case (left, right) of
			(Just y, _) -> Just (x ++ y)
			(_, Just y) -> Just (x ++ y)
			(_, _) -> Nothing

```

# 11/16/2023
### IO
Non-pure functional programming
- Print, read/write a file, communicate over network, create GUI
- IO code can call pure functions
`getLine`: reads a line of input from the console
	`getLine :: IO String`, is not a String type
`getChar`: `getchar :: IO Char`
- If a function returns an IO type than it is impure
	- may have side effects
	- may return different values for the same inputs
- IO type should be through of as a **box**
	- holds a value from an impure computation
	- use `<—` to get the value out, will be convert to normal type
```haskell
x <- getLine
hello
x == "hello"
:t x == x :: String
```
The values must be **unboxed** before that are used in pure functions
```haskell
x <- getLine
head x
```

`putStrLn`: prints a string into the console
```haskell
putStrLn :: String -> IO ()

() Unit
```

The return type of a function can be `IO ()`
The `do` syntax allows us to combine multiple IO actions, the final IO action is the return value
- will not work in pure function code
- works with IO actions

```haskell
get_and_print :: IO ()
get_and_print =
	do
		x <- getLine
		y <- getLine
		putStrLn (x ++ " " ++ y)
```

`if` expression can be used inside do blocks
`let` expression can be used inside do blocks
```haskell
add_one :: IO ()
add_one = 
	do
		n <- getLine
		let num = (read n) :: Int
			out = show (num + 1)
		if out == "42"
			then putStrLn "correct!"
			else putStrLn "wrong!"
```

`return`: put a pure value into IO, packate a value to a *Just* constructor
```haskell
:t return "hello"
IO [Char]

return ()  -- print nothing
```
- just converts pure values to IO values
- not like return in imperative language

```haskell
:t return
return :: Monad m => a -> m a
```
- *Monad*: abstract calculation structure, provides a method for serializing the steps of a computation, passing and manipulating values are allowed in the computation procedure. instance including `Maybe`, `List ([])`, IO
	- Linking the computation steps together by defining some operations, and pass the value through the different stages of the computation
	- **"boxed"**: Monad (IO)

```haskell
class Monad m where
	return :: a -> m a
	(>>=) :: m a -> (a -> m b) -> m b
```
- `>>=`: *bind operaor*, recieve a Monad and a function, pass the Monad to the function and returns a new Monad

# 17/11/2023
ghc
```haskell
ghc code.hs
code
```

`getArgs :: IO [String]` returns arguments by a list, in `System.Environment`
loop in IO code
```haskell
printN :: String -> Int -> IO ()
printN _ 0 = return ()
printN str n = 
	do
		putStrLn str
		printN str (n-1)

main :: IO ()
main = do
	args <- getArgs
	let n = read (args !! 0) :: Int
	printN (args !! 1) n
```

`read file :: String -> IO String`
```haskell
readFile "example.txt"
```

`write file :: String -> String —> IO ()`, the file will be **overwritten**.
```haskell
writeFile "output.txt" "hello\nthere\n"
```

report function
```haskell
main :: IO ()
main = do
	args <- getArgs
	let infile = args !! 0
		outfile = args !! 1
	input <- read file infile
	writeFile outfile (report input)
```

`print`: same as (putStrLn . show), print every characters
`putStr`: print a string without a new line
`readLn`: gets a line of input and calls read
`forever`: repeats an IO action forever, in `Control.Monad.package`
```haskell
process :: IO ()
process = do
	putStr "input: "
	l <- getLine
	putStrLn (map toUpper l)
```

`sequence` performs a list of IO actions
```haskell
sequence :: [IO a] -> IO [a]
sequence [getLine, getLine, getLine]

sequence (map print [1,2,3])
1
2
3
[(),(),()]
```

`mapM :: (a -> IO b) -> [a] -> IO [b]`: same as `sequence (map print [])`

`when :: Bool -> IO () -> IO ()`
```haskell
when True (print "hi")
```

`unless`: executes an IO action of a condition is false

# 11/22/2023
IO action can return any type, complex types
have to unbox and rebox the output of the recursion
```haskell
get_lines :: IO [String]
get_lines = do
	x <- getLine
	if x == "
		then return []
		else do
			xx <- get_lines
			return (x : xs)
```

```haskell
print_screen :: [String] -> IO ()
print_screen [] = return ()
print_screen (x:xs) =
	do
		putStrLn x
		print_screen xs

make_screen :: Int -> Int -> [String]
make_screen x y = [replicate x ‘ ‘ | _ <- [1..y]]
```

```haskell
modify_list :: [a] -> Int a -> [a]
modify_list list pos new = 
	let
		before = take pos list
		after  = drop (pos + 1) list
	in
		before ++ [new] ++ after


set :: [String] -> Int -> Int -> Char -> [String]
set screen x y char =
	let
		line = screen !! y
		new_line = modify_list line x char
		new_screen = modify_list screen y new_line
	in 
		new_screen


set_list :: [String] -> [(Int, Int, Char)] -> [String]
set_list screen [] = screen
set_list screen ((x,y,c) : xs) = 
	set (set_list screen xs) x y c


letter_a :: [(Int, Int, Char)]
letter_a = map (\ (x, y) -> (x, y ‘#’)) [
   …
]

—shift letter to the right
shift_letter :: [(Int, Int, Char)] -> Int -> [(Int, Int, Char)]
shift_letter letter shift = 
	map (\ (x, y, c) -> (x + shift, y, c)) letter


big_letters :: [String] -> Int -> IO ()
big_letters screem cursor = 
	do
		c <- getLine
		let lett = case head c of
				‘a’ -> letter_a
				‘b’ -> letter_b
				otherwise -> []
			new _screen = set_list screen (shift_letter lett cursor)
		print_screen new_screen
		big_letters new_screen (cursor + 6)


main :: IO ()
main = big_letters blank_screen 0
```

# 11/23/2023
- *Strict evaluation*: always apply the innermost functions first. Arguments to a function must be fully evaluated before the funciton itself is evaluated
	- Imperative languages are always strict
- *Lazy evaluation*: always apply the outermost functions first. functions can be aplied to arguments that are not yet fully evalueated
	- only comutes a value when it is needed
	- if value is never used, it is never computed
```haskell
let f x = 1
f undefined == 1
```
- For pure functions the order of evaluation is irrelevant, Haskell are lazy by default
- Laziness allow us to do infinite computations on infinite lists
```haskell
all_1s = 1 : all_1s
all_2s = zipWith (+) all_1s all_1s
```

- `$` operator evaluates a function
- `$!` operator does strict evaluation, it forces the argument to the function to be evalueated before the function itself is evaluated

# 11/24/2023
- *Tail recursion*: there is nothing left to do after the recursive call
```haskell
is_even 0 = True
is_even 1 = False
is_even n = is_even(n - 2)
```
- No call stack is built up
- Less memory is used
```haskell
fact_tail 1 acc = acc
fact_tail n acc = fact_tail (n-1) $! (acc*n)
factorial n = fact_tail n 1
```

```haskell
-- evedn
foldl f acc [] = acc
foldl f acc (x:xs) = foldl f (f acc x) xs

-- strict version of foldl, usually less memory
foldl' f acc [] = acc
foldl' f acc (x:xs) = (foldl' f $! (f acc x)) xs
```
left fold can destroy laziness, which must reach the end of the list to get the accumulator

# Next
- Recursive algorithms: sorting, tree, graph
- file handling, networking, GUIs, games, via the cabel system
- https://hackage.haskell.org/
- https://www.haskell.org/hoogle/
- alternatives for linked lists in haskell
	- `Data.Vector` provides arrays
	- `Data.Text` gives packed uniode string representations
- Monads: Learn You a Haskell
- build own imperative language with monad transformers
- lenses for deeply nested records
- advanced type system
	- Rank-N
	- Existential
	- Linear
	- Dependent
	- *What I Wish I Knew When Learning Haskell*