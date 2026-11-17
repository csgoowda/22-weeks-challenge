# Day 6 – Object-Oriented Programming (OOP)

**Subject:** Computer Science Fundamentals  
**Topic:** Object-Oriented Programming  
**Level:** Beginner to Interview Preparation  
**Language:** Python

---

# PART 1: INTERVIEW PREPARATION

## 1. What is Object-Oriented Programming (OOP)?

**Interview Answer:**

Object-Oriented Programming (OOP) is a programming paradigm based on classes and objects. It combines data and the methods that operate on that data into objects.

OOP helps developers write reusable, organized, maintainable and scalable code.

**Example:** In a banking application, we can create a `BankAccount` class containing account details and methods such as deposit, withdraw and check balance.

**Important points:**
- OOP organizes programs using classes and objects.
- It supports code reusability.
- It improves code organization.
- It makes large applications easier to maintain.
- It has four main pillars.

## 2. What are the four pillars of OOP?

**Interview Answer:**

The four pillars of OOP are:

1. Encapsulation – Combining data and methods inside a class and controlling access to data.
2. Abstraction – Hiding implementation details and exposing essential functionality.
3. Inheritance – Allowing one class to reuse properties and methods from another class.
4. Polymorphism – Allowing the same interface or method name to have different behaviours.

| Pillar | Simple meaning | Example |
|---|---|---|
| Encapsulation | Control access to data | Bank account |
| Abstraction | Hide complexity | Driving a car |
| Inheritance | Reuse code | Car inherits Vehicle |
| Polymorphism | Different behaviours | Dog and Cat sounds |

## 3. What is a class?

**Interview Answer:**

A class is a blueprint or template used to create objects. It defines the attributes and methods that its objects can have.

**Example:**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here, `Student` is a class.

## 4. What is an object?

**Interview Answer:**

An object is an instance of a class. It represents an individual entity with its own data and access to the methods defined by its class.

**Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Chethan")
student2 = Student("Rahul")
```

Here, `student1` and `student2` are two different objects of the `Student` class.

## 5. What is the difference between a class and an object?

| Class | Object |
|---|---|
| Blueprint or template | Instance of a class |
| Defines attributes and methods | Uses attributes and methods |
| Defines the structure | Represents an individual entity |
| Example: Student | Example: student1 |

## 6. What is a constructor in Python?

**Interview Answer:**

A constructor is commonly used to initialize an object's data when it is created. In Python, the `__init__()` method is used as the initializer. It is automatically called when an object is instantiated.

**Example:**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Chethan", 22)

print(student.name)
print(student.age)
```

**Output:**

```text
Chethan
22
```

## 7. What is self in Python?

**Interview Answer:**

`self` refers to the current object of a class. It is used to access the attributes and methods belonging to that object.

**Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Chethan")
student.display()
```

**Output:**

```text
Chethan
```

**Important:** `self` is not a Python keyword. It is the conventional name for the first parameter of an instance method.

## 8. Explain Encapsulation with an example.

**Interview Answer:**

Encapsulation is the process of combining data and the methods that operate on that data within a class while controlling access to the data.

It helps protect data from unintended modification.

**Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())
```

**Output:**

```text
1500
```

**Explanation:**
- `__balance` uses double-underscore name mangling.
- `deposit()` modifies the balance.
- `get_balance()` returns the balance.
- The class controls how its balance is accessed and changed.

## 9. Explain Abstraction with an example.

**Interview Answer:**

Abstraction means hiding internal implementation details and showing only the essential functionality to the user.

For example, when driving a car, we use the steering wheel, accelerator and brakes without needing to understand the internal working of the engine.

**Python Example:**

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting")


car = Car()
car.start()
```

**Output:**

```text
Car is starting
```

**Explanation:**
- `ABC` creates an abstract base class.
- `@abstractmethod` declares an abstract method.
- The child class implements the required method.

## 10. Explain Inheritance with an example.

**Interview Answer:**

Inheritance is an OOP feature that allows a child class to acquire attributes and methods from a parent class.

It promotes code reusability and reduces duplication.

**Python Example:**

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car = Car()

car.start()
car.drive()
```

