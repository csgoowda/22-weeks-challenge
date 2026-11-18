
# Day 6 – Object-Oriented Programming (OOP)

**Subject:** Computer Science Fundamentals  
**Topic:** Object-Oriented Programming  
**Language:** Python  
**Study Duration:** 25 Minutes + Practice

---

# PART 1: INTERVIEW PREPARATION

## 1. Expected Interview Questions and Answers

### Q1. What is Object-Oriented Programming (OOP)?

**Answer:**

Object-Oriented Programming (OOP) is a programming approach based on classes and objects. It helps organize code into reusable and manageable components.

OOP improves code reusability, maintainability, modularity and security.

### Q2. What are the four pillars of OOP?

**Answer:**

The four pillars of OOP are:

1. Encapsulation – Combining data and methods inside a class and controlling access to data.
2. Abstraction – Hiding implementation details and showing essential functionality.
3. Inheritance – Reusing properties and methods from an existing class.
4. Polymorphism – Allowing the same interface or method to have different behaviours.

### Q3. What is the difference between a class and an object?

**Answer:**

A class is a blueprint used to create objects, whereas an object is an instance of a class.

For example, `Car` is a class, while a BMW car or Toyota car created from that class is an object.

### Q4. What is a constructor in Python?

**Answer:**

A constructor is used to initialize an object's data when it is created. In Python, `__init__()` is commonly used as the initializer method.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### Q5. What is `self` in Python?

**Answer:**

`self` refers to the current object of a class. It is used to access the attributes and methods belonging to that object.

### Q6. What is encapsulation?

**Answer:**

Encapsulation is the concept of combining data and the methods that operate on that data inside a class while controlling access to it.

For example, a bank account allows users to deposit and withdraw money through methods instead of directly changing the balance.

### Q7. What is abstraction?

**Answer:**

Abstraction means hiding internal implementation details and exposing only the essential functionality.

For example, when driving a car, we use the steering wheel and accelerator without needing to understand the complete internal engine mechanism.

### Q8. What is inheritance?

**Answer:**

Inheritance allows one class to acquire the attributes and methods of another class.

The existing class is called the parent class, and the class that inherits from it is called the child class.

It promotes code reusability.

### Q9. What is polymorphism?

**Answer:**

Polymorphism means one interface can have different behaviours depending on the object.

For example, a `sound()` method can produce different outputs for Dog and Cat objects.

### Q10. What is method overriding?

**Answer:**

Method overriding occurs when a child class provides its own implementation of a method already defined in its parent class.

It is commonly used to achieve runtime polymorphism in Python.

### Q11. What is the difference between abstraction and encapsulation?

**Answer:**

Abstraction hides implementation details and shows only necessary functionality.

Encapsulation combines data and methods inside a class and controls how the data is accessed or modified.

### Q12. What are the different types of inheritance in Python?

**Answer:**

Python supports five commonly discussed types of inheritance:

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

### Q13. What is the difference between an instance method, class method and static method?

**Answer:**

- Instance method works with an individual object's data and takes `self`.
- Class method works with class-level data and takes `cls`. It uses `@classmethod`.
- Static method does not automatically receive `self` or `cls`. It uses `@staticmethod`.

### Q14. Can we create objects without using a constructor?

**Answer:**

Yes. In Python, we can create objects without defining our own `__init__()` method. Python provides a default initializer when one is not defined.

Example:

```python
class Car:
    def start(self):
        print("Car is starting")


car1 = Car()
car1.start()
```

### Q15. Why is OOP useful in real-world applications?

**Answer:**

OOP helps organize large applications into smaller components. It supports code reuse, makes maintenance easier and allows developers to represent real-world entities using classes and objects.

### Q16. How can you use OOP in your OptimalTaskPlanner project?

**Answer:**

I can organize the application using classes such as:

- Machine – Stores machine information and availability.
- Task – Stores task details, processing time and priority.
- Schedule – Manages task assignments and scheduling information.

This structure makes the application modular, reusable and easier to maintain.

---

## 2. Important Follow-up Interview Questions

