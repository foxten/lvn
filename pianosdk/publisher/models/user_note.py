from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.user import User


class UserNote(BaseModel):
    user_note_id: Optional[str]
    user: Optional['User']
    content: Optional[str]
    type: Optional[str]
    create_date: Optional[str]
    create_by: Optional['User']
    update_date: Optional[str]
    update_by: Optional['User']
    readonly: Optional[bool]


UserNote.update_forward_refs()