**Output:**

```text
Vehicle is starting
Car is driving
```

Here:
- `Vehicle` is the parent class.
- `Car` is the child class.
- `Car` inherits the `start()` method.

## 11. What are the types of inheritance?

**Interview Answer:**

Python supports five commonly discussed types of inheritance:

1. Single inheritance – One child class inherits from one parent class.
2. Multiple inheritance – One child class inherits from multiple parent classes.
3. Multilevel inheritance – A class inherits from a class that already inherits from another class.
4. Hierarchical inheritance – Multiple child classes inherit from one parent class.
5. Hybrid inheritance – A combination of multiple inheritance structures.

## 12. Explain Polymorphism with an example.

**Interview Answer:**

Polymorphism means many forms. It allows the same interface or method name to behave differently depending on the object.

In Python, method overriding is a common way to achieve polymorphism.

**Python Example:**

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

Both classes have the same method name but provide different implementations.

## 13. What is method overriding?

**Interview Answer:**

Method overriding occurs when a child class provides its own implementation of a method already defined in its parent class.

It allows a child class to customize inherited behaviour.

## 14. What is the difference between method overloading and method overriding?

| Method Overloading | Method Overriding |
|---|---|
| Same method name with different parameter combinations | Child class redefines a parent method |
| Common in languages such as Java and C++ | Supported in Python |
| Python does not support traditional signature-based overloading directly | Python supports method overriding |
| Can be simulated using default arguments or `*args` | Achieved through inheritance |

## 15. What are the different types of methods in Python?

**Interview Answer:**

Python classes commonly have three types of methods:

1. Instance methods – Work with individual object data using `self`.
2. Class methods – Work with class-level data using `cls`.
3. Static methods – Utility methods that do not automatically receive `self` or `cls`.

**Example:**

```python
class Student:
    college = "SJCE Mysore"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display(self):
        print(self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print(cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Python OOP")


student = Student("Chethan")

student.display()
Student.show_college()
Student.welcome()
```

**Output:**

```text
Chethan
SJCE Mysore
Welcome to Python OOP
```

## 16. What is the difference between an instance method, class method and static method?

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | Not required | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | No automatic first parameter |
| Access object data | Yes | Through class or object reference | Only if passed explicitly |
| Access class data | Yes | Yes | Only if passed explicitly |
| Main purpose | Object operations | Class-level operations | Utility operations |

## 17. What is the difference between abstraction and encapsulation?

**Interview Answer:**

Abstraction focuses on hiding implementation details and showing essential functionality.

Encapsulation focuses on combining data and methods within a class and controlling access to that data.

**Example:**
- Abstraction: Using a car's steering wheel without understanding the engine.
- Encapsulation: Controlling access to a bank account balance.

## 18. Why is OOP important in real-world projects?

**Interview Answer:**

OOP is important because it helps developers divide large applications into manageable components.

It improves code reusability, maintainability, organization and scalability.

For example, in a production scheduling application, we can create separate classes for machines, tasks and schedules.

## 19. How can OOP be used in your OptimalTaskPlanner project?

**Interview Answer:**

In OptimalTaskPlanner, OOP can represent real-world manufacturing entities.

- `Machine` class stores machine information and availability.
- `Task` class stores task details, processing time and priority.
- `Schedule` class manages task assignments and scheduling operations.

This structure makes the application easier to maintain, extend and test.

## 20. Does Python support multiple inheritance?

**Interview Answer:**

Yes. Python supports multiple inheritance, which means a child class can inherit from more than one parent class.

**Example:**

```python
class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills()
child.talent()
```

**Output:**

```text
Gardening
Cooking
```

## 21. What is the difference between public, protected and private members in Python?

**Interview Answer:**

Python uses naming conventions and name mangling to indicate access levels.

| Type | Naming | Meaning |
|---|---|---|
| Public | `name` | Intended for general access |
| Protected | `_name` | Conventionally intended for internal or subclass use |
| Private | `__name` | Triggers name mangling to reduce accidental access |

