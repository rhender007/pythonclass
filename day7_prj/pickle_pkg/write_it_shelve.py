'''
Created on Dec 1, 2016

@author: Student
'''
import shelve

shelveObj = shelve.open("pickles2.dat", writeback=True)

print(shelveObj["variety"])
shelveObj["variety"]["New_Value"] = "This is a temp data"
print(shelveObj["variety"])
shelveObj.close()

# key1 = input("Enter the key")
# value1 = int(input("Enter the number of values "))
# for x in range(value1):
#     print(shelveObj[key1])
#     val = input("Enter the value")
#     (shelveObj[key1]).append(val)
# print(shelveObj[key1])
# shelveObj.sync()
# shelveObj.close()