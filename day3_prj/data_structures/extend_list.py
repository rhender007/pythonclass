'''
Created on Nov 15, 2016

@author: Student
'''
lst = [42, 98, 77]
lst2 = [8, 9]
lst.append(lst2)
print(lst)

# Using extend operation now:

lst = [42, 98, 77]
lst2 = [8, 9]
lst.extend(lst2)
print(lst)