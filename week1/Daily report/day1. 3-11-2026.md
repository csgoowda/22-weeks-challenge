Day 1 – Complete Study Notes and Progress Record
I've organized your Day 1 notes according to the roadmap. I've also updated the progress record based on the work you've completed and confirmed.
Progress record updated
1. Day 1 study notes
Day 1 – Python, DSA, OOP, Aptitude and English
1. Python Fundamentals
What is Python?
Python is a high-level, general-purpose programming language used for backend development, automation, AI, machine learning and data science.
Python execution
In CPython:
1. Python source code is compiled into bytecode.
2. The Python Virtual Machine executes the bytecode.
3. The program produces output.
Python syntax
Syntax means the rules for writing valid Python code.
print("Hello, World!")
Python generally executes statements from top to bottom.
Indentation
Indentation means spaces at the beginning of a line. Python uses indentation to define code blocks.
age = 20

if age >= 18:
    print("Eligible")
Use four spaces for each indentation level.
Comments
Comments explain code and are ignored during normal execution.
# This is a comment
print("Hello")
Variables
A variable is a named reference used to store or access a value.
name = "Chethan"
age = 22
cgpa = 7.3
Variable naming rules:
- Cannot start with a number.
- Cannot contain spaces.
- Can contain letters, numbers and underscores.
- Variable names are case-sensitive.
- Python keywords cannot be used as variable names.
- Use snake_case for readable names.
Basic data types
Type	Example	Meaning
int	100	Whole number
float	7.3	Decimal number
str	"Python"	Text
bool	True	True or False100 is an integer, while "100" is a string.
print()
Displays information.
print("Hello Python")
input()
Receives information from the user. It returns a string by default.
name = input("Enter your name: ")
Type conversion
Function	Purpose
int()	Convert to integer
float()	Convert to decimal
str()	Convert to string
bool()	Convert to BooleanExample:
age = int(input("Enter age: "))
Arithmetic operators
Operator	Meaning	Example
'+	Addition	10 + 5 = 15
'-	Subtraction	10 - 5 = 5
*	Multiplication	10 * 5 = 50
/	Division	10 / 5 = 2.0
//	Floor division	11 // 5 = 2
%	Remainder	11 % 5 = 1
**	Power	2 ** 3 = 8Five Python practice exercises
1. Print your introduction.
2. Store and display student information.
3. Receive two numbers and calculate their sum.
4. Check the type of input before and after conversion.
5. Create a Machine summary using machine_name, machine_capacity and is_available.

2. DSA Fundamentals
What is DSA?
DSA stands for Data Structures and Algorithms.
- Data Structures organize and store data.
- Algorithms are step-by-step instructions to solve problems.
What is an algorithm?
An algorithm is a finite sequence of well-defined steps used to solve a particular problem.

Example: Adding two numbers.
1. Start.
2. Receive two numbers.
3. Add them.
4. Display the result.
5. Stop.
IPO model
Stage	Meaning	Addition example
Input	Receive data	10 and 20
Process	Perform operation	10 + 20
Output	Display result	30Time complexity
Time complexity describes how the amount of work performed by an algorithm grows as input size increases.

It helps programmers compare algorithm efficiency.
Big-O notation
O(1) – Constant time

The amount of work stays approximately constant as input size increases.
numbers = [10, 20, 30, 40]
print(numbers[0])
O(n) – Linear time

The work grows proportionally with the number of elements.
numbers = [10, 20, 30]

for number in numbers:
    print(number)
O(n²) – Quadratic time

Two nested loops, each running n times, perform approximately n × n iterations.
numbers = [10, 20, 30]

for i in numbers:
    for j in numbers:
        print(i, j)
Complexity	For n = 5
O(1)	1
O(n)	5
O(n²)	25Dry run: Production total
production = [100, 150, 200, 120]
total = 0

for quantity in production:
    total = total + quantity

print(total)
Iteration	Quantity	Total
1	100	100
2	150	250
3	200	450
4	120	570Final output: 570.

3. OOP Fundamentals
What is OOP?
OOP means Object-Oriented Programming. It organizes programs around objects that combine data and functionality.
Class
A class is a blueprint or template used to create objects.
class Machine:
    pass
Object
An object is an instance of a class.

Example: CNC Machine and Drilling Machine can be two objects of the Machine class.
Attributes
Attributes represent data or properties belonging to an object or class.
Methods
Methods are functions defined inside a class. They represent actions an object can perform.
Constructor and self
class Machine:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def display_details(self):
        print("Machine:", self.name)
        print("Capacity:", self.capacity)


machine1 = Machine("CNC Machine", 500)
machine2 = Machine("Drilling Machine", 300)

machine1.display_details()
machine2.display_details()
- __init__() initializes a new object.
- self refers to the current object.
- self.name and self.capacity are instance attributes.
- display_details() is a method.
- machine1 and machine2 are objects.

4. Aptitude – Percentages
What is percentage?
Percentage means a value out of 100.
Fraction to percentage
Percentage = (Numerator / Denominator) × 100

Example:

(5000 / 20000) × 100 = 25%
Percentage to fraction
25% = 25/100 = 1/4
Decimal to percentage
Multiply by 100.

0.25 × 100 = 25%
Percentage to decimal
Divide by 100.

60 / 100 = 0.6
X% of a number
X% of N = (X / 100) × N

Example:

20% of 150 = (20 / 100) × 150 = 30
Quick calculation tricks
Percentage	Shortcut
10%	Divide by 10
20%	Divide by 5
25%	Divide by 4
50%	Divide by 2
5%	Find 10%, then divide by 2
1%	Divide by 100
5. English Communication
Interview self-introduction structure
1. Greeting.
2. Name and current education.
3. Previous education.
4. Industrial or internship exposure.
5. Technical skills and projects.
6. Career goal.
7. Thank the interviewer.
Useful sentences
- I am currently pursuing my Bachelor of Engineering in Information Science and Engineering.
- I completed my Diploma in Mechanical Engineering.
- I gained exposure to manufacturing and process design.
- I am interested in Python backend development.
- My goal is to combine manufacturing knowledge with software development skills.
Speaking practice
- Speak slowly and clearly.
- Use simple English.
- Practise without reading.
- Record your voice.
- Identify one sentence to improve.
- Repeat the introduction.

Day 1 Revision Summary
Topics studied:
- Python installation and execution
- Syntax, indentation and comments
- Variables and naming rules
- Four basic data types
- Input, output and type conversion
- Arithmetic operators
- Algorithms and IPO
- O(1), O(n), O(n²)
- Classes, objects, attributes and methods
- Percentages
- English self-introduction
Day 1 is complete only after all 12 roadmap checklist activities are verified.




2. Updated Day 1 progress record
Verified checklist completion
58%



7 of 12 activities completed
No.	Activity	Current status
1	Python version and simple .py execution	Done
2	Editor and project folder verified	Pending
3	Git repository/status checked	Pending
4	Python syntax, indentation, comments and variables	Done
5	Four basic data types	Done
6	Input, print and type conversion	Done
7	Five Python exercises	Confirmed
8	Algorithm and Big-O understanding	Done
9	OOP explained in own words	Pending
10	Percentage questions and mistake review	Pending
11	Two-minute English introduction recorded/practised	Pending
12	Notes and progress status updated	Done

The DSA concept explanations and complexity answers were correct. The IPO example still needs further practice, but the required algorithm and Big-O understanding has been demonstrated.
3. Remaining work to close Day 1
There are five activities left:
1. Verify your project folder.
2. Check Git repository and status.
3. Explain OOP concepts in your own words.
4. Complete 8–10 aptitude questions and review mistakes.
5. Record and practise your two-minute English introduction.
Progress rule: Day 1 remains open until all 12 activities are verified. We will not automatically advance to Day 2 just because the notes are finished.
