"""
Context usage:

.. code:: python

    ctx = Context(value=1)
    with ctx:
        call_a_function(ctx=ctx)

A bit more readable version:

.. code:: python

    ctx = Context(value=1)
    with ctx.copy(value=2, new_value=3) as c:
        call_a_function(ctx=c)
"""
import threading


class Context(threading.local):
    """
    This is a thread safe stack based implementation of context.
    """

    def __init__(self, *args, **kwargs):
        super(Context, self).__init__()
        self.clear(*args, **kwargs)
        self.stack = []

    def __getitem__(self, name):
        return self.data[name]

    def __setitem__(self, name, value):
        self.data[name] = value

    def __iter__(self):
        return self.data.__iter__()

    def keys(self):
        return self.data.keys()

    def items(self):
        return self.data.items()

    def copy(self, *args, **kwargs):
        return self.__class__(self.data).update(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.data.update(*args, **kwargs)
        return self

    def clear(self, *args, **kwargs):
        self.data = dict(*args, **kwargs)
        return self

    def _push(self):
        self.stack.append(self.data)
        self.data = self.data.copy()

    def _pop(self):
        self.data = self.stack.pop()

    def __enter__(self):
        self._push()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._pop()

ctx = Context()
