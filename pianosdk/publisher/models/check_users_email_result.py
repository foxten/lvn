from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.import_user import ImportUser
from typing import List


class CheckUsersEmailResult(BaseModel):
    existing_emails: Optional['List[ImportUser]']
    existing_but_not_bounded_emails: Optional['List[ImportUser]']
    new_emails: Optional['List[ImportUser]']
    invalid_emails: Optional['List[ImportUser]']


CheckUsersEmailResult.update_forward_refs()
