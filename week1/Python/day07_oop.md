
# Day 7 – Python Object-Oriented Programming (OOP)

**Week:** 1  
**Topic:** Classes, Inheritance, Encapsulation and Polymorphism  
**Project Connection:** OptimalTaskPlanner – Factory Machine and Task Domain Model  
**Main File:** `week01/day07_oop.py`

---

# PART 1: INTERVIEW PREPARATION

## 1. What is Object-Oriented Programming (OOP)?

**Answer:**

Object-Oriented Programming is a programming approach that organizes code using classes and objects. It helps us structure programs, reuse code, manage data and build maintainable applications.

For example, in a factory management system, we can create classes such as Machine, Task and Schedule.

## 2. What is a class?

**Answer:**

A class is a blueprint or template used to create objects. It defines the attributes and methods that its objects can have.

Example:

```python
class Machine:
    pass
```

## 3. What is an object?

**Answer:**

An object is an instance of a class. It contains its own data and can use the methods defined in its class.

Example:

```python
class Machine:
    pass

machine1 = Machine()
machine2 = Machine()
```

Here, `machine1` and `machine2` are two different objects.

## 4. What is the difference between a class and an object?

| Class | Object |
|---|---|
| Blueprint or template | Instance of a class |
| Defines attributes and methods | Contains actual data |
| Created using `class` | Created by calling the class |
| Example: Machine | Example: CNC-01 |

## 5. What is `__init__()`?

**Answer:**

`__init__()` is a special method that initializes an object's attributes when an object is created.

Example:

```python
class Machine:

    def __init__(self, name):
        self.name = name
```

## 6. What is `self`?

**Answer:**

`self` refers to the current object. It allows us to access that object's attributes and methods inside the class.

Example:

```python
self.name = name
```

This stores the name in the current object.

## 7. What is inheritance?

**Answer:**

Inheritance is an OOP feature that allows a child class to reuse attributes and methods from a parent class.

For example, CNCMachine and LatheMachine can inherit common properties from the Machine class.

## 8. What is `super()`?

**Answer:**

`super()` allows a child class to access methods from its parent class.

We commonly use `super().__init__()` to initialize the attributes defined in the parent constructor.

## 9. What is encapsulation?

**Answer:**

Encapsulation combines data and related methods inside a class and provides controlled ways to access or modify that data.

For example, we can validate machine capacity before allowing it to change.

## 10. What is a protected attribute in Python?

**Answer:**

An attribute beginning with a single underscore, such as `_capacity`, is conventionally intended for internal use.

Python does not strictly prevent external access to a single-underscore attribute.

## 11. What is `@property`?

**Answer:**

The `@property` decorator allows us to access a method like an attribute.

Example:

```python
@property
def capacity(self):
    return self._capacity
```

We can access it using:

```python
machine.capacity
```

## 12. What is a setter?

**Answer:**

A setter allows us to control how a property is updated. We can validate the new value before storing it.

Example:

```python
@capacity.setter
def capacity(self, value):
    if value <= 0:
        raise ValueError("Capacity must be greater than 0")

    self._capacity = value
```

## 13. What is polymorphism?

**Answer:**

Polymorphism means one interface can have many forms.

Different classes can have a method with the same name but different implementations.

For example, CNCMachine and LatheMachine can both have a `describe()` method that returns different descriptions.

## 14. What is method overriding?

**Answer:**

Method overriding occurs when a child class provides its own implementation of a method inherited from its parent class.

## 15. What is the difference between inheritance and composition?

| Inheritance | Composition |
|---|---|
| Represents an is-a relationship | Represents a has-a relationship |
| Child reuses parent functionality | One object contains or uses another object |
| CNCMachine is a Machine | Schedule has Tasks |
| Uses parent class inheritance | Uses object references |

Prefer composition when objects have a has-a relationship or when a deep inheritance hierarchy would make the design difficult to maintain.

## 16. What is the difference between overriding and overloading?

**Overriding:** A subclass provides its own implementation of an inherited method.

**Overloading:** Using the same method name with different parameter lists.

Python does not directly support traditional method overloading by defining multiple methods with the same name. The latest definition replaces the earlier one. Alternatives include default arguments, `*args` and `functools.singledispatch`.

## 17. Why should we call `super().__init__()`?

It allows the parent class to initialize its own attributes. Without it, the child object may not have the attributes expected from the parent class.

## 18. What are instance attributes and class attributes?

**Instance attributes:** Belong to individual objects.

**Class attributes:** Are defined in the class body and shared through the class unless overridden on an instance.

