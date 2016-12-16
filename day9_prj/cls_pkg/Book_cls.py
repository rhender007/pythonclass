'''
Created on Dec 8, 2016

@author: Student
'''
class Book:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    def getBasicInformation(self):
        return "Name:" + self.name + ", Author: " + self.author
    
    def calculateYearsFromRelease(self, year):
        return(2016 - year)