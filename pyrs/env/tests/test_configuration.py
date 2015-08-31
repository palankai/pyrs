import unittest

from .. import configuration


class TestConfigManager(unittest.TestCase):

    def test_basic(self):
        conf = configuration.Configuration()

        with self.assertRaises(TypeError):
            conf['hello'] = 12

    def test_normal(self):
        class Basic(object):
            a = 12

        conf = configuration.Configuration(Basic)
        self.assertEqual(conf['a'], 12)

    def test_multiple(self):
        class A(object):
            a = 1
            b = 2

        class B(object):
            b = 3
            c = 4

        conf = configuration.Configuration(A, B)
        self.assertEqual(conf['a'], 1)
        self.assertEqual(conf['b'], 3)
        self.assertEqual(conf['c'], 4)

    def test_update(self):
        class A(object):
            a = 1
            b = 2

        class B(object):
            b = 3
            c = 4

        conf = configuration.Configuration(A)
        conf.upgrade(B)
        self.assertEqual(conf['a'], 1)
        self.assertEqual(conf['b'], 3)
        self.assertEqual(conf['c'], 4)
