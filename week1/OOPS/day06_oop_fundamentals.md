# Day 6 – CS Fundamentals: Object-Oriented Programming (OOP)

## 1. What is OOP?

OOP stands for **Object-Oriented Programming**.

It is a programming approach in which we organize programs using classes and objects.

Instead of writing all the code in one place, we divide the program into smaller parts called objects.

Each object can contain:
- Data (attributes or properties)
- Functions (methods or behaviours)

### Real-world example

Consider a car.

A car has data:
- Brand
- Colour
- Model
- Speed

A car also has behaviours:
- Start
- Stop
- Accelerate
- Brake

In OOP, we can represent a car using a class and create different car objects from it.

### Advantages of OOP

1. Code reusability.
2. Easy to maintain and update.
3. Better code organization.
4. Data protection through encapsulation.
5. Useful for building large applications.
6. Reduces repeated code.

---

## 2. Class and Object

### What is a class?

A **class** is a blueprint or template used to create objects.

It defines the properties and methods that its objects can have.

Example:

```python
class Car:
    brand = "BMW"
    color = "Black"
```

Here, `Car` is a class.

### What is an object?

An **object** is an instance of a class.

We create objects using the class name.

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

### Creating multiple objects

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

Each object has its own attribute values.

---

## 3. Constructor – `__init__()`

A constructor is a special method that initializes an object's attributes when the object is created.

In Python, we commonly use `__init__()` as the initializer.

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

- `__init__()` runs when an object is created.
- `self` refers to the current object.
- `self.name` stores the name in that object.
- `self.age` stores the age in that object.

---

## 4. What is `self` in Python?

`self` refers to the current object.

It allows us to access the attributes and methods belonging to that object.

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
- Python passes the current object automatically when an instance method is called.

---

## 5. Attributes and Methods

### Attributes

Attributes are variables that store information about an object.

Example:

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
```

Here:
- `brand` is an attribute.
- `price` is an attribute.

### Methods

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

# 6. Four Pillars of OOP

The four main pillars of Object-Oriented Programming are:

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

## 6.1 Encapsulation

**Definition:** Encapsulation means combining data and the methods that operate on that data inside a class, while controlling how the data is accessed or modified.

### Real-world example

Consider a bank account.

You cannot change your bank balance directly through the bank's interface. You use operations such as deposit and withdrawal.

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

- `__balance` uses a double underscore for name mangling.
- `deposit()` changes the balance through a method.
- `get_balance()` provides access to the balance.

### Important points

- Encapsulation combines data and methods.
- It helps control access to data.
- Python uses naming conventions and name mangling rather than strict private access control.

---

## 6.2 Abstraction

**Definition:** Abstraction means hiding unnecessary implementation details and showing only the essential functionality to the user.

### Real-world example

When you drive a car:
- You use the steering wheel.
- You press the accelerator.
- You apply the brakes.

You do not need to understand every internal engine operation to drive the car.

### Python example using an abstract class

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

- `ABC` is used to create an abstract base class.
- `@abstractmethod` declares a method that subclasses must implement.
- `Car` implements the `start()` method.

Important points:

- Abstraction hides implementation details.
- It exposes essential operations.
- Python supports abstraction through the `abc` module.

---

## 6.3 Inheritance

**Definition:** Inheritance allows one class to acquire attributes and methods from another class.

The class being inherited from is called the **parent class** or **base class**.

The class that inherits is called the **child class** or **derived class**.

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
- `Car` also has its own `drive()` method.

### Types of inheritance

1. **Single inheritance:** One child class inherits from one parent class.
2. **Multiple inheritance:** One child class inherits from multiple parent classes.
3. **Multilevel inheritance:** A class inherits from a child class, forming multiple levels.
4. **Hierarchical inheritance:** Multiple child classes inherit from one parent class.
5. **Hybrid inheritance:** A combination of inheritance types.

---

## 6.4 Polymorphism

**Definition:** Polymorphism means one interface or method name can have different behaviours depending on the object using it.

The word polymorphism means "many forms".

### Real-world example

Different animals make different sounds.

- Dog barks.
- Cat meows.
- Cow moos.

The action is the same (`sound`), but the behaviour is different.

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
- This is method overriding, a common way to achieve runtime polymorphism in Python.

### Important points

- Polymorphism means many forms.
- The same method name can produce different behaviours.
- Method overriding is one example of polymorphism.

---

# 7. Difference Between the Four Pillars

| Pillar | Meaning | Example |
|---|---|---|
| Encapsulation | Combining data and methods and controlling access | Bank account |
| Abstraction | Hiding implementation details | Driving a car |
| Inheritance | Reusing features from another class | Car inherits Vehicle |
| Polymorphism | Same interface, different behaviours | Dog and Cat sound |

### Easy way to remember

- Encapsulation – Protect data.
- Abstraction – Hide complexity.
- Inheritance – Reuse code.
- Polymorphism – Different behaviours.

---

# 8. Types of Methods in Python

Python classes commonly use three kinds of methods.

## 8.1 Instance Method

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

## 8.2 Class Method

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

## 8.3 Static Method

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

---

# 9. Class vs Object

| Class | Object |
|---|---|
| Blueprint or template | Instance of a class |
| Defines attributes and methods | Uses the attributes and methods |
| Logical definition | Created in memory at runtime |
| Example: Car | Example: BMW car object |

Example:

```python
class Car:
    pass


car1 = Car()
car2 = Car()
```

Here, `Car` is the class, while `car1` and `car2` are two different objects.

---

# 10. How OOP Is Used in OptimalTaskPlanner

Your flagship project, **OptimalTaskPlanner**, is a production task scheduling application.

OOP helps organize its real-world components.

### Example 1 – Machine class

A machine contains:
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

### Example 2 – Task class

A task contains:
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

### Example 3 – Schedule class

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
2. Each class has its own responsibilities.
3. Code can be reused and maintained easily.
4. New machine or task features can be added without putting everything into one large program.
5. It helps organize a growing backend application.

---

# 11. Important Interview Questions

### Q1. What is OOP?

OOP is a programming approach based on classes and objects.

### Q2. What is a class?

A class is a blueprint used to create objects.

### Q3. What is an object?

An object is an instance of a class.

### Q4. What is a constructor?

A constructor or initializer sets up an object's initial data. In Python, `__init__()` is commonly used for this.

### Q5. What is self?

`self` refers to the current object.

### Q6. What are the four pillars of OOP?

Encapsulation, abstraction, inheritance and polymorphism.

### Q7. What is inheritance?

Inheritance allows one class to reuse attributes and methods from another class.

### Q8. What is polymorphism?

Polymorphism allows the same method or interface to behave differently for different objects.

### Q9. What is encapsulation?

Encapsulation combines data and methods inside a class and controls access to the data.

### Q10. What is abstraction?

Abstraction hides implementation details and exposes essential functionality.

### Q11. What is method overriding?

Method overriding happens when a child class provides its own implementation of a method inherited from its parent class.

### Q12. Why is OOP useful?

OOP improves code organization, reuse, maintainability and modularity.

---

# 12. Practice Programs

Complete these programs without copying the examples.

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

# 13. Day 6 CS Fundamentals – Revision Checklist

- [ ] Understand what OOP means.
- [ ] Understand class and object.
- [ ] Understand constructor `__init__()`.
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
- [ ] Answer the interview questions aloud.

---

# 14. Final Quick Revision

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

**Day 6 learning outcome:** You should be able to explain OOP, create classes and objects in Python, understand its four pillars, and explain how classes such as `Machine`, `Task` and `Schedule` can organize your OptimalTaskPlanner project.