## 19. What is the difference between `__str__()` and `__repr__()`?

- `__str__()` provides a readable representation intended for users.
- `__repr__()` provides a developer-oriented representation.

## 20. How is OOP useful in your OptimalTaskPlanner project?

We can model factory components using classes:

- Machine: stores machine details and behaviour.
- CNCMachine: represents a CNC machine.
- LatheMachine: represents a lathe machine.
- Task: stores task details, duration and priority.
- Schedule: can contain a collection of tasks.

Inheritance helps reuse machine functionality, encapsulation helps validate data, and polymorphism allows different machines to implement common operations differently.

---

# PART 2: DETAILED PYTHON OOP NOTES

## 1. Introduction to OOP

OOP organizes software around classes and objects.

Instead of writing all the program logic in separate functions, we can organize related data and behaviour inside classes.

### Real-world example

Consider a manufacturing factory.

A machine has:

- Name
- Capacity per hour
- Availability

A task has:

- Name
- Duration
- Priority

These can be represented using Python classes.

### Benefits of OOP

1. Code reusability.
2. Better organization.
3. Easier maintenance.
4. Data validation.
5. Easier extension of applications.
6. Better representation of real-world entities.

## 2. Creating a Class

Syntax:

```python
class ClassName:
    pass
```

Example:

```python
class Machine:
    pass
```

Here:

- `class` is the Python keyword.
- `Machine` is the class name.
- `pass` indicates an empty class body.

## 3. Creating Objects

An object is created by calling its class.

```python
class Machine:
    pass


machine1 = Machine()
machine2 = Machine()

print(machine1)
print(machine2)
```

Both variables refer to separate Machine instances.

## 4. Constructor – `__init__()`

The `__init__()` method initializes the object after it is created.

Example:

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


machine1 = Machine("CNC-01", 50)
machine2 = Machine("LATHE-01", 30)

print(machine1.name)
print(machine2.name)
```

Output:

```text
CNC-01
LATHE-01
```

### Understand the constructor

```python
def __init__(self, name, capacity):
```

Accepts the values supplied when creating an object.

```python
self.name = name
```

Stores the supplied name in the current object.

```python
self.capacity = capacity
```

Stores the supplied capacity in the current object.

**Important:** `__init__()` is an initializer, not technically the method that creates the object. Python creates the object before calling it.

## 5. Understanding `self`

`self` represents the current instance.

Example:

```python
class Machine:

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(self.name)


machine1 = Machine("CNC-01")
machine2 = Machine("LATHE-01")

machine1.describe()
machine2.describe()
```

Output:

```text
CNC-01
LATHE-01
```

When `machine1.describe()` is called, `self` refers to `machine1`.

When `machine2.describe()` is called, `self` refers to `machine2`.

## 6. Instance Attributes vs Class Attributes

### Instance attributes

Each object can have its own values.

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


m1 = Machine("CNC-01", 50)
m2 = Machine("LATHE-01", 30)

print(m1.capacity)
print(m2.capacity)
```

Output:

```text
50
30
```

### Class attributes

A class attribute is defined directly inside the class body.

```python
class Machine:

    category = "Manufacturing Equipment"

    def __init__(self, name):
        self.name = name


m1 = Machine("CNC-01")
m2 = Machine("LATHE-01")

print(m1.category)
print(m2.category)
```

Output:

```text
Manufacturing Equipment
Manufacturing Equipment
```

### Important difference

Use instance attributes for data that differs between objects.

Use class attributes for data shared by instances.

Avoid modifying mutable class attributes unintentionally because objects can share the same mutable value.

## 7. Understanding `__str__()` and `__repr__()`

These are special methods used to represent objects as strings.

### `__str__()`

```python
class Machine:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Machine name: {self.name}"


machine = Machine("CNC-01")

print(machine)
```

Output:

```text
Machine name: CNC-01
```

### `__repr__()`

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return (
            f"Machine(name={self.name!r}, "
            f"capacity={self.capacity})"
        )


machine = Machine("CNC-01", 50)

print(repr(machine))
```

Output:

```text
Machine(name='CNC-01', capacity=50)
```

For Day 7, your required `Machine` class must implement `__repr__()`.

---

# PART 3: THE FOUR PILLARS OF OOP

## 8. Inheritance

Inheritance allows a child class to reuse attributes and methods from a parent class.

### Factory example

- Machine: Parent class.
- CNCMachine: Child class.
- LatheMachine: Child class.

### Basic syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

### Practical example

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class CNCMachine(Machine):
    pass


class LatheMachine(Machine):
    pass


cnc = CNCMachine("CNC-01", 50)
lathe = LatheMachine("LATHE-01", 30)

print(cnc.name)
print(lathe.name)
```

