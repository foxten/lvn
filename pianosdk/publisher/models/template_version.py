from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TemplateVersion(BaseModel):
    template_version_id: Optional[str]
    template_id: Optional[str]
    name: Optional[str]
    comment: Optional[str]
    subject: Optional[str]
    body: Optional[str]
    html: Optional[str]
    css: Optional[str]
    version: Optional[int]
    lang: Optional[str]
    published: Optional[bool]
    create_date: Optional[str]
    update_date: Optional[str]
    xdays: Optional[int]


TemplateVersion.update_forward_refs()
