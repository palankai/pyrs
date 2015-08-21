import unittest

from .. import base


class TestContext(unittest.TestCase):

    def test_basic_usage(self):
        ctx = base.Context()
        ctx['something'] = 'test'

        self.assertEqual(ctx['something'], 'test')

    def test_global_exists(self):
        ctx = base.Context()

        self.assertEqual(ctx['global'], {})

    def test_context_manager(self):
        ctx = base.Context()
        ctx['something'] = 'test'
        ctx['over'] = 'test'

        with ctx as ictx:
            ictx['else'] = 'else'
            ictx['over'] = 'over'

        self.assertNotIn('else', ctx)
        self.assertEqual(ctx['something'], 'test')
        self.assertEqual(ictx['over'], 'over')
        self.assertEqual(ctx['over'], 'test')

    def test_context_manager_copywith(self):
        ctx = base.Context()
        ctx['something'] = 'test'
        ctx['over'] = 'test'

        with ctx.copywith() as ictx:
            ictx['else'] = 'else'
            ictx['over'] = 'over'

        self.assertNotIn('else', ctx)
        self.assertEqual(ctx['something'], 'test')
        self.assertEqual(ictx['over'], 'over')
        self.assertEqual(ctx['over'], 'test')

    def test_context_manager_global_behaviour(self):
        ctx = base.Context()
        ctx['global']['x'] = 1

        with ctx as ictx:
            ictx['global']['x'] = 2

        self.assertEqual(ctx['global'], {'x': 2})

    def test_context_manager_local_behaviour(self):
        ctx = base.Context()
        ctx['local']['x'] = 1

        with ctx as ictx:
            ictx['local']['y'] = 1

        self.assertEqual(ctx['local'], {'x': 1})
        self.assertEqual(ictx['local'], {'y': 1})
