'''
Created on Nov 22, 2016

@author: Student
'''
# Multiple function parameters

def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)
    
def main():
    sumProblem(2, 3)
    sumProblem(1234567899, 34349639643)
    a = int(input("Enter an Integer: "))
    b = int(input("Enter another Integer"))
    sumProblem(a, b)
    
main()