'''
Created on Dec 8, 2016

@author: Student
'''
class parent(object):
    __default = "parent"
    
    def __init__(self, name=None): # This is a constructor
        self.default = name or self.__default
    
    @property    # This is a getter
    def default(self):
        return self.__default
    
    @default.setter
    def default(self, value):
        self.__default = value
    

class child(parent):
    __default = "child"
    

child_a = child()               # This creates the child object
child_a.default                 # 'parent'
child_a._child__default         # 'child'
child_a._parent__default        # 'parent'

child_b = child("orphan")
child_b.default                 # 'orphan'
child_b._child__default         # 'child'
child_b._parent__default        # 'orphan'


    

