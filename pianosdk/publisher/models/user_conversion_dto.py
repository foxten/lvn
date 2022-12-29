from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user import User


class UserConversionDTO(BaseModel):
    user: Optional['User']
    term: Optional['Term']


UserConversionDTO.update_forward_refs()
