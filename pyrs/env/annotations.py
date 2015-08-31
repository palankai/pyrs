from .configuration import config


def ensure_meta(func, *args, **kwargs):
    meta = getattr(func, config['meta_field'], None)
    if meta is None:
        meta = {}
        setattr(func, config['meta_field'], meta)
    meta.update(*args, **kwargs)
    return meta


def get_meta(func, name=None, default=None):
    meta = ensure_meta(func)
    if name is None:
        return meta
    if name not in meta and default is not None:
        meta[name] = default
    return meta.get(name)


def annotate(_func=None, **kwargs):
    def decorator(_func):
        ensure_meta(_func, kwargs)
        return _func
    if _func is not None:
        return decorator(_func)
    return decorator
