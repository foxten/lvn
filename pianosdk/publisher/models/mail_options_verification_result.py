from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class MailOptionsVerificationResult(BaseModel):
    dkim: Optional[bool]
    dkim_tokens: Optional[List[str]]
    spf: Optional[bool]
    spf_record: Optional[str]
    txt: Optional[bool]
    txt_token: Optional[str]
    email_verify_status: Optional[str]
    verified_email: Optional[str]
    email_provider: Optional[str]
    email_domain_verified: Optional[bool]


MailOptionsVerificationResult.update_forward_refs()
