#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Question 2

#    Task 1
#    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
#    - lst must be a list.
#    - Return the modified list.

def find_and_replace(lst, find_val, replace_val):
    # Check if lst is a list using type()
    if type(lst) != list:
        return []

    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst


# In[7]:


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)


# In[8]:


# Invoke the function "find_and_replace" using the following scenarios:
# - ["apple", "banana", "apple"], "apple", "orange"
find_and_replace(["apple", "banana", "apple"], "apple", "orange")


# In[ ]:




