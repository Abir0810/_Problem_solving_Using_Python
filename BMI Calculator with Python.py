#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator with Python 

# In[4]:


height=float(input("Enter your height in centimerters: "))
weight=float(input("Enter your weight in centemeters: "))
height= height/100
BMI= weight/(height*height)
print("your body mass index is:  ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are severly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: print("You are serverly overweight")
else:("Enter valid details")


# In[ ]:




