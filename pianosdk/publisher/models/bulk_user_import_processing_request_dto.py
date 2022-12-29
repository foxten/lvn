from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BulkUserImportProcessingRequestDto(BaseModel):
    bulk_user_import_id: Optional[str]
    bulk_user_import_created: Optional[datetime]
    bulk_user_import_total_user_count: Optional[int]
    bulk_user_import_processed_user_count: Optional[int]


BulkUserImportProcessingRequestDto.update_forward_refs()
