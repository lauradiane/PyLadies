#!/usr/bin/env python

# Some resources:
# Automated Testing: http://learnpythonthehardway.org/book/ex47.html
# unittest module in Python: http://docs.python.org/2/library/unittest.html
# Nose testing: https://nose.readthedocs.org/en/latest/

class SampleClass(object):

    def __init__(self):
        self._mylist = [ 'one', 'two', 'three', 'four', 'five' ]

    def mylist(self):
        return self._mylist

    def myname(self):
        return "Laura"

    def add_myname_to_mylist(self):
        l = self.mylist()
        name = self.myname()
        l.append(name)
        return l

    def add_to_mylist(self, element):
        l = self.mylist()
        l.append(element)
        return l
