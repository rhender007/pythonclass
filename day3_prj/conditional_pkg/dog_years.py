'''
Created on Nov 15, 2016

@author: Student
'''
age = int(input("Age of the dog: "))
print()
if age < 1:
    print("This can hardly be true!")
elif age == 1:
    print("about 14 human years")
elif age == 2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("Human years: ", human)
    
input('press Return>')
