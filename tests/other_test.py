__author__ = 'rafaeuoliveira'

import unittest


class OtherTest(unittest.TestCase):

    def test_opa(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        c = a[0:3] + a[6:len(a)]

        print c

    def test_opa2(self):
        T().add(5, 6, 7, 8, 9)

    def test_mult_for(self):
        doubles = [2 * n for n in range(5)]
        s = T().add(*doubles)
        print s

    def test_inner_value(self):
        v = {'3':0}
        T().update(v)

        print v

class T(object):
    def add(self, *pe):
        c = [1, 2, 3, 4]
        c.extend(pe)

    def update(self, value):
        value.update({'3':9})

class I(object):
    def __iter__(self):
        return iter([1,2,3,4])

    def __repr__(self):
        return " ".join(str(t) for t in [1,2,3,4])