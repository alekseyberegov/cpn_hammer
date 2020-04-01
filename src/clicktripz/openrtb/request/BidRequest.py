from clicktripz.serialize.Field import Field
from clicktripz.serialize.String import String
from clicktripz.serialize.Array import Array
from clicktripz.serialize.Serializable import Serializable

from clicktripz.openrtb.request.Device import Device
from clicktripz.openrtb.request.User import User
from clicktripz.openrtb.request.Site import Site
from clicktripz.openrtb.request.Impression import Impression


class BidRequest(Serializable):
    id = Field(String, required=True)

    bcat = Field(Array(String))

    imp = Field(Impression, required=True)

    site = Field(Site)

    user = Field(User)

    device = Field(Device)
