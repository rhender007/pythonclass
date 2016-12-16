'''
Created on Dec 1, 2016

@author: Student
'''
import shelve

shelveObj = shelve.open("shelve_obj.db")
try:
    shelveObj["key1"] = {"int": 10, "float": 9.5, "string": "Sample Data"}
finally:
    shelveObj.close()