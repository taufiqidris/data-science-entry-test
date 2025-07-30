#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Question 3

#    Task 1
#    - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
#    - Return the updated dictionary.

def update_dictionary(dct, key, value):
    # Check if key exists
    if key in dct:
        print(dct[key])  # Print original value
    # Update or add the key-value pair
    dct[key] = value
    
    return dct


# In[7]:


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"

print(update_dictionary({}, "name", "Alice"))
# key does not exist


# In[8]:


# Invoke the function "update_dictionary" using the following scenarios:
# - {"age": 25}, "age", 26

print(update_dictionary({"age": 25}, "age", 26))
# key exists,"age" already exists, prints the original value 25, then updates it to 26

