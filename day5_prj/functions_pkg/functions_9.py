'''
Created on Nov 22, 2016

@author: Student
'''

def outer(num1):
    def inner_increment(num1):
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)
    
    
outer(10)