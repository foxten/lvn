from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class RegionSimpleModel(BaseModel):
    region_name: Optional[str]
    pub_id: Optional[str]


RegionSimpleModel.update_forward_refs()
