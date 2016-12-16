'''
Created on Dec 6, 2016

@author: Student
'''
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("match.group() :", matchObj.group())
    print("match.group(1) :", matchObj.group(1))
    print("match.group(2) :", matchObj.group(2))
else:
    print("No Match!")