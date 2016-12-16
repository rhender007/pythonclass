'''
Created on Dec 1, 2016

@author: Student
'''
import shelve

shelveObj =shelve.open("shelve_obj.db", writeback = True) 
try:
    print(shelveObj["key1"])
    shelveObj["key1"]["new_value"] = "This is a new Data"
finally:
    shelveObj.close()