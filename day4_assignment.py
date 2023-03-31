#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers = input("Enter a list of integers separated by commas: ")
numbers_list = numbers.split(",")


numbers_list = [int(num) for num in numbers_list]

def sum_of_squares(numbers):
    
    sum = 0
    for num in numbers:
        sum += num ** 2
    return sum
result = sum_of_squares(numbers_list)
print(result)


# In[ ]:




