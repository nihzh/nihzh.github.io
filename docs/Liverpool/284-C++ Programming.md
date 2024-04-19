## c++
- memory management
- object-oriented
- platform dependent
- standard template library

## namespace
namespace avoid name clashes and organise code
- `::` to reference the global namespace
- std

## iostream
- `cin`: standard c input stream
- `cout`: standard c output stream
- `cerr`: standard c error stream, **unbuffered**
- `clog`: standard c error stream

## class
- access modifiers
	- public: accessed anywhere
	- private: 'frient' classes or functions can still access it
	- protected: only access within class, subclasses and frient classes
- the class has to be defined inside the namespace, which should in `.cpp` file, or using `using namespace` in the `.h` file
- *constructors*: allocate memory for class member variablels
	- `Animal(int value);`
- *destructors*: free and tidy the memory, Class variables’ memory is freed automatically when they fall out of scope
	- `~Animal();`

### virtual polymorphism
- In normal heritation of two classes, *static binding* – method resolution is based on the type of pointer, not the object it points to
- To fix this: *dynamic binding* -- using `virtural` keyword to decorate the function, then the pointer will 
- the parent class constructor is always called before the constructor of the chiled class
![](/img/Pasted%20image%2020240315163805.png)

### passing objects to functions
- direct passing
- pass a pointer
- pass by references

### permanent objects
- `new` keyword
```cpp
SettingsDialog* settingsDialog = new SettingsDialog();
settingsDialog->show();
```

### Overloading
- Multiple functions can have **same name** and **different parameters**
- picked at compile time

#### Operator overloading
- enable to add two attributes from class
- define custome behaviour for operators when thay are used with objects of new data types
- usuallu overload maths and io operators
- after c++20, spaceship `<=>` to make new operators

#### Constructor overloading
- The class definition needs private variables for its internal data, plus a way to construct an object from incoming values
```cpp
bool Ruler::operator==(const Ruler& ru) {  
return this->feet == ru.feet && this->inches == ru.inches;  
}
```

## Unary and Binary operators
- prefix-unary: `-`, `++`, `--`, `!`, `&`
- postfix-unary: `++`, `--`
- binary: `-`, `+`
```cpp
returntype operator-();
returntype operator++(int);
```

#### overloading `<<` outside count
Friendship allows accessing private attributes outside the class
```cpp
friend std::ostream& operator<<(std::ostream&, const Ruler&);
friend std::istream& operator>>(std::istream& input, Ruler& ru);
```

#### overloading outside class
