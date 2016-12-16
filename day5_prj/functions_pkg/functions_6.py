'''
Created on Nov 22, 2016

@author: Student
'''
# Function argument annotations can be a useful way to give programmers
# hints about how a function is supposed to be used

def add(x:int, y:int) ->int:
    return x + y

print(help(add))
print(add(20, 2))