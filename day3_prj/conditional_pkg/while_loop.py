'''
Created on Nov 15, 2016

@author: Student
'''
'''
The following script calculates the sum of the numbers from 1 to 100.
We will have a better way to do this later.
'''

n = 100
s = 0
counter = 1
while counter <= n:
    s = s + counter
    counter += 1
    
print("Sum of 1 until %d: %d" % (n,s))