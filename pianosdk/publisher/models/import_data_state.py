from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ImportDataState(BaseModel):
    import_data_id: Optional[str]
    import_data_status: Optional[str]


ImportDataState.update_forward_refs()
