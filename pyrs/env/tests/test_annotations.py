import unittest

from .. import annotations
from .. import config


class TestMeta(unittest.TestCase):

    def test_ensure_meta(self):
        def func():
            pass

        meta = annotations.ensure_meta(func)

        self.assertIsInstance(meta, dict)
        self.assertEqual(meta, {})

    def test_ensure_meta_with_defined_attrs(self):
        def func():
            pass

        meta = annotations.ensure_meta(func, name='myfunc')

        self.assertIsInstance(meta, dict)
        self.assertEqual(meta, {'name': 'myfunc'})

    def test_get_meta(self):
        def func():
            pass

        annotations.ensure_meta(func, name='myfunc')
        meta = annotations.get_meta(func)

        self.assertIsInstance(meta, dict)
        self.assertEqual(meta, {'name': 'myfunc'})

    def test_get_meta_field(self):
        def func():
            pass

        annotations.ensure_meta(func, name='myfunc')
        field = annotations.get_meta(func, 'name')

        self.assertEqual(field, 'myfunc')

    def test_get_meta_field_default_none(self):
        def func():
            pass

        field = annotations.get_meta(func, 'name')

        self.assertIsNone(field)
        self.assertNotIn('name', annotations.get_meta(func))

    def test_get_meta_field_default_value(self):
        def func():
            pass

        field = annotations.get_meta(func, 'name', 'myfunc')

        self.assertEqual(field, 'myfunc')
        self.assertIn('name', annotations.get_meta(func))
        self.assertEqual(annotations.get_meta(func, 'name'), 'myfunc')

    def test_get_meta_field_default_list(self):
        def func():
            pass

        annotations.get_meta(func, 'list', []).append('12')

        self.assertEqual(annotations.get_meta(func, 'list'), ['12'])


class TestAnnotate(unittest.TestCase):

    def test_annotation_basic(self):
        @annotations.annotate
        def func():
            pass

        self.assertEqual(getattr(func, config['meta_field']), {})

    def test_annotation_with_kwargs(self):
        @annotations.annotate(name='myfunc')
        def func():
            pass

        self.assertEqual(
            getattr(func, config['meta_field']), {'name': 'myfunc'}
        )
