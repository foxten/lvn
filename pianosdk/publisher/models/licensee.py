from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.licensee_manager import LicenseeManager
from pianosdk.publisher.models.licensee_representative import LicenseeRepresentative
from typing import List


class Licensee(BaseModel):
    aid: Optional[str]
    licensee_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    representatives: Optional['List[LicenseeRepresentative]']
    managers: Optional['List[LicenseeManager]']


Licensee.update_forward_refs()
