'''
Created on Dec 6, 2016

@author: Student
'''
import re

def test_patterns(text, patterns=[]):
    
    #Show the character positions and input text
    print()
    print(''.join(str(i/10 or ' ') for i in range(len(text))))
    print(''.join(str(i%10) for i in range(len(text))))
    print(text)
    
    # Look for each pattern in the text and print results
    for pattern in patterns:
        print()
        print('Matching "%s"' % pattern)
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            print(' %2d : %2d = "%s"' % (start, end-1, text[start:end]))
    return

if __name__ == '__main__':
    test_patterns('abbababbababababbbb', ['ab'])