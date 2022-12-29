from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.churn_prevention_template_version import ChurnPreventionTemplateVersion
from typing import List


class ChurnPreventionEmail(BaseModel):
    email_id: Optional[int]
    email_name: Optional[str]
    template_id: Optional[str]
    versions: Optional['List[ChurnPreventionTemplateVersion]']


ChurnPreventionEmail.update_forward_refs()
