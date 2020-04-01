from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field


class Device(Serializable):
    ua = Field(String)

    ip = Field(String)
