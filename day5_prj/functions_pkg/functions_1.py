'''
Created on Nov 22, 2016

@author: Student
'''
'''
def function_name(parameter_list):
    statements -> This is a function body
'''

def fahrenheit(T_in_celsius):
    # Returns the temperature in degree Fahrenheit
    return (T_in_celsius * 9 / 5) + 32
    

#print(fahrenheit(22.6))
#print(fahrenheit(25.8))

for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ":", fahrenheit(t))
