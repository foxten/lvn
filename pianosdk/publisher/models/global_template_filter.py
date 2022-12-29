from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.global_template_filter_item import GlobalTemplateFilterItem


class GlobalTemplateFilter(BaseModel):
    template_status: Optional['GlobalTemplateFilterItem']
    template_type: Optional['GlobalTemplateFilterItem']
    use_case: Optional['GlobalTemplateFilterItem']
    deployment_status: Optional['GlobalTemplateFilterItem']


GlobalTemplateFilter.update_forward_refs()
