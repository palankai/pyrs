"""
Context usage:

.. code:: python

    ctx = Context(value=1)
    with ctx as c:
        call_a_function(ctx=c)

A bit more readable version:

.. code:: python

    ctx = Context(value=1)
    with ctx.copywith(value=2, new_value=3) as c:
        call_a_function(ctx=c)
"""
import contextlib


class Context(dict):
    """
    Context provide basic functionality managing through calls.
    Can be used as a context manager.

    Predefined items: global and local

    .. code:: python

        ctx = Context(value=1, global={'value': 1}, local={'value': 1})

        with ctx.copywith(value=2, new_value=3) as c:
            ctx['global']['value']  # contains 1
            ctx['local']  # It's an empty dict
            call_a_function(ctx=c)

    """

    def __init__(self, *args, **kwargs):
        super(Context, self).__init__(*args, **kwargs)
        if 'global' not in self:
            self['global'] = {}
        if 'local' not in self:
            self['local'] = {}

    def __enter__(self):
        cp = self.copy()
        cp['local'] = {}
        return cp

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @contextlib.contextmanager
    def copywith(self, *args, **kwargs):
        """Make a copy of itself and pass back to inside context.

        **Cauction:** It uses simple a `dict.copy` means and if any item itself
        mutable, there is reflecting outside from the context manager as well.
        *Use immutable values if it's possible!*
        """
        with self as copied:
            copied.update(*args, **kwargs)
            yield copied
