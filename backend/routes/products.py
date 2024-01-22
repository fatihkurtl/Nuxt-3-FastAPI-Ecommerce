import shutil
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.products.schemas import schema
from db.database import get_db
from services.product_service import add_order_cart, create_product, delete_order_item, get_order_cart, get_product_by_name, get_products, save_payment_info, update_order_items

import os

router = APIRouter(
    prefix='/api',
    tags=['products']
)

PRODUCT_IMAGE_PATH = 'media/products/'

@router.post('/product', response_model=schema.Product)
async def create(name: str, price: float, file: UploadFile = File(...), db: Session = Depends(get_db)):
    db_product = get_product_by_name(db, name=name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product name already registered")
    
    with open(PRODUCT_IMAGE_PATH+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
        
    image = str(file.filename)
    
    return create_product(db=db, product_name=name, product_price=price, image=image)


@router.get('/product/images/{images}')
async def get_images(images:str):
    image_path = os.path.join(PRODUCT_IMAGE_PATH, images)
    return FileResponse(image_path)


@router.get('/products', response_model=list[schema.Product])
async def product_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    products_list = []
    for product in products:
        print(product.image_url)
        product_dict = {
            'id': product.id,
            'name': product.name,
            'image_url': 'http://127.0.0.1:8000/api/product/images/' + product.image_url,
            'price': product.price,
            'create_date': product.create_date,
        }
        products_list.append(product_dict)
    return products_list


@router.post('/add/cart/{id}')
async def add_cart(id: int, db: Session = Depends(get_db)):
    print(id)
    return add_order_cart(db=db, id=id)


@router.get('/orderCart')
async def order_cart(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    order_cart = get_order_cart(db, skip=skip, limit=limit)
    return order_cart


@router.put('/update/orderItem/{order_id}')
async def update_order(order: schema.OrderCartUpdate, db: Session = Depends(get_db)):
    print(order.order_id)
    print(order.status)    
    return update_order_items(db, order)


@router.delete('/delete/orderItem/{order_id}')
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    return delete_order_item(db, order_id)


@router.post('/payment')
async def payment(billingDetails: schema.BillingDetailsCreate, db: Session = Depends(get_db)):    
    return save_payment_info(db, billingDetails)


# @router.get('/order/detail')
# async def order_detail(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return get_order_detail(db=db, skip=skip, limit=limit)
