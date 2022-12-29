from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class App(BaseModel):
    aid: Optional[str]
    default_lang: Optional[str]
    email_lang: Optional[str]
    details: Optional[str]
    email: Optional[str]
    name: Optional[str]
    user_provider: Optional[str]
    url: Optional[str]
    logo1: Optional[str]
    logo2: Optional[str]
    state: Optional[str]
    private_key: Optional[str]
    api_token: Optional[str]


App.update_forward_refs()
