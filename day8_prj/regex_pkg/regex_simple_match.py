'''
Created on Dec 6, 2016

@author: Student
'''
import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

start = match.start()
end = match.end()

print('Found "%s" in "%s" from %d to %d ("%s") ' % (match.re.pattern, match.string, start, end, text[start:end]))
