'''
Created on Nov 17, 2016

@author: Student

The items of the sequence object are assigned one after the other to
the loop variable. To be precise the variable points to the items.
For each item the loop body is executed.

'''
edibles = ["ham", "spam", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad,: No Spam")
print("Finally, I finished stuffing myself")