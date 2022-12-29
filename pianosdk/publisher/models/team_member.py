from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class TeamMember(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    email: Optional[str]
    uid: Optional[str]
    create_date: Optional[datetime]
    last_login: Optional[datetime]
    invitation_expired: Optional[bool]
    permissions: Optional[List[str]]


TeamMember.update_forward_refs()
