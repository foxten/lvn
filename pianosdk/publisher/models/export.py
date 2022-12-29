from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Export(BaseModel):
    export_id: Optional[str]
    export_name: Optional[str]
    export_created: Optional[datetime]
    export_completed: Optional[datetime]
    export_percentage: Optional[int]
    export_records: Optional[int]
    export_status: Optional[str]
    report_type: Optional[str]
    export_updated: Optional[datetime]
    export_repeatable: Optional[bool]
    filter_data: Optional[str]


Export.update_forward_refs()
