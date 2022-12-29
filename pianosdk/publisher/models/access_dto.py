from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.resource_dto import ResourceDto
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user_dto import UserDto


class AccessDTO(BaseModel):
    access_id: Optional[str]
    parent_access_id: Optional[str]
    granted: Optional[bool]
    resource: Optional['ResourceDto']
    user: Optional['UserDto']
    expire_date: Optional[datetime]
    start_date: Optional[datetime]
    can_revoke_access: Optional[bool]
    custom_data: Optional[str]
    term: Optional['Term']


AccessDTO.update_forward_refs()
