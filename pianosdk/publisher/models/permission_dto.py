from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class PermissionDTO(BaseModel):
    title: Optional[str]
    descr: Optional[str]
    mnemonic: Optional[str]
    defaults: Optional[List[str]]


PermissionDTO.update_forward_refs()