Python does not enforce strict private or protected access in the same way as some other languages.

## 22. Expected Interview Follow-up Questions

1. Can we create multiple objects from one class?
   - Yes, one class can create many independent objects.

2. Can a child class have its own methods?
   - Yes, a child class can define additional methods.

3. Can a child class override a parent method?
   - Yes, it can provide its own implementation.

4. Is `self` mandatory as a name?
   - No, but it is the standard Python convention for the first parameter of an instance method.

5. Is `__init__()` mandatory in every class?
   - No, Python can use a default initializer when a class does not define its own.

6. Can an abstract class contain normal methods?
   - Yes, it can contain both abstract and concrete methods.

7. Can we create an object of an abstract class containing an unimplemented abstract method?
   - No, Python prevents instantiation until the required abstract methods are implemented.

8. What is code reusability?
   - Using existing code in different parts of an application instead of rewriting it.

9. What is the purpose of `super()`?
   - It provides a way to access methods from the next class in the method resolution order, commonly used to call parent-class methods.

10. What is the difference between an attribute and a method?
    - An attribute stores data; a method defines behaviour.

---

# PART 2: NORMAL DETAILED NOTES

## 1. Introduction to OOP

Object-Oriented Programming (OOP) is a programming approach in which programs are organized using classes and objects.

Every object can contain:

- Attributes – Data or properties.
- Methods – Functions or behaviours.

### Real-world example: Car

A car has attributes:
- Brand
- Model
- Colour
- Speed

A car has methods:
- Start
- Stop
- Accelerate
- Brake

OOP allows us to represent these real-world entities in a program.

### Advantages of OOP

1. Reusability – Reuse existing code.
2. Maintainability – Easier to modify and update.
3. Modularity – Divide large programs into smaller components.
4. Security – Control access to data.
5. Scalability – Organize applications as they grow.

---

## 2. Classes and Objects

### Class

A class is a blueprint used to create objects.

```python
class Car:
    brand = "BMW"
    color = "Black"
```

### Object

An object is an instance of a class.

```python
class Car:
    brand = "BMW"
    color = "Black"


car1 = Car()

print(car1.brand)
print(car1.color)
```

**Output:**

```text
BMW
Black
```

### Multiple objects

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "is starting")


car1 = Car("BMW", "Black")
car2 = Car("Toyota", "White")

car1.start()
car2.start()
```

**Output:**

```text
BMW is starting
Toyota is starting
```

Each object can have its own attribute values.

---

## 3. Constructor – `__init__()`

`__init__()` is a special initializer method used to set up an object's initial attributes.

It is automatically called when an object is created.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Chethan", 22)

print(student1.name)
print(student1.age)
```

**Output:**

```text
Chethan
22
```

### Important points

- `__init__()` initializes object attributes.
- It is called during object creation.
- It can accept parameters.
- It commonly uses `self` to assign instance attributes.

---

## 4. Understanding self

`self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)


student1 = Student("Chethan")
student2 = Student("Rahul")

student1.display()
student2.display()
```

**Output:**

```text
Student: Chethan
Student: Rahul
```

The `self.name` attribute belongs to the individual object.

---

## 5. Attributes and Methods

### Attributes

Attributes are variables associated with a class or object.

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
```

### Methods

Methods are functions defined inside a class.

```python
class Mobile:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(self.brand, "is calling")


phone = Mobile("Samsung")
phone.call()
```

**Output:**

```text
Samsung is calling
```

---

## 6. Four Pillars of OOP

### 6.1 Encapsulation

Encapsulation means combining data and methods inside a class and controlling access to the data.

**Real-world example:** Bank account.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance())
```

**Output:**

```text
1300
```

**Important concepts:**
- Encapsulation combines data and methods.
- It helps control access to internal data.
- Double underscore triggers name mangling.
- Access should be provided through suitable methods or properties.

### 6.2 Abstraction

Abstraction means hiding unnecessary implementation details and showing essential functionality.

