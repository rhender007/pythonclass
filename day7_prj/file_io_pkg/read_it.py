'''
Created on Dec 1, 2016

@author: Student
'''
print("Reading from a newly created file")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()