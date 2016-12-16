'''
Created on Nov 22, 2016

@author: Student
'''
def avg(intfirst, *intrest):
    #print(intfirst + sum(intrest))
    #print(1 + len(intrest))
    return(intfirst + sum(intrest)) / (1 + len(intrest))

print(avg(1, 2, 3, 4))

print(avg(5, 10, 15, 20, 25, 30, 35))