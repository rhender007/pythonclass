'''
Created on Nov 15, 2016

@author: Student
'''
x = {"a", "b", "c", "d", "e"}
x.discard("a")
x.discard("z")
print(x)

# We will use remove method - Similar to discard
x = {"a", "b", "c", "d", "e"}
x.remove("a")
print(x)
x.remove("z")