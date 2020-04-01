from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field
from clicktripz.serialize.Array import Array
from clicktripz.openrtb.response.SeatBid import SeatBid


class BidResponse(Serializable):

    """The top-level bid response object.
    The “id” attribute is a reflection of the bid request ID for logging purposes.
    Similarly, “bidid” is an optional response tracking ID for bidders.
    If specified, it can be included in the subsequent win notice call if the bidder wins.
    At least one “seatbid” object is required, which contains a bid on at least one impression.
    Other attributes are optional since an exchange may establish default values.
    """

    #: ID of the bid request to which this is a response.
    id = Field(String, required=True)

    #: Array of seatbid objects; 1+ required if a bid is to be made.
    seatbid = Field(Array(SeatBid), required=True)

    #: Bidder generated response ID to assist with logging/tracking.
    bidid = Field(String)

    #: Bid currency using ISO-4217 alpha codes.
    cur = Field(String)
