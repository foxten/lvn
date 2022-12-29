from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.locale_model import LocaleModel
from typing import List


class LanguageModel(BaseModel):
    language_name: Optional[str]
    label: Optional[str]
    localized_label: Optional[str]
    locales: Optional['List[LocaleModel]']


LanguageModel.update_forward_refs()
