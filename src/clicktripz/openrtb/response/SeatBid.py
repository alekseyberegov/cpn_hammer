from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field
from clicktripz.serialize.Array import Array

from clicktripz.openrtb.response.Bid import Bid


class SeatBid(Serializable):

    """At least one seatbid object is required in a bid response object.
    A bid response can contain multiple “seatbid” objects, each on behalf of a different bidder seat.
    Since a bid request can include multiple impressions,
    each “seatbid” object can contain multiple bids each pertaining to a different impression on behalf of a seat.
    Thus, each “bid” object must include the impression ID to which it pertains as well as the bid price.
    The “group” attribute can be used to specify if a seat is willing to accept
    any impressions that it can win (default) or if it is only interested
    in winning any if it can win them all (i.e., all or nothing).
    """

    #: Array of 1+ Bid objects (Section 4.2.3) each related to an impression.
    #: Multiple bids can relate to the same impression.
    bid = Field(Array(Bid), required=True)

    #: ID of the bidder seat on whose behalf this bid is made.
    seat = Field(String)


