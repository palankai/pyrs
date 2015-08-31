from .. import conf as _pyrs_config


class Configuration(object):

    def __init__(self, *bases):
        self._conf = dict()
        for base in bases:
            self.upgrade(base)

    def upgrade(self, base):
        for k in dir(base):
            if not k.startswith('_'):
                self._conf[k] = getattr(base, k)

    def __getitem__(self, name):
        return self._conf[name]

    def __iter__(self):
        return self._conf.__iter__()

    def __len__(self):
        return len(self.data)

    def get(self, name, default=None):
        return self._conf.get(name, default)

    def keys(self):
        return self._conf.keys()

    def items(self):
        return self._conf.items()


config = Configuration(_pyrs_config)
