'''
Created on Nov 22, 2016

@author: Student
'''
# Arbitrary number of keyword parameters

def f(**kwargs):
    print(kwargs)
    
f()
f(de="German", en="English", fr="French")