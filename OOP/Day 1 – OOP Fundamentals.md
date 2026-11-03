Great! Let's move to the next topic in your Day 1 roadmap.

# Day 1 – OOP Fundamentals

30 minutes

Beginner level

Today's topics:

1. What is OOP?
2. What is a class?
3. What is an object?
4. What are attributes?
5. What are methods?
6. Create a `Machine` class and two objects.

## 1. What is OOP?

OOP stands for Object-Oriented Programming.

It is a programming approach that organizes code around objects, which combine data and functionality.

OOP helps us:

- Organize code.
- Reuse code.
- Represent real-world entities.
- Make large applications easier to maintain.

For example, in manufacturing software, we might represent machines, employees, production orders and products as objects.

## 2. What is a class?

A class is a blueprint or template used to create objects.

Think about a manufacturing company.

A company has a general machine design with properties such as:

- Machine name
- Machine capacity
- Machine status

We can define a class called `Machine`.

```
class Machine:    pass
```

Here:

- `class` is a Python keyword.
- `Machine` is the class name.
- `pass` means no implementation is added yet.

## 3. What is an object?

An object is an instance of a class.

A class is the blueprint. Objects are the individual instances created from that blueprint.

For example:

[Sample Animated Lesson Videos – Imagnica](https://images.openai.com/static-rsc-4/nH8hm5bBC3XjDKK4X7CYd2fsgxvM-D2EqBPvWX4XXHhHvaDwhENYmOWWB0PMCp9Y31V-T3Ds9AI1Q8AbXgd7dfCDznnR1nLim7tNFzbJN69XB7A_AEAHasOb-nS8NckaYqkPyrj6z6ofOqIjH-ICnbeVQf1tqTkN5TYFA4B3lMk?purpose=inline)

Imagine a `Machine` class with two objects:

- CNC Machine
- Drilling Machine

Both follow the same class structure, but each can have different values.

## 4. What are attributes?

Attributes are variables that belong to an object or class. They represent an object's data or properties.

Example:

```
class Machine:    def __init__(self, name, capacity):        self.name = name        self.capacity = capacity
```

Here:

- `name` represents the machine name.
- `capacity` represents its production capacity.
- `self.name` and `self.capacity` store these values on the object.
- `__init__()` initializes the object when it is created.

Don't worry if `self` looks confusing. We'll practise it.

## 5. What are methods?

Methods are functions defined inside a class. They represent actions that an object can perform.

Example:

```
class Machine:    def __init__(self, name, capacity):        self.name = name        self.capacity = capacity    def display_details(self):        print("Machine:", self.name)        print("Capacity:", self.capacity)
```

Here, `display_details()` is a method.

It displays the machine's information.

## 6. Complete example: Machine class with two objects

Study this carefully:

```
class Machine:    # Constructor    def __init__(self, name, capacity):        self.name = name        self.capacity = capacity    # Method    def display_details(self):        print("Machine:", self.name)        print("Capacity:", self.capacity)# Creating first objectmachine1 = Machine("CNC Machine", 500)# Creating second objectmachine2 = Machine("Drilling Machine", 300)# Calling methodsmachine1.display_details()machine2.display_details()
```

Output:

```
Machine: CNC Machine
Capacity: 500

Machine: Drilling Machine
Capacity: 300
```

### Understand the important parts

| Code                | Meaning                      |
| ------------------- | ---------------------------- |
| `class Machine`     | Creates a class              |
| `__init__()`        | Initializes a new object     |
| `self`              | Refers to the current object |
| `self.name`         | Object attribute             |
| `display_details()` | Method                       |
| `machine1`          | First object                 |
| `machine2`          | Second object                |

### Class versus object

| Class             | Object                 |
| ----------------- | ---------------------- |
| Blueprint         | Instance of a class    |
| Defines structure | Contains actual values |
| `Machine`         | `machine1`             |
| `Machine`         | `machine2`             |

## 7. Your practical exercise

Create a Python file named `machine_oop.py`.

Your task:

1. Create a class named `Machine`.
2. Add two attributes: `name` and `capacity`.
3. Add a method called `display_details()`.
4. Create two objects with different machine names and capacities.
5. Call the method for both objects.

Try writing the code yourself without copying the complete example.

## 8. Test your understanding

OOP knowledge test

Q1. What is OOP?

A. Operating Output Program

B. Object-Oriented Programming

C. Object Operating Process

D. Only Object Programming



Q2. What is a class?

A. A blueprint for creating objects

B. A variable

C. A loop

D. A data type



Q3. What is an object?

A. A programming language

B. An instance of a class

C. A comment

D. A method



Q4. What are attributes?

A. Actions

B. Loops

C. Data or properties belonging to an object or class

D. Comments



Q5. What are methods?

A. Functions defined inside a class

B. Only variables

C. Data types

D. Comments



0/5 answered

Submit answers

One important thing: We still have the DSA quiz pending. We can return to it after this OOP lesson. Once your practical and quiz are verified, we'll move to aptitude and English.
