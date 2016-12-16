'''
Created on Nov 17, 2016

@author: Student
'''
n = 100
sumInt = 0
for counter in range(1, n+1):
    sumInt = sumInt + counter
    print("Sum is " + str(sumInt))
    
print("Sum of 1 until %d: %d" % (n,sumInt))