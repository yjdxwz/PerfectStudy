"""
Testing ``AutoFillDict``::

    >>> adict = AutoFillDict()
    >>> len(adict)
    0
    >>> adict['first']
    0
    >>> adict
    {'first': 0}
    >>> adict['second']
    1
    >>> adict['third']
    2
    >>> len(adict)
    3
    >>> adict
    {'first': 0, 'second': 1, 'third': 2}
    >>> adict['__magic__']
    Traceback (most recent call last):
      ...
    KeyError: '__magic__'

Testing ``MicroEnum``::

    >>> class Flavor(MicroEnum):
    ...     cocoa
    ...     coconut
    ...     vanilla
    >>> Flavor.cocoa, Flavor.vanilla
    (0, 2)
    >>> Flavor[1]
    'coconut'
"""


class AutoFillDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__next_value = 0

    def __missing__(self, key):
        if key.startswith('__') and key.endswith('__'):
            raise KeyError(key)
        self[key] = value = self.__next_value
        self.__next_value += 1
        return value


class MicroEnumMeta(type):
    def __prepare__(name, bases, **kwargs):
        return AutoFillDict()

    def __getitem__(cls, key):
        for k, v in cls.__dict__.items():
            if v == key:
                return k
        raise KeyError(key)


class MicroEnum(metaclass=MicroEnumMeta):
    pass
