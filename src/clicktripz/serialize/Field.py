
import ValidationError


def get_deserializer(field_type):
    if hasattr(field_type, 'deserialize'):
        return field_type.deserialize

    def deserialize(value):
        try:
            return field_type(value)
        except (ValueError, TypeError):
            raise ValidationError('should be convertible to {}, got {} instead'.format(field_type, type(value)))
    return deserialize


class Field(object):
    def __init__(self, field_type, required=False, default=None):
        self.deserialize = get_deserializer(field_type)
        self.required = required
        self.default = default
