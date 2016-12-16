'''
Created on Nov 10, 2016

@author: Student
'''
'''
In Java, this is your typical code syntax:

public static void main(String args[]){System.out.println("This is a test");}

'''

from math import sqrt
n = input("Maximum Number?")
n = int(n) + 1
for a in range(1,n):
    for b in range(a,n):
        c_square = a ** 2 + b ** 2
        c = int(sqrt(c_square))
        if ((c_square - c ** 2) == 0):
            print(a,b,c)
