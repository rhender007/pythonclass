'''
Created on Dec 8, 2016

@author: Student
'''
from HistoryBook import HistoryBook

historyBook = HistoryBook("Hamlet", "Shakespeare", 1500)
historyBook.displayCompleteInfo()

print(historyBook.calculateYearsFromRelease(1500))