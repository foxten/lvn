from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BulkUserImport(BaseModel):
    bulk_user_import_id: Optional[str]
    bulk_user_import_created: Optional[datetime]
    bulk_user_import_completed: Optional[datetime]


BulkUserImport.update_forward_refs()
