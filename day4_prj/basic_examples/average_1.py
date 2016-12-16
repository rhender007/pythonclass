'''
Created on Nov 17, 2016

@author: Student
'''
count = 0
sum = 0.0
number = 1 # Used to set to something that will not exit the while loop immediately

print("Enter 0 to exit the loop")

while number != 0:
    number = float(input("Enter a number: "))
    if number != 0:
        count = count + 1
        sum = sum + number
    if number == 0:
        print("The average was: ", sum / count)