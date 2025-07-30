#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 5

#    Task 1
#    - Create a function to check if the number (num) is divisible by another number (divisor).
#    - Both num and divisor must be numeric.
#    - Return True if num is divisible by divisor, False otherwise.

def check_divisibility(num, divisor):
    # Check if both arguments num and divisor are int or float using type()
    if type(num) not in [int, float] or type(divisor) not in [int, float]:
        return False
    if divisor == 0:
        return False
    return num % divisor == 0    


# In[2]:


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
print(check_divisibility(10, 2))


# In[3]:


# Invoke the function "check_divisibility" using the following scenarios:
# - 7, 3
print(check_divisibility(7, 3))


# In[ ]:




