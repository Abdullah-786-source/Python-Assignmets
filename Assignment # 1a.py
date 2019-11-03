#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Printing string in a specefic format
space = "     "
print ("Twinkle, twinkle, little star,")
print (space, "How I wonder what you are!")
print (((space) *2) + "Up above the world so high,")
print (((space) *2) + "Like a diamond in the sky.")
print ("Twinkle, twinkle, little star,")
print (space, "How I wonder what you are!")


# In[5]:


# Printing current version of Python
import sys
print(sys.version)


# In[10]:


# Printing current date and time
import datetime
now = datetime.datetime.now()
print(now)


# In[12]:


# calcuating Area of circle
pi = 3.14
r = float(input ("Enter a Radius."))
a = pi * (r ** 2)
print ("radis is ", a)


# In[14]:


# printing first name and last name in reverse order
firstname = input ("Enter First Name: ")
lastname = input ("Enter Last Name: ")
print (lastname + " " + firstname)


# In[16]:


# Addition of two inputs
a = int(input ("Enter first number: "))
b = int (input ("Enter second number: "))
result = a + b
print (result)


# In[ ]:




