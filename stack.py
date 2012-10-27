'''
python stack implementation

@author: jvallver [jvallver@gmail.com]
'''

class EmptyStackError(Exception): pass

class stack(object):
    
    def __init__(self):
        self.__head = None
    
    def push(self, value):
        self.__head = _StackItem(value, self.__head)
    
    def pop(self):
        if self.__head is None: raise EmptyStackError("The stack is empty!")
        value = self.__head.value
        self.__head = self.__head.nextItem
        return value
    
    def isEmpty(self):
        return self.__head is None
    
    def __str__(self):
        currentItem = self.__head
        string = ""
        while currentItem:
            if type(currentItem.value) is str:
                string += "'{0}'".format(currentItem.value)
            else:
                string += str(currentItem.value)
            currentItem = currentItem.nextItem
            if currentItem:
                string += ", "
        return "[{0}]".format(string)

class _StackItem():
    
    def __init__(self, value, nextItem):
        self.__value = value
        self.__nextItem = nextItem
    
    @property
    def value(self):
        return self.__value
    
    @property
    def nextItem(self):
        return self.__nextItem