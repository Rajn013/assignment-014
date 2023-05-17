#!/usr/bin/env python
# coding: utf-8

# Q1. Is an assignment operator like += only for show? Is it possible that it would lead to faster results at the runtime?
# 

# += is not just for show and can potentially lead to faster results at runtime, but the performance difference is typically small. Readability and maintainability should be the primary considerations when choosing between += and separate operations.
# 

# Q2. What is the smallest number of statements you'd have to write in most programming languages to replace the Python expression a, b = a + b, a?
# 

# #In most programming languages, the easiest way to replace the Python expression a, b = a + b, a is to use a temporary variable. The smallest number of statements needed is two:
# 
# temp = a
# 
# a = a+b
# 
# b = temp

# Q3. In Python, what is the most effective way to set a list of 100 integers to 0?
# 

# In[5]:


list = [0] * 100


# In[6]:


list


# Q4. What is the most effective way to initialise a list of 99 integers that repeats the sequence 1, 2, 3? S If necessary, show step-by-step instructions on how to accomplish this.
# 

# In[7]:


list = [1,2,3] * 33


# In[8]:


list


# Q5. If you're using IDLE to run a Python application, explain how to print a multidimensional list as efficiently?
# 

# In[9]:


#When using IDLE to run a Python application, printing a multidimensional list efficiently can be done by using a loop to iterate over the list's elements and printing them one by one. 
#for example

list = [[1,2,3,4],[5,6,7],[8,9,10]]
for row in list:
    print(row)


# Q6. Is it possible to use list comprehension with a string? If so, how can you go about doing it?
# 

# 
# The easiest way to use list comprehension with a string in Python is to treat the string as an iterable sequence of characters.

# In[11]:


new_string = "hello , world!"
list = [char for char in new_string]


# In[12]:


list


# Q7. From the command line, how do you get support with a user-written Python programme? Is this possible from inside IDLE?
# 

# #True, it is possible to get support with a user-written Python program both from the command line and inside IDLE.
# Inside IDLE, you can also get support:
# 
# Reading through the program's code and comments.
# Using the built-in help function (help()) to access documentation and usage details.
# Utilizing the Shift+Tab shortcut to view function signatures and documentation.

# Q8. Functions are said to be “first-class objects” in Python but not in most other languages, such as C++ or Java. What can you do in Python with a function (callable object) that you can't do in C or C++?
# 

# "first-class objects," which means you can treat them just like any other object in the language. Here's an easy way to understand what you can do with functions in Python that you can't do in languages like C or C++:
# 
# Assign functions to variables: You can assign a function to a variable, just like you assign an integer or string to a variable. This allows you to refer to the function using the variable name and use it in various ways.
# 
# Pass functions as arguments: Python lets you pass functions as arguments to other functions. This means you can write functions that take other functions as inputs, allowing for dynamic and flexible behavior.
# 
# Return functions from other functions: You can have a function return another function as its result. This can be useful when you want to create specialized or customized functions on the fly.
# 
# Store functions in data structures: Python allows you to store functions in data structures like lists, dictionaries, or sets. This makes it possible to create collections of functions and perform operations on them, like iterating over the functions and executing them.
# 
# Define functions inside other functions: Python supports nested functions, which means you can define functions within other functions. This allows for better organization and encapsulation of code, especially when the inner function is only needed within the outer function.

# Q9. How do you distinguish between a wrapper, a wrapped feature, and a decorator?
# 

# Wrapper: A wrapper is a function or class that adds functionality to an existing function or class without changing its core behavior.
# 
# Wrapped feature: The wrapped feature refers to the original function or class that is being modified or extended by the wrapper.
# 
# Decorator: A decorator is a special kind of wrapper in Python that uses the @ symbol and is placed above a function or class definition to add extra functionality to it.

# Q10. If a function is a generator function, what does it return?
# 

# If a function is a generator function, it returns a generator object. The generator object can be iterated over to produce a sequence of values, one at a time, using the yield statement inside the function.
# 

# Q11. What is the one improvement that must be made to a function in order for it to become a generator function in the Python language?
# 

# To turn a regular function into a generator function in Python, you need to replace the return statement(s) with yield statement(s). This allows the function to generate a sequence of values on-the-fly and be used as an iterator.

# Q12. Identify at least one benefit of generators.
# 

# 
# One benefit of generators is that they allow for memory-efficient and on-the-fly generation of values, which is particularly useful when working with large or infinite sequences of data.

# In[ ]:




