from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Config(BaseModel):
    aid: Optional[str]
    config_id: Optional[int]
    name: Optional[str]
    create_date: Optional[datetime]
    update_date: Optional[datetime]


Config.update_forward_refs()
