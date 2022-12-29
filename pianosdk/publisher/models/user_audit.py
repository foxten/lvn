from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.audit_changed_field_dto import AuditChangedFieldDto
from typing import List


class UserAudit(BaseModel):
    user_audit_id: Optional[str]
    uid: Optional[str]
    session_id: Optional[str]
    country_name: Optional[str]
    city: Optional[str]
    user_agent: Optional[str]
    visited: Optional[datetime]
    ip: Optional[str]
    action_type: Optional[str]
    aid: Optional[str]
    changed_fields: Optional['List[AuditChangedFieldDto]']


UserAudit.update_forward_refs()
