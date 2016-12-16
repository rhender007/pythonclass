'''
Created on Nov 29, 2016

@author: Student
'''
def x_times_y(x, y):
    return x * y

print(x_times_y(2, 3))

dct = {'x':2, 'y': 6}
print(x_times_y(**dct)) # ** indicates a dictionary object