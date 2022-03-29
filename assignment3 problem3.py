#!/usr/bin/env python
# coding: utf-8

# In[3]:


#calculate the upper and lower case
def alphabets(list1):
    count_upper=0
    count_lower=0
    for i in list1:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
    print(" no of uppercase letters are: ",count_upper)
    print("no of lower case letters are: ",count_lower)
string=" The quick Brow Fox"
list2=(string)
alphabets(list2)


# In[ ]:




