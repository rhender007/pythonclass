'''
Created on Nov 29, 2016

@author: Student
'''
def getName():
    name = input("Enter the students name ")
    grade1 = input("Enter a grade:")
    grade2 = input("Enter a grade:")
    grade3 = input("Enter a grade:")
    grade4 = input("Enter a grade:")
    return name, grade1, grade2, grade3, grade4

gradeMap = {'A': 4, 'B': 3, 'C': 2, 'D': 1}

def grade2Int(x):
    try:
        return gradeMap[x.upper()]
    except KeyError:
        raise Exception('Invalid grade: ' + x)
    
def getGrades(grades):
    return map(grade2Int, grades)

def calcGpa(grades):
    return sum(grades) / 4.0

def main(name, GPA):
    print("The GPA for ", name, "is", GPA)
    return 0

if __name__ == '__main__':
    name, grade1, grade2, grade3, grade4 = getName()
    grades = getGrades([grade1, grade2, grade3, grade4])
    print(grades)
    GPA = calcGpa(grades)
    main(name, GPA)

