from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.publisher.models.erase_contract_user import EraseContractUser
from pianosdk.publisher.models.erase_conversion import EraseConversion
from pianosdk.publisher.models.erase_subscription import EraseSubscription
from pianosdk.publisher.models.erase_transaction import EraseTransaction
from pianosdk.publisher.models.erase_user import EraseUser
from pianosdk.publisher.models.erase_user_payment import EraseUserPayment
from pianosdk.publisher.models.erase_user_payment_info import EraseUserPaymentInfo
from typing import List


class EraseUserResponse(BaseModel):
    user: Optional['EraseUser']
    subscriptions: Optional['List[EraseSubscription]']
    upis: Optional['List[EraseUserPaymentInfo]']
    payments: Optional['List[EraseUserPayment]']
    transactions: Optional['List[EraseTransaction]']
    conversions: Optional['List[EraseConversion]']
    contract_users: Optional['List[EraseContractUser]']


EraseUserResponse.update_forward_refs()