| Question | Short Answer |
|---|---|
| Is `self` a keyword? | No, it is a conventional parameter name. |
| Is Python an OOP language? | Yes, Python supports OOP and other programming styles. |
| Can a class have multiple objects? | Yes. |
| Can a child class override a parent method? | Yes. |
| Does Python support multiple inheritance? | Yes. |
| What does `super()` do? | It provides access to methods in the parent class according to Python's method resolution order. |
| What is an attribute? | A variable associated with a class or object. |
| What is a method? | A function defined inside a class. |
| What is an instance? | An object created from a class. |
| What is name mangling? | Python transforms names beginning with double underscores inside a class to reduce accidental name clashes. |

## 3. Interview Coding Questions

### Program 1: Create a Class and Object

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


student1 = Student("Chethan", 22)
student1.display()
```

### Program 2: Demonstrate Inheritance

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

### Program 3: Demonstrate Polymorphism

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

### Program 4: Demonstrate Encapsulation

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

### Program 5: Demonstrate Abstraction

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

---

# PART 2: DETAILED OOP NOTES

## 4. Introduction to OOP

OOP stands for Object-Oriented Programming.

It is a programming paradigm in which programs are organized using classes and objects.

An object contains:

- Attributes – Data or properties.
- Methods – Functions or behaviours.

### Real-world example: Car

A car has attributes:

- Brand
- Colour
- Model
- Speed

A car has methods:

- Start
- Stop
- Accelerate
- Brake

We can represent these properties and behaviours using a class.

### Advantages of OOP

1. Code reusability.
2. Easy maintenance.
3. Better organization.
4. Modularity.
5. Data protection through controlled access.
6. Easier expansion of large applications.

---

## 5. Class and Object

### 5.1 Class

A class is a blueprint or template used to create objects.

Example:

```python
class Car:
    brand = "BMW"
    color = "Black"
```

Here, `Car` is the class.

### 5.2 Object

An object is an instance of a class.

Example:

```python
class Car:
    brand = "BMW"
    color = "Black"


car1 = Car()

print(car1.brand)
print(car1.color)
```

Output:

```text
BMW
Black
```

Here:

- `Car` is the class.
- `car1` is the object.
- `brand` and `color` are attributes.

### 5.3 Multiple Objects

We can create multiple objects from one class.

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

Output:

```text
BMW is starting
Toyota is starting
```

Each object stores its own data.

---

## 6. Constructor – `__init__()`

A constructor or initializer is used to initialize object attributes when an object is created.

Python commonly uses the `__init__()` method for this purpose.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Chethan", 22)

print(student1.name)
print(student1.age)
```

Output:

```text
Chethan
22
```

Explanation:

- `__init__()` is called during object initialization.
- `self` refers to the current object.
- `self.name` stores the student's name.
- `self.age` stores the student's age.

### Important point

Python does not require you to define your own `__init__()` method. A class can create objects without explicitly defining one.

---

## 7. Understanding `self`

`self` refers to the current object.

It allows an instance method to access the attributes and other methods of that object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student name:", self.name)


student1 = Student("Chethan")
student2 = Student("Rahul")

student1.display()
student2.display()
```

Output:

```text
Student name: Chethan
Student name: Rahul
```

Important points:

- `self` is not a Python keyword.
- It is the conventional name for the first parameter of an instance method.
- Python automatically supplies the current object when an instance method is called.

---

## 8. Attributes and Methods

### 8.1 Attributes

Attributes are variables that store information about a class or object.

Example:

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
```

Here, `brand` and `price` are instance attributes.

### 8.2 Methods

Methods are functions defined inside a class.

Example:

```python
class Mobile:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(self.brand, "is calling")


phone = Mobile("Samsung")
phone.call()
```

Output:

```text
Samsung is calling
```

---

# 9. Four Pillars of OOP

The four pillars of OOP are:

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

## 9.1 Encapsulation

**Definition:** Encapsulation means combining data and the methods that operate on that data inside a class, while controlling access to the data.

### Real-world example

Consider a bank account.

Users perform operations such as depositing and withdrawing money rather than directly changing the account balance through the banking interface.

### Python example

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

Output:

```text
1500
```

Explanation:

