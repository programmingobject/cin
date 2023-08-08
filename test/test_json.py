# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116


"json"


import unittest


from opr.decoder import loads
from opr.encoder import dumps
from opr.objects import Object
from opr.persist import Persist


VALIDJSON = "{'test': 'bla'}"
VALIDPYTHON = '{"test": "bla"}'


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")


class TestEncoder(unittest.TestCase):

    def test_dumps(self):
        obj = Object()
        obj.test = "bla"
        print(dumps(obj))
        self.assertEqual(dumps(obj), VALIDPYTHON)
