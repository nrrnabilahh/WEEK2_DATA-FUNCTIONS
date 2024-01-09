#!/usr/bin/env python
# coding: utf-8

# In[ ]:


subjects = ["software", "Chemistry", "Mathematics", "Biology"]

def subject_availability(subject_name):
    if(is_available(subject_name)):
        return "the subject is available"
    else:
        return "the subject is not available"
    
def is_available(subject_name):
    return subject_name in subjects

input_subject=input("please enter the name of the subject")
print(subject_availability(input_subject))


# In[ ]:


def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

print(sum(20,10))
print(sub(20,10))
print(mult(20,10))
print(div(20,10))




# In[ ]:





# In[ ]:




