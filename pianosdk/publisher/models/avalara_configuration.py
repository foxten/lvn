from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.address_config import AddressConfig
from pianosdk.publisher.models.avalara_origin_address import AvalaraOriginAddress
from typing import List


class AvalaraConfiguration(BaseModel):
    avalara_account_id: Optional[str]
    avalara_license_key: Optional[str]
    avalara_company_code: Optional[str]
    avalara_sales_invoice_enabled: Optional[bool]
    avalara_return_invoice_enabled: Optional[bool]
    avalara_collect_address_enabled: Optional[bool]
    avalara_address_config_us: Optional['List[AddressConfig]']
    avalara_address_config_ca: Optional['List[AddressConfig]']
    avalara_origin_address: Optional['AvalaraOriginAddress']


AvalaraConfiguration.update_forward_refs()
