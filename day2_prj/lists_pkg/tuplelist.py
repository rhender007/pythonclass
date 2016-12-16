'''
Created on Nov 10, 2016

@author: Student
'''
tupleStr = ("tuples", "are", "immutable")

print(tupleStr[0])

# Assignment to tuples are not allowed

#tupleStr[0] = "gw"

tuple_mutate = ([1,2,3], [3,2,1])
print(tuple_mutate[0])
tuple_mutate[0][0] = 10
print(tuple_mutate)