- `__balance` uses a double underscore.
- `deposit()` changes the balance through a method.
- `get_balance()` provides controlled access to the balance.

### Important points

- Combines data and methods.
- Helps control access to data.
- Supports better data organization.
- Python uses naming conventions and name mangling rather than strict private access control.

---

## 9.2 Abstraction

**Definition:** Abstraction means hiding unnecessary implementation details and showing only essential functionality.

### Real-world example

When driving a car:

- You use the steering wheel.
- You press the accelerator.
- You apply the brakes.

You do not need to understand every internal engine operation to drive the car.

### Python example

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

Output:

```text
Car is starting
```

Explanation:

- `ABC` creates an abstract base class.
- `@abstractmethod` declares a method that concrete subclasses must implement.
- `Car` implements the `start()` method.

### Important points

- Hides implementation details.
- Exposes essential functionality.
- Python supports abstraction through the `abc` module.

---

## 9.3 Inheritance

**Definition:** Inheritance allows one class to acquire attributes and methods from another class.

The existing class is called the parent class or base class.

The class that inherits is called the child class or derived class.

### Real-world example

A parent class called `Vehicle` can contain common properties and methods.

Classes such as `Car` and `Bike` can inherit from `Vehicle`.

### Python example

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

Output:

```text
Vehicle is starting
Car is driving
```

Explanation:

- `Vehicle` is the parent class.
- `Car` is the child class.
- `Car` inherits the `start()` method.
- `Car` also defines its own `drive()` method.

### Types of inheritance

**1. Single Inheritance**

One child class inherits from one parent class.

```python
class A:
    pass

class B(A):
    pass
```

**2. Multiple Inheritance**

One child class inherits from multiple parent classes.

```python
class Father:
    def skill1(self):
        print("Gardening")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()
child.skill1()
child.skill2()
```

**3. Multilevel Inheritance**

A class inherits from another child class, forming multiple levels.

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass
```

**4. Hierarchical Inheritance**

Multiple child classes inherit from one parent class.

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass
```

**5. Hybrid Inheritance**

A combination of two or more inheritance types.

---

## 9.4 Polymorphism

**Definition:** Polymorphism means one interface or method name can have different behaviours depending on the object using it.

The word polymorphism means "many forms".

### Real-world example

Different animals make different sounds:

- Dog barks.
- Cat meows.
- Cow moos.

The action is the same, but the behaviour is different.

### Python example

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

Output:

```text
Dog barks
Cat meows
```

Explanation:

- Both classes have a method named `sound()`.
- Each class provides a different implementation.
- This is method overriding.

### Important points

- Polymorphism means many forms.
- The same interface can produce different behaviours.
- Method overriding is a common example of runtime polymorphism in Python.

---

## 10. Difference Between the Four Pillars

| Pillar | Meaning | Example |
|---|---|---|
| Encapsulation | Combine data and methods; control access | Bank account |
| Abstraction | Hide implementation details | Driving a car |
| Inheritance | Reuse features from another class | Car inherits Vehicle |
| Polymorphism | Same interface, different behaviours | Dog and Cat sound |

### Easy way to remember

- Encapsulation – Protect data.
- Abstraction – Hide complexity.
- Inheritance – Reuse code.
- Polymorphism – Different behaviours.

---

## 11. Types of Methods in Python

Python classes commonly use three kinds of methods.

### 11.1 Instance Method

An instance method works with an individual object's data.

It takes `self` as its first parameter.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Chethan")
student.display()
```

### 11.2 Class Method

A class method works with class-level data.

It uses the `@classmethod` decorator and takes `cls` as its first parameter.

```python
class Student:
    college = "SJCE Mysore"

    @classmethod
    def show_college(cls):
        print(cls.college)


Student.show_college()
```

Output:

```text
SJCE Mysore
```

### 11.3 Static Method

A static method does not automatically receive `self` or `cls`.

It uses the `@staticmethod` decorator.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

Output:

```text
30
```

### Difference Between Method Types

| Method | First Parameter | Decorator | Main Use |
|---|---|---|---|
| Instance method | `self` | None | Object data |
| Class method | `cls` | `@classmethod` | Class data |
| Static method | No automatic parameter | `@staticmethod` | Related utility operation |

---

## 12. Class vs Object

| Class | Object |
|---|---|
| Blueprint or template | Instance of a class |
| Defines attributes and methods | Uses attributes and methods |
| One class can create many objects | Each object has its own identity |
| Example: Car | Example: BMW car object |

Example:

```python
class Car:
    pass


