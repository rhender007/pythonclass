'''
Created on Nov 15, 2016

@author: Student
'''
# A Set contains an unordered collection of UNIQUE and IMMUTABLE objects.

xSet = set("A Python Tutorial 1234512345")
print(type(xSet))

xList = set(["Perl", "Python", "Java"])
print(xList)

xList1 = set(["Perl", "Python", "Java"])

# Frozen Set
# Although sets are Immutable
cities = set(["Frankfurt", "Basel", "Freiburg"])
cities.add("Strasburg")
print(cities)

cities = frozenset(["Frankfurt", "Basel", "Freiburg"])
cities.add("Strasburg")
print(cities)
