'''
Created on Nov 29, 2016

@author: Student

You might ask yourself, why we used both a positional parameter "x" and
the variable parameter "*l" in our function definition. We could have only used
*l to contain all our numbers. The idea is that we wanted to enforce that we 
always have a non-empty list of numbers. This is necessary to prevent a division
by zero error, because the average of an empty list of numbers is not defined.

'''

def arithmetic_mean(x, *l):
    """
    This function calculates the arithmetic mean of a non-empty
    arbitrary number of numbers
    """
    sum = x
    for i in l:
        sum += i
    
    return sum / (1.0 + len(l))