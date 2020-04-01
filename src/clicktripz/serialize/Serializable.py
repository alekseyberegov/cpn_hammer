import json

from clicktripz.serialize.Reflection import add_reflection
from clicktripz.serialize.Reflection import Reflection
from clicktripz.serialize.ValidationError import ValidationError


def serialize(obj):
    if hasattr(obj, 'serialize'):
        return obj.serialize()
    if isinstance(obj, list):
        return list(map(serialize, obj))
    return obj


class Map(dict):
    def __str__(self):
        return json.dumps(self)


@add_reflection(Reflection)
class Serializable(object):

    def __init__(self, **kwargs):
        if not self._required.issubset(kwargs):
            missing = next(name for name in self._required if name not in kwargs)
            raise ValidationError('{}.{} is required'.format(self.__class__.__name__,  missing))
        self.__dict__.update(self._defaults, **kwargs)

    def __getattr__(self, k):
        return None

    @classmethod
    def deserialize(cls, obj):
        data = {}
        func = cls._deserializers.get
        for k, v in iter(obj.items()):
            if v is not None:
                deserialize = func(k)
                data[k] = deserialize(v) if deserialize is not None else v
        return cls(**data)

    def serialize(self):
        attrs = {k: serialize(v) for k, v in iter(self.__dict__.items()) if v is not None}
        return Map(attrs)
