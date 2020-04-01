from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field


class Impression(Serializable):
    id = Field(String, required=True)
