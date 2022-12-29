from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.resource import Resource
from pianosdk.publisher.models.term import Term
from pianosdk.publisher.models.user import User


class Access(BaseModel):
    access_id: Optional[str]
    parent_access_id: Optional[str]
    granted: Optional[bool]
    revoked: Optional[bool]
    resource: Optional['Resource']
    user: Optional['User']
    expire_date: Optional[datetime]
    start_date: Optional[datetime]
    can_revoke_access: Optional[bool]
    term: Optional['Term']


Access.update_forward_refs()
