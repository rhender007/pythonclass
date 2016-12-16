'''
Created on Nov 15, 2016

@author: Student
'''
person = input("Nationality? ")
globalVar = "Testing"
if person == "french" or person == "French" :
    print("French" + globalVar)  # Statement block
elif person == "italian" or person == "Italian":
    print("Italian" + globalVar)  # Statement block
else:
    print("You speak english?" + globalVar)