**Real-world example:** Driving a car without understanding all the internal engine operations.

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting")


car = Car()
car.start()
```

**Output:**

```text
Car is starting
```

**Important concepts:**
- `ABC` is an abstract base class.
- `@abstractmethod` declares an abstract method.
- Child classes implement required abstract methods.
- An abstract class with unimplemented abstract methods cannot be instantiated.

### 6.3 Inheritance

Inheritance allows one class to reuse the attributes and methods of another class.

**Example:**

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car = Car()

car.start()
car.drive()
```

**Output:**

```text
Vehicle is starting
Car is driving
```

### Types of inheritance

**1. Single inheritance**

One child class inherits from one parent class.

```python
class Parent:
    def display(self):
        print("Parent class")


class Child(Parent):
    pass


obj = Child()
obj.display()
```

**2. Multiple inheritance**

One child class inherits from multiple parent classes.

```python
class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


obj = Child()

obj.skills()
obj.talent()
```

**3. Multilevel inheritance**

A class inherits from a class that already inherits from another class.

```python
class Grandparent:
    def display1(self):
        print("Grandparent")


class Parent(Grandparent):
    def display2(self):
        print("Parent")


class Child(Parent):
    def display3(self):
        print("Child")


obj = Child()

obj.display1()
obj.display2()
obj.display3()
```

**4. Hierarchical inheritance**

Multiple child classes inherit from one parent class.

```python
class Vehicle:
    def start(self):
        print("Vehicle starting")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


car = Car()
bike = Bike()

car.start()
bike.start()
```

**5. Hybrid inheritance**

Hybrid inheritance combines two or more inheritance structures.

### 6.4 Polymorphism

Polymorphism means many forms.

It allows the same method or interface to behave differently for different objects.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

**Important concepts:**
- Same method name.
- Different implementations.
- Method overriding is a common example.

---

## 7. Types of Methods in Python

### Instance Method

Uses `self` and works with object data.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Chethan")
student.display()
```

### Class Method

Uses `cls` and works with class-level data.

```python
class Student:
    college = "SJCE Mysore"

    @classmethod
    def show_college(cls):
        print(cls.college)


Student.show_college()
```

### Static Method

Does not automatically receive `self` or `cls`.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

**Output:**

```text
30
```

---

## 8. Access Modifiers in Python

Python uses naming conventions to indicate intended access.

| Type | Example | Meaning |
|---|---|---|
| Public | `name` | General access |
| Protected | `_name` | Intended for internal or subclass use |
| Private | `__name` | Name mangling to avoid accidental access |

Example:

```python
class Employee:
    def __init__(self):
        self.name = "Chethan"
        self._department = "IT"
        self.__salary = 30000


employee = Employee()

print(employee.name)
print(employee._department)
```

The double-underscore attribute is name-mangled. It is not completely inaccessible, but direct access using its original name is not available in the usual way.

---

## 9. Difference Between Abstraction and Encapsulation

| Abstraction | Encapsulation |
|---|---|
| Hides implementation details | Combines data and methods |
| Focuses on essential functionality | Focuses on controlling data access |
| Uses abstract classes and interfaces | Uses classes, methods and access conventions |
| Example: Car controls | Example: Bank account balance |

---

## 10. OOP in OptimalTaskPlanner

OOP is useful in your manufacturing scheduling project because the project contains real-world entities.

### Machine class

Stores:
- Machine ID
- Machine name
- Capacity
- Availability

```python
class Machine:
    def __init__(self, machine_id, name, capacity):
        self.machine_id = machine_id
        self.name = name
        self.capacity = capacity

    def display(self):
        print(self.machine_id, self.name, self.capacity)


machine1 = Machine(1, "CNC Machine", 8)

machine1.display()
```

### Task class

Stores:
- Task ID
- Task name
- Processing time
- Priority

```python
class Task:
    def __init__(self, task_id, name, processing_time, priority):
        self.task_id = task_id
        self.name = name
        self.processing_time = processing_time
        self.priority = priority

    def display(self):
        print(self.name, self.processing_time, self.priority)


