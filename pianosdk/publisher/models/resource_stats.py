from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ResourceStats(BaseModel):
    rid: Optional[str]
    num_bundles: Optional[int]
    num_customers: Optional[int]
    num_terms: Optional[int]
    tags: Optional[str]


ResourceStats.update_forward_refs()
