from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Experience(BaseModel):
    experience_id: Optional[str]
    aid: Optional[str]
    type: Optional[str]
    cover_image_url: Optional[str]
    title: Optional[str]
    description: Optional[str]
    model: Optional[str]
    draft: Optional[str]
    draft_date: Optional[datetime]
    draft_base_version: Optional[int]
    create_date: Optional[datetime]
    create_by: Optional[str]
    update_date: Optional[datetime]
    update_by: Optional[str]
    version: Optional[int]
    schedule: Optional[str]
    status: Optional[str]
    hierarchy_type: Optional[str]
    parent_id: Optional[str]


Experience.update_forward_refs()
