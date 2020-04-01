from clicktripz.serialize.Field import Field
from clicktripz.serialize.String import String
from clicktripz.serialize.Array import Array
from clicktripz.serialize.Serializable import Serializable


class BidRequest:
    id = Field(String)

    bcat = Field(Array(String))

    imp = Field(Serializable)

    site = Field(Serializable)

    user = Field(Serializable)

    def __init__(self):
        pass