Output:

```text
CNC-01
LATHE-01
```

Both subclasses inherit the constructor and attributes from Machine.

## 9. Understanding `super()`

`super()` allows a subclass to call a method from its parent class.

Example:

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class CNCMachine(Machine):

    def __init__(self, name, capacity, tool_type):
        super().__init__(name, capacity)
        self.tool_type = tool_type


cnc = CNCMachine("CNC-01", 50, "Milling")

print(cnc.name)
print(cnc.capacity)
print(cnc.tool_type)
```

Output:

```text
CNC-01
50
Milling
```

`super().__init__(name, capacity)` calls the parent constructor.

This prevents us from repeating the parent's initialization code.

## 10. Types of Inheritance

Python supports these common inheritance patterns:

1. Single inheritance: One child inherits from one parent.
2. Multiple inheritance: One child inherits from multiple parents.
3. Multilevel inheritance: A class inherits from a child class, forming multiple levels.
4. Hierarchical inheritance: Multiple child classes inherit from one parent.
5. Hybrid inheritance: A combination of inheritance patterns.

For your Day 7 factory model, we use hierarchical inheritance:

```text
             Machine
                |
        ----------------
        |              |
    CNCMachine    LatheMachine
```

## 11. Encapsulation

Encapsulation keeps data and related methods together and provides controlled access to an object's data.

### Public attributes

```python
self.name = name
```

Public attributes are intended for normal external use.

### Protected naming convention

```python
self._capacity = capacity
```

A single underscore indicates that the attribute is intended for internal use.

It is a convention, not strict access protection.

### Property getter

```python
@property
def capacity(self):
    return self._capacity
```

This lets us read the value using:

```python
machine.capacity
```

### Property setter

```python
@capacity.setter
def capacity(self, value):

    if value <= 0:
        raise ValueError("Capacity must be greater than 0")

    self._capacity = value
```

This validates the new value before updating it.

### Complete example

```python
class Machine:

    def __init__(self, name, capacity):
        self.name = name
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):

        if value <= 0:
            raise ValueError("Capacity must be greater than 0")

        self._capacity = value


machine = Machine("CNC-01", 50)

print(machine.capacity)

machine.capacity = 80

print(machine.capacity)
```

Output:

```text
50
80
```

If we try:

```python
machine.capacity = -100
```

Python raises:

```text
ValueError: Capacity must be greater than 0
```

## 12. Polymorphism

Polymorphism means one interface can have multiple implementations.

Different classes can define the same method name but behave differently.

### Example

```python
class Machine:

    def describe(self):
        return "General machine"


class CNCMachine(Machine):

    def describe(self):
        return "CNC machine"


class LatheMachine(Machine):

    def describe(self):
        return "Lathe machine"


machines = [
    CNCMachine(),
    LatheMachine(),
    Machine()
]

for machine in machines:
    print(machine.describe())
```

Output:

```text
CNC machine
Lathe machine
General machine
```

The same method call works with different objects.

## 13. Method Overriding

Method overriding means redefining an inherited method in a subclass.

Example:

```python
class Machine:

    def describe(self):
        return "General machine"


class CNCMachine(Machine):

    def describe(self):
        return "CNC machine"


cnc = CNCMachine()

print(cnc.describe())
```

Output:

```text
CNC machine
```

The subclass implementation is used for the CNC object.

## 14. Inheritance vs Composition

### Inheritance – Is-a relationship

A CNC machine is a machine.

```python
class Machine:
    pass


class CNCMachine(Machine):
    pass
```

### Composition – Has-a relationship

A schedule has tasks.

```python
class Task:

    def __init__(self, name):
        self.name = name


class Schedule:

    def __init__(self, tasks):
        self.tasks = tasks


task1 = Task("Production")
task2 = Task("Inspection")

schedule = Schedule([task1, task2])

for task in schedule.tasks:
    print(task.name)
