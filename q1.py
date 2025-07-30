#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Question 1

#    Task 1
#    - Create a function that would swap the value of x and y using only x and y as variables.
#    - x and y must be numeric.
#    - Return -1 if x and y is not numeric, and
#    - print the swapped values if both x and y are numeric.
# function swap with 2 arguments, x and y        

def swap(x, y):
    # type(x) and type(y) in [int, float] must be numeric either integer or float, if not to return -1
    if not (type(x) in [int, float] and type(y) in [int, float]):
        return -1
    print(x, y)


# In[19]:


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
swap("Apple", 10)


# In[20]:


# Invoke the function "swap" using the following scenarios:
# - 9, 17
swap(9, 17) 

