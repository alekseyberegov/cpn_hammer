from clicktripz.serialize.Serializable import Serializable
from clicktripz.serialize.String import String
from clicktripz.serialize.Field import Field
from clicktripz.serialize.Array import Array
from decimal import Decimal

class Bid(Serializable):

    """At least one bid object is required in a bid set object.
    For each bid, the “nurl” attribute contains the win notice URL.
    If the bidder wins the impression, the exchange calls this notice URL
        a) to inform the bidder of the win and
        b) to convey certain information using substitution macros.
    The “adomain” attribute can be used to check advertiser block list compliance.
    The “iurl” attribute can provide a link to an image that is representative of the campaign’s
    content (irrespective of whether the campaign may have multiple creatives).
    This enables human review for spotting inappropriate content.
    The “cid” attribute can be used to block ads that were previously identified as inappropriate;
    essentially a safety net beyond the block lists.
    The “crid” attribute can be helpful in reporting creative issues back to bidders.
    Finally, the “attr” array indicates the creative attributes that describe the ad to be served.
    """

    #: Bidder generated bid ID to assist with logging/tracking.
    id = Field(String, required=True)

    #: ID of the Imp object in the related bid request.
    impid = Field(String, required=True)

    #: Bid price expressed as CPM although the actual transaction is for a
    #: unit impression only. Note that while the type indicates float, integer
    #: math is highly recommended when handling currencies (e.g., BigDecimal in
    #: Java).
    price = Field(Decimal, required=True)

    #: ID of a preloaded ad to be served if the bid wins.
    adid = Field(String)

    #: Win notice URL called by the exchange if the bid wins; optional means
    #: of serving ad markup.
    nurl = Field(String)

    #: Optional means of conveying ad markup in case the bid wins; supersedes
    #: the win notice if markup is included in both.
    adm = Field(String)

    #: Advertiser domain for block list checking (e.g., “ford.com”). This can
    #: be an array of for the case of rotating creatives. Exchanges can mandate
    #: that only one domain is allowed.
    adomain = Field(Array(String))

    #: Bundle or package name (e.g., com.foo.mygame) of the app being
    #: advertised, if applicable; intended to be a unique ID across exchanges.
    bundle = Field(String)

    #: URL without cache-busting to an image that is representative of the
    #: content of the campaign for ad quality/safety checking.
    iurl = Field(String)

    #: Campaign ID to assist with ad quality checking; the collection of
    #: creatives for which iurl should be representative.
    cid = Field(String)

    #: Creative ID to assist with ad quality checking.
    crid = Field(String)

    #: IAB content categories of the creative. Refer to List 5.1.
    cat = Field(Array(String))

    #: Reference to the deal.id from the bid request if this bid pertains to a
    #: private marketplace direct deal.
    dealid = Field(String)

    #: Height of the creative in pixels.
    h = Field(int)

    #: Width of the creative in pixels.
    w = Field(int)
