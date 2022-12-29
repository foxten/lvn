from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.link_term_conversion_params import LinkTermConversionParams
from pianosdk.publisher.models.link_term_session_params import LinkTermSessionParams
from pianosdk.publisher.models.link_term_subscription_params import LinkTermSubscriptionParams


class LinkTermEventRequest(BaseModel):
    session: Optional['LinkTermSessionParams']
    subscription: Optional['LinkTermSubscriptionParams']
    conversion: Optional['LinkTermConversionParams']


LinkTermEventRequest.update_forward_refs()
