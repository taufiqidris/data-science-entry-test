#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Question 6

#    Task 1
#    - Create a function that finds the first negative number in a list (lst).
#    - Return the first negative number if found, otherwise return "No negatives".
#    - Use a while loop to implement this.

def find_first_negative(lst):
    # check if lst is a list using type()
    if type(lst) !=list:
        return "No negatives"
    # using while loop
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
        
    return "No negatives"


# In[5]:


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
print(find_first_negative([3, 5, -1, 7, -2, 8]))


# In[6]:


# Invoke the function "find_first_negative" using the following scenario:
# - [2, 10, 7, 0]
print(find_first_negative([2, 10, 7, 0]))


# In[ ]:




