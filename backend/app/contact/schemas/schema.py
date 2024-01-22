from typing import Union
from pydantic import BaseModel
from datetime import datetime


class ContactBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    message: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    send_date: datetime