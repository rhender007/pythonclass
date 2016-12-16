'''
Created on Nov 22, 2016

@author: Student
'''
def average(*intrest):
    return(sum(intrest)) / (len(intrest))

print(average(1, 2, 3, 4))

print(average(5, 10, 15, 20, 25, 30, 35))

xList = [3, 5, 9]
print(average(*xList))
