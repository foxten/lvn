from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Any
from typing import Dict
from typing import List


class UserDto(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    personal_name: Optional[str]
    uid: Optional[str]
    image1: Optional[str]
    create_date: Optional[datetime]
    reset_password_email_sent: Optional[bool]
    custom_fields: Optional['List[Dict[str, Any]]']


UserDto.update_forward_refs()
