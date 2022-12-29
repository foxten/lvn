from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CommentAction(BaseModel):
    id: Optional[str]
    caption: Optional[str]


CommentAction.update_forward_refs()
