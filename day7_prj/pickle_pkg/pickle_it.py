'''
Created on Dec 1, 2016

@author: Student
'''
import pickle

print("Pickling lists")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

file = open("pickles.dat", "wb") 

pickle.dump(variety, file)
pickle.dump(shape, file)
pickle.dump(brand, file)

file.close()