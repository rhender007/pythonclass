'''
Created on Nov 22, 2016

@author: Student
'''
def factorial(number):
    # Error Handling
    if not isinstance(number, int):
        raise TypeError("Sorry. Number must be Integer")
    if not number >= 0:
        raise ValueError("Sorry. Number must be zero or positive")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number -1)
    return inner_factorial(number)

# Call the outer function
print(factorial(4))
