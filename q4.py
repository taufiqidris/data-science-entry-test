#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Question 4

#    Task 1
#    - Create a function that reverses a given string (s).
#    - s must be a string.
#    - Return the reversed string.

def string_reverse(s):
    # Check if argument s is a string using type()
    if type(s) != str:
        return ""
    # Reverse the string using slicing
    return s[::-1]


# In[6]:


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
print(string_reverse("Hello World")) 


# In[7]:


# Invoke the function "string_reverse" using the following scenarios:
# - "Python"
print(string_reverse("Python")) 

