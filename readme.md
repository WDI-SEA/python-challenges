# Python Challenges

## Getting Started

* Fork and clone this repository
* Run `python3 challenges/file_name.py` to run your file

## Requirements

Complete each challenge in a separate file.

### Challenge 1 - Calculator

Create a simple calculator that first asks the user what method they would like
to use (addition, subtraction, multiplication, division) and then asks the user
for two numbers, returning the result of the method with the two numbers. Here
is a sample prompt:

```
What calculation would you like to do? (add, sub, mult, div)
add
What is number 1?
3
What is number 2?
6
Your result is 9
```

### Challenge 2 - Reverse a string
Reverse a string manually. Don't use s[::-1] (even though that's awesome).
Create a new variable storing an empty string and add the letters from
the first string one by one. The for loop should iterate over the length
of the string and you should access letters individually.

Below is some sample output.

```
Enter a string:
reverse_me
em_esrever
```

### Challenge 3 - Bank Transactions
Create a prompt that asks the user if they would like to display their balance,
withdraw or deposit. Write three methods to perform these calculations and
output the result to the user.

Gather user input using the `input` function. Note that input always returns
user input as a string. You have to manually convert it to an int or a float
to make it behave like number. Also, end the input prompt with a \n newline
character if you want the user to type in on the next line.

```
age = input("How old are you?\n")
age = int(age)
```

Here is a sample output:

```
Your current balance is
4000
What would you like to do? (deposit, withdraw, check_balance)
deposit
How much would you like to deposit?
1000
Your current balance is 5000
Are you done?
yes
Thank you!
```

### Challenge 4 - Sort a String

Create a function that takes a string and returns the string with the letters in 
alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation 
symbols will not be included in the string.

```
Give me a string to alphabetize
supercalifragilisticexpialidocious
Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
```
#  MyGA Modules:
 # Introduction to Computer Science
 * Computer Science is the study of computer systems, algorithms, and data structures, and their applications.<br>
 * It encompasses the theory, design, development, and application of software and hardware systems. <br>
 * It involves the study of algorithms, programming languages, computer architecture, software engineering, databases, human-computer interaction, and more, to create and understand computational systems that can solve complex problems.
 ### * Explain why understanding computer science can make you a better programmer.
  * Algorithmic Thinking: A strong understanding of algorithms and data structures can help you write more efficient and effective code, as well as develop solutions to complex problems<br>
  * Abstraction: Computer Science teaches you to think abstractly and model real-world situations in a way that can be easily represented in code, making your code more maintainable and    scalable.<br>
 * Software Design: Knowledge of software design patterns and principles can help you write code that is easier to read, understand, and maintain, improving the overall quality of your code.
*  Problem Solving: Computer Science trains you to think logically and systematically, which is an essential skill for solving programming problems and debugging code.
* Understanding the Limitations of Computers: Understanding the limitations of computer hardware and software can help you write more efficient code and avoid pitfalls that can negatively  impact performance.
* Overall, a deep understanding of computer science can help you write better code, solve problems more effectively, and make more informed decisions when working on projects.

# Design Patterns
Design patterns exist in programming to provide proven solutions to common problems that arise in software design. They represent a reusable solution to a common problem, and serve as a starting point that can be adapted to meet the specific needs of a particular software project. Design patterns help programmers to write more maintainable, scalable, and efficient code, by abstracting the common characteristics of a particular problem into a reusable and modular design. This results in improved communication among team members and increased productivity, as well as reduced time-to-market for the software product.

#  Define creational, structural, and behavioral design patterns.
Creational design patterns focus on the process of object creation. They aim to provide a way to create objects in a manner suitable for a particular situation, reducing the need for the user to know the details of object creation and promoting loose coupling. Examples of creational design patterns are Singleton, Factory Method, Abstract Factory, Builder, and Prototype.
Structural design patterns deal with the composition of classes, objects and methods, to form larger structures. These patterns provide a way to simplify complex relationships between objects and help to organize the code in a more manageable way. Examples of structural design patterns are Adapter, Bridge, Composite, Decorator, Facade, and Proxy.
Behavioral design patterns define the ways in which objects interact and communicate with each other, and how they operate in a particular context. These patterns provide a way to distribute responsibility among objects, reducing the coupling between objects and making the code more scalable and maintainable. Examples of behavioral design patterns are Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor.


# Algorithms: Introduction to Algorithms
* Algorithms play a crucial role in programming as they provide a step-by-step procedure to solve a problem or perform a task. They allow developers to express solutions to problems in a clear, concise, and unambiguous way, making it easier to understand, debug, and maintain code. Algorithms also serve as a blueprint for efficient and effective implementation of computational processes in software and hardware systems.

# Algorithms: Big O Notation
Big O notation is a way of describing the upper bound of the growth rate of the running time or space usage of an algorithm. It is used to describe the efficiency of algorithms, usually in the worst-case scenario. It gives an idea of the algorithm's scalability and helps determine the maximum amount of resources an algorithm requires as the input size increases. The notation provides a simplified representation of the relationship between the size of the input and the time/space taken to solve the problem.



# Algorithms: Binary Search (the last one)
Binary Search is an algorithm used to search for an element in a sorted array. It works by dividing the array into two parts and repeatedly narrowing down the search space until the target element is found or it is determined that the element is not present in the array. The algorithm works by comparing the middle element of the current search space with the target element. If the middle element is equal to the target element, the search is successful. If the target element is less than the middle element, the search continues in the left half of the array. If the target element is greater than the middle element, the search continues in the right half of the array. This process is repeated until the target element is found or it is determined that the element is not in the array

# Data Structures: Introduction to Data Structures
Data structures are used in computer science to organize, store, and manipulate data in a specific way so as to enable efficient access and modification. Different data structures have different strengths and weaknesses, and selecting the right one for a particular task can have a significant impact on an algorithm's efficiency and overall performance. Some of the most commonly used data structures in computer science include arrays, linked lists, stacks, queues, trees, and graphs. These data structures can be used to implement various algorithms, such as searching, sorting, and graph traversal, among others.
and they are used in a wide range of applications, such as databases, network communication, and algorithms for sorting, searching, and processing data.


## Licensing
1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
