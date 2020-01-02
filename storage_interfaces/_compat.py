# pylint: disable=undefined-variable,import-error,exec-used,redefined-builtin
import sys

PY2 = sys.version_info[0] == 2

if PY2:
    exec("""def with_metaclass(meta):
    class _WithMetaclassBase(object):
        __metaclass__ = meta
    return _WithMetaclassBase
""")
else:
    exec("""def with_metaclass(meta):
    class _WithMetaclassBase(object, metaclass=meta):
        pass
    return _WithMetaclassBase
""")

if PY2:

    string_types = (basestring,)

    import __builtin__ as _builtins

    def iteritems(d):
        return d.iteritems()  # not dict.iteritems!!!
                              # we support ordered dicts as well

    def items(d):
        return d.items()

    def itervalues(d):
        return d.itervalues()

    xrange = _builtins.xrange
else:

    string_types = (str,)

    import builtins as _builtins

    xrange = range

    def iteritems(d):
        return iter(d.items())

    def items(d):
        return list(d.items())  # python3.3 dict.items() returns dictitems
                                # type instead of list of tuples, as python2.x

    def itervalues(d):
        return iter(d.values())