```

Output:

```text
Production
Inspection
```

Composition is useful when one object contains or uses other objects rather than being a specialized type of another object.

---

# PART 4: DAY 7 PRACTICAL IMPLEMENTATION

## 15. Machine Class – Required Implementation

Requirements:

- `name`
- `capacity_per_hour`
- `available=True`
- `__repr__()`
- Capacity validation
- Property getter and setter

```python
class Machine:

    def __init__(self, name, capacity_per_hour, available=True):

        if capacity_per_hour <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.name = name
        self._capacity_per_hour = capacity_per_hour
        self.available = available

    @property
    def capacity_per_hour(self):
        return self._capacity_per_hour

    @capacity_per_hour.setter
    def capacity_per_hour(self, value):

        if value <= 0:
            raise ValueError("Capacity must be greater than 0")

        self._capacity_per_hour = value

    def describe(self):
        return f"Machine: {self.name}"

    def hourly_capacity(self):
        return self.capacity_per_hour

    def __repr__(self):
        return (
            f"Machine(name={self.name!r}, "
            f"capacity_per_hour={self.capacity_per_hour}, "
            f"available={self.available})"
        )
```

## 16. CNCMachine Class

```python
class CNCMachine(Machine):

    def __init__(self, name, capacity_per_hour, available=True):
        super().__init__(name, capacity_per_hour, available)

    def describe(self):
        return f"CNC Machine: {self.name}"
```

## 17. LatheMachine Class

```python
class LatheMachine(Machine):

    def __init__(self, name, capacity_per_hour, available=True):
        super().__init__(name, capacity_per_hour, available)

    def describe(self):
        return f"Lathe Machine: {self.name}"
```

Both subclasses inherit common functionality and override `describe()`.

## 18. Task Class

Requirements:

- `name`
- `duration_minutes`
- `priority`
- `is_urgent` property
- Duration validation
- `__repr__()`

```python
class Task:

    def __init__(self, name, duration_minutes, priority):

        if duration_minutes <= 0:
            raise ValueError("Task duration must be greater than 0")

        self.name = name
        self.duration_minutes = duration_minutes
        self.priority = priority

    @property
    def is_urgent(self):
        return self.priority <= 2

    def __repr__(self):
        return (
            f"Task(name={self.name!r}, "
            f"duration_minutes={self.duration_minutes}, "
            f"priority={self.priority})"
        )
```

### Understand `is_urgent`

| Priority | Result |
|---:|---|
| 1 | True |
| 2 | True |
| 3 | False |
| 4 | False |
| 5 | False |

According to the roadmap, priority values less than or equal to 2 are urgent.

## 19. Demonstrate Polymorphism

```python
machines = [
    CNCMachine("CNC-01", 50),
    LatheMachine("LATHE-01", 30),
    CNCMachine("CNC-02", 60, False)
]

for machine in machines:

    print(machine.describe())
    print("Capacity:", machine.hourly_capacity())
    print("Available:", machine.available)
    print()
```

Expected output:

```text
CNC Machine: CNC-01
Capacity: 50
Available: True

Lathe Machine: LATHE-01
Capacity: 30
Available: True

CNC Machine: CNC-02
Capacity: 60
Available: False
```

---

# PART 5: ASSERT TESTING

## 20. What is assert?

An `assert` statement checks whether a condition is true.

If the condition is false, Python raises an `AssertionError`.

Example:

```python
x = 10

assert x == 10
```

This passes without an error.

Example:

```python
x = 10

assert x == 20
```

This raises an `AssertionError`.

## 21. Day 7 Required Tests

Add the following tests after defining your classes.

```python
# Machine tests
machine = Machine("General-01", 40)

assert machine.name == "General-01"
assert machine.capacity_per_hour == 40
assert machine.available is True

# CNC and Lathe tests
cnc = CNCMachine("CNC-01", 50)
lathe = LatheMachine("LATHE-01", 30)

assert cnc.describe() == "CNC Machine: CNC-01"
assert lathe.describe() == "Lathe Machine: LATHE-01"

# Capacity property test
machine.capacity_per_hour = 70

assert machine.capacity_per_hour == 70

# Invalid capacity test
try:
    machine.capacity_per_hour = 0
    assert False, "Expected ValueError"
except ValueError:
    pass

# Task tests
task1 = Task("Production", 60, 1)
task2 = Task("Inspection", 30, 3)

assert task1.is_urgent is True
assert task2.is_urgent is False
assert task1.duration_minutes == 60

# Invalid duration test
try:
    Task("Invalid task", 0, 1)
    assert False, "Expected ValueError"
except ValueError:
    pass

print("All tests passed!")
```

Expected output:

```text
All tests passed!
```

**Important:** Run the file normally using Python. Python's `-O` optimization option disables ordinary assert statements, so don't use it when checking these tests.

---

# PART 6: COMMON MISTAKES

## Mistake 1: Forgetting self

Incorrect:

```python
def describe():
    print("Machine")
