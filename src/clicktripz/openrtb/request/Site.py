from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field
from clicktripz.serialize.Array import Array


class Site(Serializable):
    id = Field(String)

    cat = Field(Array(String))
