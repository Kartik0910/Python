#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("enter the number you want to try"))
print(num)

if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("The number is neither divisible by 3 nor by 5 ")


# In[ ]:




