'''
Created on Dec 1, 2016

@author: Student
'''
import shelve

shelveObj = shelve.open("pickles2.dat")
shelveObj["variety"] = ["sweet", "hot", "dill"]
shelveObj["shape"] = ["whole", "spear", "chip"]
shelveObj["brand"] = ["Claussen", "Heinz", "Vlassic"]
shelveObj.sync()

print("Retrieve the data from Shelves")
print("Brand - ", shelveObj["brand"])
print("shape - ", shelveObj["shape"])

shelveObj.close()