from Field import Field


def add_reflection(metaclass):
    def wrapper(cls):
        attrs = cls.__dict__.copy()
        slots = attrs.get('__slots__')
        if slots is not None:
            if isinstance(slots, str):
                slots = [slots]
            for a in slots:
                attrs.pop(a)
        attrs.pop('__dict__', None)
        attrs.pop('__weakref__', None)
        if hasattr(cls, '__qualname__'):
            attrs['__qualname__'] = cls.__qualname__
        return metaclass(cls.__name__, cls.__bases__, attrs)
    return wrapper


class Reflection(type):
    def __init__(cls, name, bases, attrs):
        super(Reflection, cls).__init__(name, bases, attrs)
        named_fields = [item for item in iter(attrs) if isinstance(item[1], Field)]
        cls._deserializers = {name: field.deserialize for name, field in named_fields}
        cls._defaults = {name: field.default for name, field in named_fields}
        cls._required = {name for name, field in named_fields if field.required}
