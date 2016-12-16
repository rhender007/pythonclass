'''
Created on Dec 6, 2016

@author: Student

^     - Matches the beginning of line
$     - Matches the end of line
.     - Matches single character except newline.
[...] - Matches any single character in brackets
[^...]- Matches any single character not in brackets

'''
import re
print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

