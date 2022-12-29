from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.import_item import ImportItem
from typing import List


class ImportSection(BaseModel):
    id: Optional[str]
    name: Optional[str]
    import_list_items: Optional['List[ImportItem]']


ImportSection.update_forward_refs()
