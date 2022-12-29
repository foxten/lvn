from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.import_section import ImportSection
from typing import List


class ImportData(BaseModel):
    import_data_id: Optional[str]
    import_data_status: Optional[str]
    sections: Optional['List[ImportSection]']


ImportData.update_forward_refs()
