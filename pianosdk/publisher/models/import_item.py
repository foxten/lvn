from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.variant_item import VariantItem
from pianosdk.publisher.models.version_item import VersionItem
from typing import List


class ImportItem(BaseModel):
    item_id: Optional[str]
    name: Optional[str]
    action: Optional[str]
    import_result: Optional[str]
    update_date: Optional[int]
    count_variants: Optional[int]
    variant_list: Optional['List[VariantItem]']
    version: Optional[int]
    version_list: Optional['List[VersionItem]']


ImportItem.update_forward_refs()
