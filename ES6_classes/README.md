# ES6 Classes Learning!




# General Questions:




## How to define a class?
In ES6, you can define a class using the `class` keyword. Here's a basic example:

```javascript
class MyClass {
  constructor(myParameter) {
    this.myProperty = myParameter;
  }

  myMethod() {
    console.log(this.myProperty);
  }
}
```

In this example, `MyClass` is the class name. The `constructor` is a special method for creating and initializing an object created with a class.
`myMethod` is a method on the class. You can create an instance of the class and call its method like this:

```javascript
let instance = new MyClass('Hello, world!');
instance.myMethod();  // Outputs: 'Hello, world!'
```




## How to add methods to a class?
In ES6, you can add methods to a class by defining them inside the class body. Here's an example:

```javascript
class MyClass {
  constructor(myParameter) {
    this.myProperty = myParameter;
  }

  myMethod() {
    console.log(this.myProperty);
  }

  // Adding a new method
  anotherMethod() {
    console.log('This is another method');
  }
}
```

In this example, `anotherMethod` is a new method added to the `MyClass`. You can call this method on an instance of the class like this:

```javascript
let instance = new MyClass('Hello, world!');
instance.anotherMethod();  // Outputs: 'This is another method'
```




## Why and how to add a static method to a class?
Static methods are methods that are called on the class itself, not on instances of the class. They're often used for utility functions that don't
depend on the state of an instance.

Here's how you can add a static method to a class in ES6:

```javascript
class MyClass {
  constructor(myParameter) {
    this.myProperty = myParameter;
  }

  myMethod() {
    console.log(this.myProperty);
  }

  // Adding a static method
  static myStaticMethod() {
    console.log('This is a static method');
  }
}
```

You can call the static method directly on the class, like this:

```javascript
MyClass.myStaticMethod();  // Outputs: 'This is a static method'
```

Note that you cannot call the static method on an instance of the class:

```javascript
let instance = new MyClass('Hello, world!');
instance.myStaticMethod();  // This will throw an error
```




## How to extend a class from another?
In ES6, you can extend a class from another class using the `extends` keyword. Here's an example:

```javascript
class MyBaseClass {
  constructor(myParameter) {
    this.myProperty = myParameter;
  }

  myMethod() {
    console.log(this.myProperty);
  }
}

class MyDerivedClass extends MyBaseClass {
  // MyDerivedClass inherits all methods from MyBaseClass

  // You can also add new methods or override the existing ones
  anotherMethod() {
    console.log('This is another method in derived class');
  }
}
```

In this example, `MyDerivedClass` is a subclass of `MyBaseClass` and inherits all its methods. You can create an instance of the subclass and call
its methods like this:

```javascript
let instance = new MyDerivedClass('Hello, world!');
instance.myMethod();  // Outputs: 'Hello, world!'
instance.anotherMethod();  // Outputs: 'This another method in derived class'
```




## What is metaprogramming and symbols?
Metaprogramming is a programming technique in which computer programs have the ability to treat other programs as their data. It means that a
program can be designed to read, generate, analyze or transform other programs, and even modify itself while running.

In JavaScript, metaprogramming capabilities are significantly enhanced with the introduction of the `Proxy` and `Reflect` objects in ES6, and also
with `Symbols`.

A `Symbol` is a unique and immutable data type introduced in ES6. It can be used as an identifier for object properties. The main purpose of
`Symbols` is to avoid name clashes between properties, since no symbol is equal to another.

Here's an example of using a `Symbol`:

```javascript
let symbol1 = Symbol('symbol');

let obj = {
  [symbol1]: 'value'
};

console.log(obj[symbol1]);  // Outputs: 'value'
```

In this example, `symbol1` is a `Symbol` and can be used as a property key in objects. The value of `obj[symbol1]` is 'value', and this property
can't be accidentally overwritten or accessed without referencing the `symbol1` symbol.
