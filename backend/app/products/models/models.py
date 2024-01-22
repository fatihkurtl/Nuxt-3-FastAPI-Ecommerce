from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from db.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    image_url = Column(String)
    price = Column(Float)
    create_date = Column(DateTime, default=datetime.now)
    

class OrderCart(Base):
    __tablename__ = 'order_cart'
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    create_date = Column(DateTime, default=datetime.now)
    
    
class Billing(Base):
    __tablename__ = 'billing_details'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    country = Column(String)
    company_name = Column(String, nullable=True)
    street_address = Column(String)
    apartment_or_suite = Column(String, nullable=True)
    state_or_country = Column(String)
    posta_or_zip = Column(String)
    email = Column(String)
    phone = Column(String)
    order_notes = Column(String)
    order_id = Column(Integer, ForeignKey('order_cart.order_id'))
    total_price = Column(Float)
    create_date = Column(DateTime, default=datetime.now)
    