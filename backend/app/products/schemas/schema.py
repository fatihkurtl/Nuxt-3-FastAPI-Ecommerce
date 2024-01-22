from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class OrderCartBase(BaseModel):
    product_id: int
    quantity: int
    
class OrderCartCreate(OrderCartBase):
    pass

class OrderCart(OrderCartBase):
    order_id: int
    create_date: datetime

class OrderCartUpdate(BaseModel):
    order_id: int
    status: str


class ProductBase(BaseModel):
    name: str
        
class ProductCreate(ProductBase):
    price: float

class Product(ProductBase):
    id: int
    price: float
    image_url: str
    create_date: datetime
    

class BillingDetailsCreate(BaseModel):
    country: str
    firstname: str
    lastname: str
    company_name: Optional[str] = None
    street_address: str
    apartment_or_suite: Optional[str] = None
    state_or_country: str
    posta_or_zip: str
    email: str
    phone: str
    order_notes: str
    total_price: float
    