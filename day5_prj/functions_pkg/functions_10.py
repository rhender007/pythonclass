'''
Created on Nov 22, 2016

@author: Student
'''
# Recursion function: A function calling itself

def factorial(n):
    print("factorial has been called with n=" + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        print("Intermediate result for ", n, " * factorial(", n-1, "):", res)
        return res
    
print(factorial(5))