```

Correct:

```python
def describe(self):
    print("Machine")
```

## Mistake 2: Forgetting super()

Incorrect:

```python
class CNCMachine(Machine):

    def __init__(self, name, capacity):
        self.name = name
```

This does not initialize all the attributes expected from the parent constructor.

Correct:

```python
class CNCMachine(Machine):

    def __init__(self, name, capacity):
        super().__init__(name, capacity)
```

## Mistake 3: Using a class attribute instead of an instance attribute

Incorrect for machine-specific capacity:

```python
class Machine:
    capacity = 50
```

This gives a shared class-level default rather than storing a distinct capacity for each object.

Correct:

```python
class Machine:

    def __init__(self, capacity):
        self.capacity = capacity
```

## Mistake 4: Forgetting validation

Incorrect:

```python
self.duration_minutes = duration_minutes
```

Correct:

```python
if duration_minutes <= 0:
    raise ValueError("Task duration must be greater than 0")

self.duration_minutes = duration_minutes
```

## Mistake 5: Calling a property like a method

Incorrect:

```python
task.is_urgent()
```

Correct:

```python
task.is_urgent
```

Because `is_urgent` uses `@property`.

---

# PART 7: PRACTICE QUESTIONS

## A. Conceptual Questions

1. What is OOP?
2. What is a class?
3. What is an object?
4. What is the purpose of `__init__()`?
5. What does `self` represent?
6. What is the difference between class and instance attributes?
7. What is inheritance?
8. Why do we use `super()`?
9. What is encapsulation?
10. What is polymorphism?
11. What is method overriding?
12. What is the difference between inheritance and composition?
13. What is the purpose of `@property`?
14. What is a setter?
15. What is the difference between `__str__()` and `__repr__()`?

## B. Coding Practice

1. Create a Machine class with name and capacity.
2. Create two Machine objects with different capacities.
3. Create CNCMachine inheriting from Machine.
4. Create LatheMachine inheriting from Machine.
5. Override `describe()` in both subclasses.
6. Add a property to validate machine capacity.
7. Create a Task class with duration validation.
8. Add the `is_urgent` property.
9. Create a mixed machine list and demonstrate polymorphism.
10. Write assert tests for all classes.

---

# PART 8: DAY 7 REVISION CHECKLIST

## Python OOP

- [ ] Understand classes and objects.
- [ ] Understand `__init__()` and `self`.
- [ ] Understand instance and class attributes.
- [ ] Understand `__repr__()` and `__str__()`.
- [ ] Understand inheritance.
- [ ] Use `super().__init__()`.
- [ ] Understand encapsulation.
- [ ] Use `_protected` naming.
- [ ] Implement `@property` getters.
- [ ] Implement validated setters.
- [ ] Understand polymorphism.
- [ ] Override `describe()`.
- [ ] Understand inheritance vs composition.
- [ ] Implement Machine, CNCMachine and LatheMachine.
- [ ] Implement Task with `is_urgent`.
- [ ] Validate duration using ValueError.
- [ ] Run assert tests.

## Required Deliverable

**File:** `week01/day07_oop.py`

It must contain:

- Machine class with `__repr__()`.
- CNCMachine subclass.
- LatheMachine subclass.
- Task class.
- Inheritance using `super()`.
- Capacity validation.
- Duration validation.
- `is_urgent` property.
- Polymorphism demonstration.
- Six or more successful assertions.

## GitHub Commit

```bash
git add week01/day07_oop.py

git commit -m "Add Machine/Task classes with inheritance"

git push
```

---

# PART 9: FINAL INTERVIEW REVISION

Before finishing Day 7, make sure you can explain these four concepts without looking at your notes:

| OOP Pillar | Factory Example |
|---|---|
| Encapsulation | Validate machine capacity |
| Inheritance | CNCMachine inherits Machine |
| Polymorphism | CNC and Lathe implement describe() differently |
| Abstraction | Expose essential operations while hiding implementation details |

**Final interview explanation:**

"In my factory scheduling project, I use object-oriented programming to represent machines and production tasks. I use inheritance to create specialized machine classes, encapsulation to validate machine and task data, and polymorphism to allow different machine types to implement common methods differently. This helps keep the code organized, reusable and easier to maintain."

---

**Day 7 Python Topic: OOP**

**Main Concepts:** Classes, Objects, Inheritance, Encapsulation, Polymorphism

**Practical Deliverable:** `day07_oop.py`

**Completion Status:** Mark complete only after the code runs successfully, the assertions pass and the Git commit is pushed.