task1 = Task(101, "Cutting", 3, "High")

task1.display()
```

### Schedule class

Manages tasks.

```python
class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task.name)


task1 = Task(101, "Cutting", 3, "High")
task2 = Task(102, "Drilling", 2, "Medium")

schedule = Schedule()

schedule.add_task(task1)
schedule.add_task(task2)

schedule.show_tasks()
```

**Output:**

```text
Cutting
Drilling
```

### Benefits in the project

1. Separate responsibilities for machines, tasks and schedules.
2. Easier testing and debugging.
3. Better code organization.
4. Reusable components.
5. Easier to add new scheduling features.

---

# PART 3: PRACTICE PROGRAMS

## Program 1 – Student Class

**Task:** Create a Student class with name, USN and marks. Create two objects and display their details.

```python
class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks:", self.marks)


student1 = Student("Chethan", "ISE101", 85)
student2 = Student("Rahul", "ISE102", 90)

student1.display()
student2.display()
```

## Program 2 – Calculator Class

**Task:** Create a calculator class with addition, subtraction, multiplication and division.

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calc = Calculator()

print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))
```

## Program 3 – Inheritance

**Task:** Create a Vehicle parent class and a Bike child class.

```python
class Vehicle:
    def start(self):
        print("Vehicle started")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


bike = Bike()

bike.start()
bike.ride()
```

## Program 4 – Polymorphism

**Task:** Create Animal, Dog and Cat classes with different sound methods.

```python
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

## Program 5 – Bank Account

**Task:** Create a bank account with deposit, withdrawal and balance checking.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print("Balance:", account.get_balance())
```

**Output:**

```text
Balance: 4000
```

---

# PART 4: QUICK REVISION

## Important Definitions

| Concept | Definition |
|---|---|
| OOP | Programming paradigm based on classes and objects |
| Class | Blueprint used to create objects |
| Object | Instance of a class |
| Constructor | Initializer used to set up object data |
| `self` | Reference to the current object |
| Attribute | Data associated with a class or object |
| Method | Function defined inside a class |
| Encapsulation | Combining data and methods and controlling access |
| Abstraction | Hiding implementation details |
| Inheritance | Reusing features from another class |
| Polymorphism | Same interface with different behaviours |
| Overriding | Redefining a parent method in a child class |

## Four Pillars – One-Line Revision

- Encapsulation – Protect and control access to data.
- Abstraction – Hide internal complexity.
- Inheritance – Reuse existing code.
- Polymorphism – Same interface, different behaviour.

## Day 6 CS Fundamentals Checklist

- [ ] Understand OOP.
- [ ] Understand class and object.
- [ ] Understand `__init__()`.
- [ ] Understand `self`.
- [ ] Understand attributes and methods.
- [ ] Learn encapsulation.
- [ ] Learn abstraction.
- [ ] Learn inheritance.
- [ ] Learn polymorphism.
- [ ] Understand types of inheritance.
- [ ] Understand instance, class and static methods.
- [ ] Understand access conventions.
- [ ] Complete at least two practice programs.
- [ ] Prepare answers for interview questions.
- [ ] Explain how OOP applies to OptimalTaskPlanner.

---

# PART 5: FINAL SELF-ASSESSMENT

Before marking this topic complete, make sure you can answer these questions without looking at the notes.

1. What is OOP?
2. What is the difference between a class and an object?
3. What is the purpose of `__init__()`?
4. What is `self`?
5. Explain all four pillars of OOP.
6. What is the difference between abstraction and encapsulation?
7. Explain inheritance and its types.
8. What is method overriding?
9. What is the difference between instance, class and static methods?
10. How can OOP help in a manufacturing scheduling application?

**Expected learning outcome:**

You should be able to create Python classes and objects, explain the four pillars of OOP, write basic inheritance and polymorphism programs, and confidently answer common fresher interview questions about OOP.

**GitHub commit message:**

```bash
git add week01/day06_oop_fundamentals.md
git commit -m "Add OOP fundamentals and interview preparation notes"
git push
```
