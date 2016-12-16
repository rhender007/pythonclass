'''
Created on Nov 17, 2016

@author: Student
'''
sum = 0.0

print("This program will take several numbers then average them")
count = int(input("How many numbers would you like to average: "))

start_count = 0
print("start_count", start_count)
print("count", count)
while start_count < count:
    start_count = start_count + 1
    print("Number", start_count)
    number = float(input("Enter a number: "))
    sum = sum + number
    
print("Average", sum / count)
print("Average using Start count", sum / start_count)
