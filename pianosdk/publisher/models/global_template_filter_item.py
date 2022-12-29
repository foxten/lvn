from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.global_template_filter_sub_item import GlobalTemplateFilterSubItem
from typing import List


class GlobalTemplateFilterItem(BaseModel):
    id: Optional[str]
    name: Optional[str]
    counter_value: Optional[int]
    global_template_filter_sub_items: Optional['List[GlobalTemplateFilterSubItem]']


GlobalTemplateFilterItem.update_forward_refs()
