import threading
import unittest


from .. import base


class TestContext(unittest.TestCase):

    def test_basic_usage(self):
        ctx = base.Context()
        ctx['something'] = 'test'

        self.assertEqual(ctx['something'], 'test')

    def test_context_manager_global_behaviour(self):
        ctx = base.Context({'global': {}})
        ctx['global']['x'] = 1

        with ctx as ictx:
            ictx['global']['x'] = 2

        self.assertEqual(ctx['global'], {'x': 2})

    def test_with_other_thread(self):
        ctx = base.Context()
        ctx['exists'] = 1
        ctx['obj'] = [1, 2, 3]

        def other_thread():
            ctx['obj'] = [1, 2, 3, 4]
            ctx['other'] = 1
            ctx['exists'] = 2
        t = threading.Thread(target=other_thread)
        t.start()
        t.join()
        self.assertNotIn('other', ctx)
        self.assertEqual(ctx['exists'], 1)
        self.assertEqual(ctx['obj'], [1, 2, 3])

    def test_dictlike(self):
        dl = base.Context()
        dl['aaa'] = 12

        self.assertEqual(dict(dl), {'aaa': 12})

    def test_context_manager_copywith(self):
        ctx = base.Context()
        ctx.clear()
        ctx['something'] = 'test'
        ctx['over'] = 'test'
        ctx['obj'] = [1, 2, 3]

        with ctx.copy(justhere='a') as ictx:
            ictx['else'] = 'else'
            ictx['over'] = 'over'
            ictx['obj'] = [1, 2, 3, 4]
            self.assertEqual(ictx['something'], 'test')
            self.assertEqual(ictx['justhere'], 'a')

        self.assertNotIn('else', ctx)
        self.assertNotIn('justhere', ctx)
        self.assertEqual(ctx['obj'], [1, 2, 3])
        self.assertEqual(ctx['something'], 'test')
        self.assertEqual(ctx['over'], 'test')
