
# Top Python Interview Questions (with Answers & Examples)

## Table of Contents
1. [Python Basics](#python-basics)
2. [OOP, Advanced Functions, and Error Handling](#oop-advanced-functions-and-error-handling)
3. [File Handling, Iterators, Comprehensions, Built-ins, Modules](#file-handling-iterators-comprehensions-built-ins-modules)
4. [Modules, Packages, Standard Library, OOP Advanced, Functional Programming](#modules-packages-standard-library-oop-advanced-functional-programming)
5. [Advanced Topics: Threading, Multiprocessing, Async, Testing, Data Science, Web, Best Practices](#advanced-topics-threading-multiprocessing-async-testing-data-science-web-best-practices)
6. [More Advanced Python Interview Questions](#more-advanced-python-interview-questions)
7. [Networking](#networking)
8. [Database](#database)
9. [Security](#security)
10. [Design Patterns](#design-patterns)
11. [Interview Coding Problems](#interview-coding-problems)
12. [Python Internals](#python-internals)


## Python Basics

1. **What is Python?**
   - Python is a high-level, interpreted, general-purpose programming language known for its readability and simplicity.

2. **What are the key features of Python?**
   - Easy to learn and use
   - Interpreted language
   - Dynamically typed
   - Extensive standard library
   - Supports OOP and functional programming

3. **What is PEP 8?**
   - PEP 8 is the Python Enhancement Proposal that provides guidelines and best practices on how to write Python code.

4. **How is Python interpreted?**
   - Python code is executed line by line by the Python interpreter.

5. **What is the difference between list and tuple?**
   - Lists are mutable, tuples are immutable.
	 - Example:
		 ```python
		 my_list = [1, 2, 3]
		 my_tuple = (1, 2, 3)
		 my_list[0] = 10  # Valid
		 # my_tuple[0] = 10  # Error
		 ```

6. **What are dictionaries in Python?**
   - Unordered collections of key-value pairs.
	 - Example:
		 ```python
		 d = {'a': 1, 'b': 2}
		 print(d['a'])  # 1
		 ```

7. **What is slicing?**
   - Extracting a portion of a sequence.
	 - Example:
		 ```python
		 s = 'python'
		 print(s[1:4])  # yth
		 ```

8. **What is the difference between `==` and `is`?**
   - `==` checks value equality, `is` checks identity (same object in memory).
	 - Example:
		 ```python
		 a = [1, 2]
		 b = [1, 2]
		 print(a == b)  # True
		 print(a is b)  # False
		 ```

9. **How do you handle exceptions in Python?**
   - Using try-except blocks.
   - Example:
	 ```python
	 try:
		 x = 1 / 0
	 except ZeroDivisionError:
		 print('Cannot divide by zero')
	 ```

10. **What is a function? How do you define one?**
	- A reusable block of code.
		 - Example:
			 ```python
			 def add(a, b):
					 return a + b
			 ```

11. **What are *args and **kwargs?**
	- *args: variable number of positional arguments
	- **kwargs: variable number of keyword arguments
		 - Example:
			 ```python
			 def func(*args, **kwargs):
					 print(args, kwargs)
			 ```

12. **What is a lambda function?**
	- An anonymous, inline function.
		 - Example:
			 ```python
			 square = lambda x: x * x
			 print(square(5))  # 25
			 ```

13. **What is list comprehension?**
	- A concise way to create lists.
		 - Example:
			 ```python
			 squares = [x*x for x in range(5)]
			 ```

14. **What is the difference between `append()` and `extend()` in lists?**
	- `append()` adds a single element; `extend()` adds elements from another iterable.
		 - Example:
			 ```python
			 l = [1, 2]
			 l.append([3, 4])  # [1, 2, [3, 4]]
			 l = [1, 2]
			 l.extend([3, 4])  # [1, 2, 3, 4]
			 ```

15. **What is a module?**
	- A file containing Python code (functions, classes, variables) that can be imported.

16. **How do you import a module?**
	- Using the `import` statement.
		 - Example:
			 ```python
			 import math
			 print(math.sqrt(16))
			 ```

17. **What is the purpose of `__init__.py`?**
	- Marks a directory as a Python package.

18. **What is a package?**
	- A collection of Python modules under a common namespace.

19. **What is the difference between local and global variables?**
	- Local: defined inside a function; Global: defined outside all functions.

20. **How do you create a virtual environment?**
	- Using `python -m venv env` or `virtualenv env`.

21. **What is pip?**
	- The package installer for Python.

22. **What is the difference between Python 2 and Python 3?**
	- Print statement vs function, integer division, Unicode support, etc.

23. **What is a decorator?**
	- A function that modifies another function.
	- Example:
	  ```python
	  def my_decorator(func):
		  def wrapper():
			  print('Before')
			  func()
			  print('After')
		  return wrapper
	  @my_decorator
	  def say_hello():
		  print('Hello')
	  ```

24. **What is a generator?**
	- A function that yields values one at a time using `yield`.
	- Example:
	  ```python
	  def gen():
		  yield 1
		  yield 2
	  ```

25. **What is the difference between `yield` and `return`?**
	- `return` ends a function and returns a value; `yield` returns a generator and can be resumed.

26. **What is the use of `with` statement?**
	- For resource management (context managers), e.g., file handling.
		 - Example:
			 ```python
			 with open('file.txt') as f:
					 data = f.read()
			 ```

27. **What is a class? How do you define one?**
	- A blueprint for creating objects.
		 - Example:
			 ```python
			 class Person:
					 def __init__(self, name):
							 self.name = name
			 ```

28. **What is inheritance?**
	- Mechanism to create a new class from an existing class.
	   - Example:
		 ```python
		 class Animal:
			 pass
		 class Dog(Animal):
			 pass
		 ```

// ...existing code...

30. **What is method overriding?**
	- Redefining a method in a subclass.
	   - Example:
		 ```python
		 class Parent:
			 def show(self):
				 print('Parent')
		 class Child(Parent):
			 def show(self):
				 print('Child')
		 ```

## OOP, Advanced Functions and Error Handling

31. **What is encapsulation?**
	- Wrapping data and methods into a single unit (class). Restricts direct access to some variables.
		 - Example:
			 ```python
			 class MyClass:
					 def __init__(self):
							 self.__private = 42  # private variable
			 ```

32. **What is polymorphism?**
	- The ability to use a common interface for multiple forms (data types).
	   - Example:
		 ```python
		 class Cat:
			 def speak(self):
				 print('Meow')
		 class Dog:
			 def speak(self):
				 print('Woof')
		 def animal_sound(animal):
			 animal.speak()
		 ```

33. **What is abstraction?**
	- Hiding complex implementation details and showing only the necessary features.

34. **What is a static method?**
	- A method bound to the class, not the instance. Defined with `@staticmethod`.
		 - Example:
			 ```python
			 class Math:
					 @staticmethod
					 def add(a, b):
							 return a + b
			 ```

35. **What is a class method?**
	- A method bound to the class, not the object. Defined with `@classmethod`.
		 - Example:
			 ```python
			 class MyClass:
					 @classmethod
					 def hello(cls):
							 print('Hello from', cls)
			 ```

36. **What is the difference between `@staticmethod` and `@classmethod`?**
	- `@staticmethod` does not take `self` or `cls` as the first argument; `@classmethod` takes `cls`.

37. **What is method resolution order (MRO)?**
	- The order in which Python looks for a method in a hierarchy of classes.
	- Use `ClassName.__mro__` or `help(ClassName)`.

38. **What is duck typing?**
	- Python’s dynamic typing: "If it looks like a duck and quacks like a duck, it’s a duck."

39. **What is the purpose of `super()`?**
	- To call methods from a parent/super class.
	   - Example:
		 ```python
		 class Parent:
			 def show(self):
				 print('Parent')
		 class Child(Parent):
			 def show(self):
				 super().show()
				 print('Child')
		 ```

40. **What is exception handling?**
	- Mechanism to handle runtime errors using try-except-finally blocks.

41. **What is the use of `finally` block?**
	- Code in `finally` always runs, regardless of exceptions.
	   - Example:
		 ```python
		 try:
			 x = 1 / 0
		 except:
			 print('Error')
		 finally:
			 print('Cleanup')
		 ```

42. **How to raise a custom exception?**
	- Use `raise` with a custom exception class.
		 - Example:
			 ```python
			 class MyError(Exception):
					 pass
			 raise MyError('Something went wrong')
			 ```

43. **What is the difference between `Exception` and `BaseException`?**
	- `BaseException` is the base class for all exceptions; `Exception` is for most user-defined exceptions.

44. **What is the purpose of `assert` statement?**
	- Used for debugging; raises `AssertionError` if condition is false.
		 - Example:
			 ```python
			 assert 2 + 2 == 4
			 ```

45. **What is the difference between shallow copy and deep copy?**
	- Shallow copy copies references; deep copy copies objects recursively.
		 - Example:
			 ```python
			 import copy
			 a = [[1, 2], [3, 4]]
			 b = copy.copy(a)
			 c = copy.deepcopy(a)
			 ```

46. **What is a docstring?**
	- A string literal used to document a module, class, function, or method.
		 - Example:
			 ```python
			 def foo():
					 """This is a docstring."""
					 pass
			 ```

47. **How do you get the length of a list, tuple, or string?**
	- Using `len()` function.

48. **What is the difference between `remove()`, `pop()`, and `del` in lists?**
	- `remove(x)`: removes first occurrence of x
	- `pop(i)`: removes and returns item at index i
	- `del`: deletes item or slice

49. **How do you reverse a list?**
	- Using `list.reverse()` or `list[::-1]`.

50. **How do you sort a list?**
	- Using `list.sort()` (in-place) or `sorted(list)` (returns new list).

51. **What is a set? How is it different from a list?**
	- Unordered, unique elements. Lists are ordered and can have duplicates.
		 - Example:
			 ```python
			 s = {1, 2, 3}
			 ```

52. **How do you add/remove elements from a set?**
	- `add()`, `remove()`, `discard()` methods.

53. **What is a frozenset?**
	- An immutable set.
		 - Example:
			 ```python
			 fs = frozenset([1, 2, 3])
			 ```

54. **What is a string in Python?**
	- An immutable sequence of Unicode characters.

55. **How do you format strings?**
	- Using f-strings, `format()`, or `%` operator.
		 - Example:
			 ```python
			 name = 'Alice'
			 print(f'Hello, {name}')
			 ```

56. **What is string immutability?**
	- Strings cannot be changed after creation.

57. **How do you convert between string and int?**
	- `int('123')` and `str(123)`

58. **How do you check if a substring exists in a string?**
	- Using `in` keyword.
		 - Example:
			 ```python
			 'py' in 'python'  # True
			 ```

59. **How do you split and join strings?**
	- `split()` breaks a string into a list; `join()` joins a list into a string.
		 - Example:
			 ```python
			 s = 'a,b,c'
			 parts = s.split(',')
			 s2 = ','.join(parts)
			 ```

60. **How do you remove whitespace from a string?**
	- Using `strip()`, `lstrip()`, `rstrip()` methods.

## File Handling, Iterators, Comprehensions, Built-ins, Modules

61. **How do you read and write files in Python?**
	- Using `open()` function.
	   - Example:
		 ```python
		 with open('file.txt', 'r') as f:
			 data = f.read()
		 with open('file.txt', 'w') as f:
			 f.write('Hello')
		 ```

62. **What is the difference between `read()`, `readline()`, and `readlines()`?**
	- `read()`: reads entire file
	- `readline()`: reads one line
	- `readlines()`: reads all lines into a list

63. **How do you check if a file exists?**
	- Using `os.path.exists()` or `pathlib.Path.exists()`.
		 - Example:
			 ```python
			 import os
			 os.path.exists('file.txt')
			 ```

64. **What is an iterator?**
	- An object with `__iter__()` and `__next__()` methods.

65. **What is an iterable?**
	- An object capable of returning its members one at a time (e.g., list, tuple, string).

66. **How do you create a custom iterator?**
	- By defining `__iter__()` and `__next__()` in a class.
	   - Example:
		 ```python
		 class Counter:
			 def __init__(self, low, high):
				 self.current = low
				 self.high = high
			 def __iter__(self):
				 return self
			 def __next__(self):
				 if self.current > self.high:
					 raise StopIteration
				 else:
					 self.current += 1
					 return self.current - 1
		 ```

67. **What is a list comprehension?**
	- A concise way to create lists.
		 - Example:
			 ```python
			 squares = [x*x for x in range(10)]
			 ```

68. **What is a dictionary comprehension?**
	- A concise way to create dictionaries.
		 - Example:
			 ```python
			 d = {x: x*x for x in range(5)}
			 ```

69. **What is a set comprehension?**
	- A concise way to create sets.
		 - Example:
			 ```python
			 s = {x for x in range(5)}
			 ```

70. **What are built-in functions in Python?**
	- Functions like `len()`, `type()`, `id()`, `sum()`, `min()`, `max()`, etc.

71. **How do you get the type of an object?**
	- Using `type(obj)`.

72. **How do you get the id (memory address) of an object?**
	- Using `id(obj)`.

73. **How do you check the data type of a variable?**
	- Using `isinstance(obj, type)`.

74. **What is the use of `enumerate()`?**
	- Returns an enumerate object with index and value pairs.
		 - Example:
			 ```python
			 for i, v in enumerate(['a', 'b']):
					 print(i, v)
			 ```

75. **What is the use of `zip()`?**
	- Combines multiple iterables into tuples.
		 - Example:
			 ```python
			 a = [1, 2]
			 b = ['x', 'y']
			 for i, j in zip(a, b):
					 print(i, j)
			 ```

76. **What is the use of `map()`?**
	- Applies a function to all items in an iterable.
		 - Example:
			 ```python
			 list(map(str, [1, 2, 3]))  # ['1', '2', '3']
			 ```

77. **What is the use of `filter()`?**
	- Filters items in an iterable based on a function.
		 - Example:
			 ```python
			 list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # [2, 4]
			 ```

78. **What is the use of `reduce()`?**
	- Applies a rolling computation to sequential pairs. From `functools` module.
		 - Example:
			 ```python
			 from functools import reduce
			 reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10
			 ```

79. **What is the use of `any()` and `all()`?**
	- `any()`: True if any element is true. `all()`: True if all elements are true.

80. **What is the use of `sorted()`?**
	- Returns a new sorted list from the elements of any iterable.

81. **What is the use of `reversed()`?**
	- Returns a reverse iterator.

82. **What is the use of `abs()`?**
	- Returns the absolute value of a number.

83. **What is the use of `round()`?**
	- Rounds a floating-point number.

84. **What is the use of `sum()`?**
	- Sums items of an iterable.

85. **What is the use of `min()` and `max()`?**
	- Returns the smallest/largest item in an iterable.

86. **What is the use of `chr()` and `ord()`?**
	- `chr()`: int to Unicode char; `ord()`: char to int.

87. **What is the use of `eval()`?**
	- Evaluates a string as a Python expression.
		 - Example:
			 ```python
			 eval('2 + 2')  # 4
			 ```

88. **What is the use of `exec()`?**
	- Executes dynamically created Python code.

89. **What is the use of `globals()` and `locals()`?**
	- Returns the global/local symbol dictionary.

90. **How do you import specific functions from a module?**
	- Using `from module import func`.
		 - Example:
			 ```python
			 from math import sqrt
			 ```
      
## Modules, Packages, Standard Library, OOP Advanced, Functional Programming

91. **What is the difference between module and package?**
    - Module: single file; Package: directory with `__init__.py` and modules.

92. **How do you list all modules installed?**
    - Use `pip list` in terminal or `help('modules')` in Python shell.

93. **What is the Python Standard Library?**
    - A collection of modules and packages included with Python (e.g., `os`, `sys`, `math`, `datetime`).

94. **How do you use the `os` module?**
    - For interacting with the operating system.
		 - Example:
			 ```python
			 import os
			 print(os.getcwd())
			 ```

95. **How do you use the `sys` module?**
    - For system-specific parameters and functions.
		 - Example:
			 ```python
			 import sys
			 print(sys.version)
			 ```

96. **How do you use the `math` module?**
    - For mathematical functions.
		 - Example:
			 ```python
			 import math
			 print(math.pi)
			 ```

97. **How do you use the `random` module?**
    - For generating random numbers.
		 - Example:
			 ```python
			 import random
			 print(random.randint(1, 10))
			 ```

98. **How do you use the `datetime` module?**
    - For date and time manipulation.
		 - Example:
			 ```python
			 from datetime import datetime
			 print(datetime.now())
			 ```

99. **How do you use the `collections` module?**
    - Provides specialized container datatypes like `Counter`, `deque`, `defaultdict`.
		 - Example:
			 ```python
			 from collections import Counter
			 Counter('aabbc')  # Counter({'a': 2, 'b': 2, 'c': 1})
			 ```

100. **What is object-oriented programming (OOP)?**
	- A programming paradigm based on objects and classes.

// ...existing code...

102. **What is method overloading?**
	- Defining multiple methods with the same name but different arguments (not directly supported in Python, can use default arguments or *args).

103. **What is method overriding?**
	- Redefining a method in a subclass.

104. **What is the difference between class and instance variables?**
	- Class variables are shared; instance variables are unique to each object.
		 - Example:
			 ```python
			 class MyClass:
					 x = 10  # class variable
					 def __init__(self):
							 self.y = 20  # instance variable
			 ```

105. **What is the `self` keyword?**
	- Refers to the instance of the class.

106. **What is the `__init__` method?**
	- The constructor method in Python classes.

107. **What is the `__str__` method?**
	- Returns a string representation of the object for `print()`.
		 - Example:
			 ```python
			 class Person:
					 def __str__(self):
							 return 'Person object'
			 ```

108. **What is the `__repr__` method?**
	- Returns an unambiguous string representation of the object.

109. **What is the difference between `__str__` and `__repr__`?**
	- `__str__` is for end users; `__repr__` is for developers/debugging.

110. **What is inheritance hierarchy?**
	- The structure showing how classes inherit from each other.

111. **What is a metaclass?**
	- A class of a class; controls class creation.

112. **What is monkey patching?**
	- Dynamically changing a class or module at runtime.
	- Example:
	  ```python
	  import math
	  math.pi = 3
	  ```

113. **What is functional programming?**
	- Programming paradigm using functions as first-class objects, immutability, and no side effects.

114. **What are first-class functions?**
	- Functions treated as objects: can be passed, returned, assigned.

115. **What is a higher-order function?**
	- A function that takes another function as argument or returns a function.

116. **What is a closure?**
	- A function object that remembers values in enclosing scopes.
		- Example:
		  ```python
		  def outer(x):
				def inner():
					 print(x)
				return inner
		  ```

117. **What is recursion?**
	- A function calling itself.
		 - Example:
			 ```python
			 def fact(n):
					 return 1 if n == 0 else n * fact(n-1)
			 ```

118. **What is memoization?**
	- Caching function results to speed up repeated calls.
		- Example:
		  ```python
		  from functools import lru_cache
		  @lru_cache(maxsize=None)
		  def fib(n):
				if n < 2:
					 return n
				return fib(n-1) + fib(n-2)
		  ```

119. **What is the difference between `@staticmethod`, `@classmethod`, and instance methods?**
	- Instance methods take `self`, class methods take `cls`, static methods take neither.

120. **What is the use of `property()`?**
	- To create managed attributes (getters/setters).
		- Example:
		  ```python
		  class C:
				def __init__(self):
					 self._x = None
				@property
				def x(self):
					 return self._x
				@x.setter
				def x(self, value):
					 self._x = value
		  ```

## Advanced Topics: Threading, Multiprocessing, Async, Testing, Data Science, Web, Best Practices

121. **What is multithreading in Python?**
	- Running multiple threads (smaller units of a process) concurrently.
		 - Example:
			 ```python
			 import threading
			 def worker():
					 print('Worker')
			 t = threading.Thread(target=worker)
			 t.start()
			 ```

122. **What is the Global Interpreter Lock (GIL)?**
	- A mutex that allows only one thread to execute Python bytecode at a time.

123. **What is multiprocessing?**
	- Running multiple processes in parallel, bypassing the GIL.
		 - Example:
			 ```python
			 from multiprocessing import Process
			 def worker():
					 print('Worker')
			 p = Process(target=worker)
			 p.start()
			 ```

124. **What is the difference between threading and multiprocessing?**
	- Threading: shared memory, lightweight, affected by GIL.
	- Multiprocessing: separate memory, true parallelism, not affected by GIL.

125. **What is an asynchronous function?**
	- A function defined with `async def` that can be paused and resumed (coroutines).
		 - Example:
			 ```python
			 import asyncio
			 async def main():
					 print('Hello')
			 asyncio.run(main())
			 ```

126. **What is `await` in Python?**
	- Used to pause a coroutine until the awaited task completes.

127. **What is an event loop?**
	- The core of every asyncio application; runs asynchronous tasks and callbacks.

128. **What is a context manager?**
	- An object that defines `__enter__` and `__exit__` methods, used in `with` statements.

129. **How do you create a custom context manager?**
	- By defining `__enter__` and `__exit__` or using `contextlib`.
	   - Example:
		 ```python
		 class MyContext:
			 def __enter__(self):
				 print('Enter')
			 def __exit__(self, exc_type, exc_val, exc_tb):
				 print('Exit')
		 ```

130. **What is unit testing?**
	- Testing individual units of code (functions, classes) for correctness.

131. **How do you write tests in Python?**
	- Using `unittest` or `pytest` frameworks.
		 - Example:
			 ```python
			 import unittest
			 class TestAdd(unittest.TestCase):
					 def test_add(self):
							 self.assertEqual(2 + 2, 4)
			 ```

132. **What is mocking?**
	- Replacing parts of your system under test with mock objects.

133. **What is test coverage?**
	- A measure of how much code is tested by automated tests.

134. **What is logging?**
	- Recording events for debugging and monitoring.
		 - Example:
			 ```python
			 import logging
			 logging.basicConfig(level=logging.INFO)
			 logging.info('Info message')
			 ```

135. **What is serialization?**
	- Converting an object to a format that can be stored or transmitted (e.g., JSON, pickle).
		 - Example:
			 ```python
			 import json
			 data = {'a': 1}
			 s = json.dumps(data)
			 ```

136. **What is deserialization?**
	- Converting serialized data back to an object.

137. **What is the use of `pickle` module?**
	- Serializing and deserializing Python objects.

138. **What is the use of `json` module?**
	- Working with JSON data (serialization/deserialization).

139. **What is regular expression (regex)?**
	- A sequence of characters defining a search pattern.
		 - Example:
			 ```python
			 import re
			 re.match(r'\d+', '123')
			 ```

140. **How do you use regex in Python?**
	- Using the `re` module: `re.match`, `re.search`, `re.findall`, etc.

141. **What is list slicing?**
	- Extracting a part of a list using `[start:stop:step]`.

142. **What is a memoryview?**
	- A built-in object that exposes the buffer interface.

143. **What is a generator expression?**
	- Like a list comprehension, but returns a generator.
		 - Example:
			 ```python
			 gen = (x*x for x in range(5))
			 ```

144. **What is the difference between `deepcopy` and `copy`?**
	- `copy` creates a shallow copy; `deepcopy` copies nested objects recursively.

145. **What is the use of `*` and `**` in function calls?**
	- `*` unpacks positional arguments; `**` unpacks keyword arguments.

146. **What is the use of `@property` decorator?**
	- To define getter/setter methods in a class.

147. **What is the use of `__slots__`?**
	- Restricts the creation of instance attributes to save memory.

148. **What is the use of `namedtuple`?**
	- Factory function for creating tuple subclasses with named fields.
		 - Example:
			 ```python
			 from collections import namedtuple
			 Point = namedtuple('Point', 'x y')
			 p = Point(1, 2)
			 ```

149. **What is the use of `dataclass`?**
	- Decorator for creating classes with boilerplate code for initialization, representation, etc.
		 - Example:
			 ```python
			 from dataclasses import dataclass
			 @dataclass
			 class Point:
					 x: int
					 y: int
			 ```

150. **What are some best practices for Python programming?**
	- Follow PEP 8
	- Write readable and maintainable code
	- Use virtual environments
	- Write tests
	- Use list comprehensions and generators
	- Handle exceptions properly
	- Document your code

## More Advanced Python Interview Questions

151. **What is the difference between `@dataclass` and a regular class?**
	- `@dataclass` automatically generates special methods like `__init__`, `__repr__`, and `__eq__`.

152. **What is type hinting in Python?**
	- Adding type information to function signatures and variables for better readability and tooling.
		 - Example:
			 ```python
			 def add(a: int, b: int) -> int:
					 return a + b
			 ```

153. **What is the `typing` module?**
	- Provides support for type hints (e.g., `List`, `Dict`, `Optional`).

154. **What is the use of `asyncio.gather()`?**
	- Runs multiple coroutines concurrently and waits for all to finish.
	   - Example:
		 ```python
		 import asyncio
		 async def foo():
			 return 1
		 async def bar():
			 return 2
		 results = asyncio.run(asyncio.gather(foo(), bar()))
		 ```

155. **What is a coroutine?**
	- A function that can pause and resume its execution (`async def`).

156. **What is the difference between `@staticmethod` and a regular function?**
	- `@staticmethod` is bound to a class, not an instance, but is called via the class.

157. **What is the use of `functools.partial`?**
	- Fixes some arguments of a function and returns a new function.
		 - Example:
			 ```python
			 from functools import partial
			 def power(base, exp):
					 return base ** exp
			 square = partial(power, exp=2)
			 ```

158. **What is the use of `itertools` module?**
	- Provides fast, memory-efficient tools for working with iterators (e.g., `count`, `cycle`, `chain`).

159. **What is the use of `__call__` method?**
	- Allows an instance of a class to be called as a function.
		 - Example:
			 ```python
			 class Adder:
					 def __call__(self, x, y):
							 return x + y
			 a = Adder()
			 a(2, 3)  # 5
			 ```

160. **What is the use of `__getattr__` and `__setattr__`?**
	- Customize attribute access and assignment in classes.

161. **What is a descriptor?**
	- An object attribute with binding behavior, defined by methods like `__get__`, `__set__`, and `__delete__`.

162. **What is the use of `property` decorator?**
	- To define managed attributes with getter/setter/deleter.

163. **What is the use of `__enter__` and `__exit__`?**
	- Used to implement context managers for the `with` statement.

164. **What is the use of `yield from`?**
	- Delegates part of a generator’s operations to another generator.
		 - Example:
			 ```python
			 def gen1():
					 yield from range(3)
			 ```

165. **What is the use of `@lru_cache`?**
	- Caches results of expensive function calls for performance.

166. **What is monkey patching?**
	- Dynamically modifying or extending code at runtime.

167. **How do you package and distribute a Python library?**
	- Use `setuptools`, create `setup.py` or `pyproject.toml`, and upload to PyPI.

168. **What is the use of `__main__`?**
	- Allows code to run when the file is executed as a script, not when imported.
		 - Example:
			 ```python
			 if __name__ == "__main__":
					 print("Run as script")
			 ```

169. **What is the use of `timeit` module?**
	- Measures execution time of small code snippets.
		 - Example:
			 ```python
			 import timeit
			 print(timeit.timeit('sum(range(100))', number=1000))
			 ```

170. **What are f-strings?**
	- String literals prefixed with `f` for inline expressions (Python 3.6+).
	- Example:
	  ```python
	  name = 'Bob'
	  print(f'Hello, {name}')
	  ```

## Networking
1. **How do you create a TCP client and server in Python?**
   - Use the `socket` module.
	 - Example (TCP server):
		 ```python
		 import socket
		 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		 s.bind(('localhost', 12345))
		 s.listen(1)
		 conn, addr = s.accept()
		 print('Connected by', addr)
		 data = conn.recv(1024)
		 conn.sendall(data)
		 conn.close()
		 ```

2. **How do you make HTTP requests in Python?**
   - Use the `requests` library.
	 - Example:
		 ```python
		 import requests
		 r = requests.get('https://api.github.com')
		 print(r.status_code, r.json())
		 ```

3. **How do you perform web scraping in Python?**
   - Use `requests` and `BeautifulSoup`.
	 - Example:
		 ```python
		 import requests
		 from bs4 import BeautifulSoup
		 r = requests.get('https://example.com')
		 soup = BeautifulSoup(r.text, 'html.parser')
		 print(soup.title.text)
		 ```

## Database
4. **How do you connect to a SQLite database in Python?**
   - Use the `sqlite3` module.
	 - Example:
		 ```python
		 import sqlite3
		 conn = sqlite3.connect('example.db')
		 c = conn.cursor()
		 c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
		 conn.commit()
		 conn.close()
		 ```

5. **What is SQLAlchemy?**
   - A popular ORM (Object Relational Mapper) for Python.
	 - Example:
		 ```python
		 from sqlalchemy import create_engine, Column, Integer, String, declarative_base
		 Base = declarative_base()
		 class User(Base):
				 __tablename__ = 'users'
				 id = Column(Integer, primary_key=True)
				 name = Column(String)
		 engine = create_engine('sqlite:///example.db')
		 Base.metadata.create_all(engine)
		 ```

## Security
6. **How do you hash a password in Python?**
   - Use the `hashlib` or `bcrypt` library.
	 - Example:
		 ```python
		 import hashlib
		 password = 'secret'.encode()
		 hashed = hashlib.sha256(password).hexdigest()
		 print(hashed)
		 ```

7. **How do you encrypt and decrypt data in Python?**
   - Use the `cryptography` library.
	 - Example:
		 ```python
		 from cryptography.fernet import Fernet
		 key = Fernet.generate_key()
		 f = Fernet(key)
		 token = f.encrypt(b'secret data')
		 print(f.decrypt(token))
		 ```

8. **What are some security best practices in Python?**
   - Never store plain-text passwords.
   - Validate and sanitize user input.
   - Use virtual environments and keep dependencies updated.
   - Avoid using `eval()` on untrusted input.

## Design Patterns
9. **What is the Singleton pattern?**
   - Ensures a class has only one instance.
   - Example:
	 ```python
	 class Singleton:
		 _instance = None
		 def __new__(cls, *args, **kwargs):
			 if not cls._instance:
				 cls._instance = super().__new__(cls)
			 return cls._instance
	 ```

10. **What is the Factory pattern?**
	- Provides a way to create objects without specifying the exact class.
	   - Example:
		 ```python
		 class Dog:
			 def speak(self):
				 return 'Woof'
		 class Cat:
			 def speak(self):
				 return 'Meow'
		 def animal_factory(kind):
			 return Dog() if kind == 'dog' else Cat()
		 ```

11. **What is the Observer pattern?**
	- Allows objects to be notified of state changes in other objects.
	   - Example:
		 ```python
		 class Subject:
			 def __init__(self):
				 self._observers = []
			 def attach(self, obs):
				 self._observers.append(obs)
			 def notify(self, msg):
				 for obs in self._observers:
					 obs.update(msg)
		 class Observer:
			 def update(self, msg):
				 print('Received:', msg)
		 ```

## Interview Coding Problems
12. **How do you reverse a linked list in Python?**
	   - Example:
		 ```python
		 class Node:
			 def __init__(self, val):
				 self.val = val
				 self.next = None
		 def reverse(head):
			 prev = None
			 curr = head
			 while curr:
				 nxt = curr.next
				 curr.next = prev
				 prev = curr
				 curr = nxt
			 return prev
		 ```

13. **How do you find duplicates in a list?**
	   - Example:
		 ```python
		 def find_duplicates(lst):
			 seen = set()
			 dupes = set()
			 for x in lst:
				 if x in seen:
					 dupes.add(x)
				 seen.add(x)
			 return list(dupes)
		 ```

## Python Internals
14. **How does Python manage memory?**
	- Python uses reference counting and a cyclic garbage collector to manage memory.

15. **What is the difference between CPython, PyPy, and Jython?**
	- CPython: standard Python implementation in C.
	- PyPy: fast Python implementation with JIT compilation.
	- Jython: Python implemented in Java, runs on JVM.

16. **How does garbage collection work in Python?**
	- Python automatically frees memory by reference counting and detecting cycles with the `gc` module.
---

## Additional Advanced Topics Not Yet Covered

- **Networking:** No questions on socket, HTTP requests, or web scraping.
- **Database:** No questions on SQLite, SQLAlchemy, or database connections.
- **Security:** No questions on security best practices, encryption, or safe coding.
- **Design Patterns:** No explicit coverage of Singleton, Factory, Observer, etc.
- **Interview Coding Problems:** No algorithmic/coding challenge questions (e.g., reverse a linked list, find duplicates, etc.).
- **Python internals:** No deep-dive on memory management, garbage collection, or CPython internals.
