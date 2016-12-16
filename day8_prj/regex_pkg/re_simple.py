'''
Created on Dec 6, 2016

@author: Student
'''
import re

patterns = ['this', 'that']
text = 'Does this and this match the pattern?'

for pattern in patterns:
    print('Looking for "%s" in "%s"' % (pattern, text))
    
    if re.search(pattern, text):
        print("Found match!")
    else:
        print("No Match")