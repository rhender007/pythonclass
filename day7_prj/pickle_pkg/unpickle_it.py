'''
Created on Dec 1, 2016

@author: Student
'''
import pickle

print("Unpickle lists")
f = open("pickles.dat", "rb")
varietys = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(varietys)