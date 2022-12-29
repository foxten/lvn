from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class TermTypeDTO(BaseModel):
    type_id: Optional[str]
    type_name: Optional[str]
    type_enum_name: Optional[str]


TermTypeDTO.update_forward_refs()
