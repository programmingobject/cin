# This file is placed in the Public Domain.
#
# pylint: disable=C0103,C0115,C0116,R0903


"inheritence"


import unittest


from opr.objects import Object
from opr.persist import Persist

class A(Object):

    pass


class B(Object):

    pass


class C(A, B):

    bla = "mekker"


class D:

    pass


class E(A, D):

    pass


class F(C, D):

    pass


class H(dict):

    pass


class I(object):

   pass


class J(A, I):

   pass


class K(J, H):

   pass


class Persisted(A, Persist):

   pass


class TestInherit(unittest.TestCase):

    def testinherit1(self):
        c = C()
        self.assertEqual(type(c), C)

    def testinherit2(self):
        e = E()
        self.assertEqual(type(e), E)

    def testinherit3(self):
        f = F()
        self.assertEqual(type(f), F)

    def testinherit4(self):
        f = F()
        self.assertEqual(f.bla, "mekker")

    def testinherit5(self):
        h = H()
        self.assertEqual(type(h), H)

    def testinherit6(self):
        i = I()
        self.assertEqual(type(i), I)

    def testinherit5(self):
        j = J()
        self.assertEqual(type(j), J)

    def testinherit5(self):
        k = K()
        self.assertEqual(type(k), K)

    def testinheritpersist(self):
       per = Persisted()
       self.assertTrue(per.__oid__)
