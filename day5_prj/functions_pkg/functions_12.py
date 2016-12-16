'''
Created on Nov 22, 2016

@author: Student
'''
'''
This is a simplified function to check if a certain user has the correct permissions
to access the data.
You could easily modify this to grab the user in session to check if they have
the correct credentials to access a certain route.
Instead of checking if the user is just equal to 'Admin' you could query against
a database or a pickled object then return the correct value.
'''

def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}".format(username, page)
    return inner

current_user = has_permission('Admin Area')
print(current_user)
print(current_user('Admin'))








