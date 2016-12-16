'''
Created on Nov 17, 2016

@author: Student
'''
a = 0
b = 1
count = 0
max_count = 5
arrayList = []

while count < max_count:
    count = count + 1
    print(a, b, end=" ") # This keeps the print from creating a new line
    a = a + b
    b = a + b
print()