car1 = Car()
car2 = Car()
```

Here, `Car` is the class, while `car1` and `car2` are separate objects.

---

# 13. OOP in OptimalTaskPlanner

OptimalTaskPlanner is a production task scheduling application.

OOP helps organize its real-world components.

### 13.1 Machine Class

A machine can contain:

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

### 13.2 Task Class

A task can contain:

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

### 13.3 Schedule Class

A schedule manages tasks assigned to machines.

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

Output:

```text
Cutting
Drilling
```

### Why use OOP in this project?

1. Machine, Task and Schedule are natural real-world entities.
2. Each class has its own responsibility.
3. Code can be reused and maintained easily.
4. New features can be added without putting everything into one large program.
5. It helps organize a growing backend application.

---

# 14. Practice Programs

Complete these programs independently.

### Program 1 – Student Class

Create a `Student` class with:

- Name
- USN
- Marks

Create two objects and display their information.

### Program 2 – Calculator Class

Create a `Calculator` class with methods:

- `add()`
- `subtract()`
- `multiply()`
- `divide()`

### Program 3 – Inheritance

Create a parent class `Vehicle` with a `start()` method.

Create a child class `Bike` with a `ride()` method.

### Program 4 – Polymorphism

Create a parent class `Animal` and child classes `Dog` and `Cat`.

Implement the same `sound()` method differently.

### Program 5 – Bank Account

Create a `BankAccount` class with:

- Private balance attribute using `__balance`.
- `deposit()` method.
- `withdraw()` method.
- `get_balance()` method.

Validate that deposits and withdrawals use positive amounts and that withdrawals do not exceed the balance.

---

# 15. Important Revision Questions

1. What is OOP?
2. What are the advantages of OOP?
3. What is a class?
4. What is an object?
5. What is a constructor?
6. What is `self`?
7. What are attributes and methods?
8. Explain the four pillars of OOP.
9. What is the difference between encapsulation and abstraction?
10. What is inheritance?
11. Explain the five types of inheritance.
12. What is polymorphism?
13. What is method overriding?
14. Explain instance, class and static methods.
15. How can OOP help in a production scheduling application?

---

# 16. Day 6 – CS Fundamentals Completion Checklist

- [ ] Understand what OOP means.
- [ ] Understand class and object.
- [ ] Understand `__init__()`.
- [ ] Understand `self`.
- [ ] Understand attributes and methods.
- [ ] Learn encapsulation.
- [ ] Learn abstraction.
- [ ] Learn inheritance.
- [ ] Learn polymorphism.
- [ ] Understand the difference between the four pillars.
- [ ] Understand instance, class and static methods.
- [ ] Explain how OOP is useful in OptimalTaskPlanner.
- [ ] Complete at least two practice programs.
- [ ] Answer interview questions aloud.

---

# 17. Final Quick Revision

| Concept | Remember |
|---|---|
| OOP | Programming using classes and objects |
| Class | Blueprint |
| Object | Instance of a class |
| `__init__()` | Initializes object data |
| `self` | Current object |
| Attribute | Object or class data |
| Method | Function inside a class |
| Encapsulation | Combine data and methods; control access |
| Abstraction | Hide implementation details |
| Inheritance | Reuse features from a parent class |
| Polymorphism | Same interface, different behaviours |

**Day 6 Learning Outcome:**

You should be able to explain OOP in an interview, create classes and objects in Python, understand its four pillars, write basic OOP programs and explain how classes such as `Machine`, `Task` and `Schedule` can organize your OptimalTaskPlanner project.

---

## GitHub Commit

Save this file as:

`week01/day06_oop_fundamentals.md`

Run these commands from your repository root:

```bash
git add week01/day06_oop_fundamentals.md
git commit -m "Add Day 6 OOP fundamentals interview and study notes"
git push
```
