from clicktripz.serialize.Field import get_deserializer


class Array(object):
    def __init__(self, field_type):
        self.deserializer = get_deserializer(field_type)

    def deserialize(self, value):
        return list(map(self.deserializer, (value or ())))
