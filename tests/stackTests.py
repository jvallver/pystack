'''
unittest for stack class

@author: jvallver [jvallver@gmail.com]
'''

import unittest
from stack import stack, EmptyStackError

class stackTests(unittest.TestCase):
    
    def _getStackInstance(self):
        return stack()
    
    def _doPushTest(self, elements):
        myStack = self._getStackInstance()
        for element in elements:
            myStack.push(element)
        expected = str(elements[::-1])
        self.assertEquals(expected, str(myStack))
    
    def test_push_called_putTheElementOnTheStackCorrectly(self):
        self._doPushTest(["dummy element"])
    def test_push_calledTwoTimes_putTheElementsOnTheStackCorrectly(self):
        self._doPushTest(["dummy element1", "dummy element2"])
    
    def test_pop_called_returnFirstStackItem(self):
        myStack = self._getStackInstance()
        myElement = "element"
        myStack.push(myElement)
        actual = myStack.pop()
        self.assertEquals(myElement, actual)
    def test_pop_calledWithEmptyStack_raiseEmptyStackError(self):
        self.assertRaises(EmptyStackError, self._getStackInstance().pop)
    
    def _doIsEmptyTest(self, element, expected):
        myStack = self._getStackInstance()
        if element: myStack.push(element)
        actual = myStack.isEmpty()
        self.assertEquals(actual, expected)
    
    def test_isEmpty_calledWithNonEmptyStack_returnFalse(self):
        self._doIsEmptyTest("element", False)
    
    def test_isEmpty_calledWithEmptyStack_returnTrue(self):
        self._doIsEmptyTest(None, True)

if __name__ == "__main__":
    unittest.main()
