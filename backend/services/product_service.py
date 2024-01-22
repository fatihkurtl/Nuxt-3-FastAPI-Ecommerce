from sqlalchemy.orm import Session
from fastapi import status, HTTPException

from app.products.models import models
from app.products.schemas import schema


def get_product_by_name(db: Session, name: str):
    return db.query(models.Product).filter(models.Product.name == name).first()


def create_product(db: Session, product_name:str, product_price: float, image: str):
    db_product = models.Product(name=product_name, price=product_price, image_url=image)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def add_order_cart(db: Session, id: int):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    db_order = models.OrderCart(product_id=db_product.id, quantity=1)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return {'message': 'Product added to cart', 'status': status.HTTP_201_CREATED}


def get_order_cart(db: Session, skip: int = 0, limit: int = 50):
    db_order = db.query(models.OrderCart).offset(skip).limit(limit).all()
    order_list = []
    
    total_price = 0
    for i in db_order:
        db_products = db.query(models.Product).filter(models.Product.id == i.product_id).first()
        order_product_object = {
            'id': db_products.id,
            'name': db_products.name,
            'image_url': 'http://127.0.0.1:8000/api/product/images/' + db_products.image_url,
            'price': db_products.price,
            'order_id': i.order_id,
            'product_id': i.product_id,
            'sum_products_price': db_products.price * i.quantity,
            'quantity': i.quantity,           
        }
        order_list.append(order_product_object)
        total_price += db_products.price * i.quantity
    
    return {'order_list': order_list, 'total_price': total_price}


def update_order_items(db: Session, order: schema.OrderCartUpdate):
    print(order)
    db_order_item = db.query(models.OrderCart).filter(models.OrderCart.order_id == order.order_id).first()

    if order.status == 'increase':
        db_order_item.quantity += 1
        db.commit()
        return {'messages': 'Product added', 'status': status.HTTP_200_OK}
    
    elif order.status == 'decrease':
        if db_order_item.quantity == 1:
            db.delete(db_order_item)
            db.commit()
            return {'messages': 'Product quantity reduced', 'status': status.HTTP_200_OK}
        
        else:
            db_order_item.quantity -= 1
            db.commit()
            return {'messages': 'Product quantity reduced', 'status': status.HTTP_200_OK}
        
    return {'messages': 'Failed to update cart', 'status': status.HTTP_204_NO_CONTENT}

    
def delete_order_item(db: Session, order_id: int):
    db_order_item = db.query(models.OrderCart).filter(models.OrderCart.order_id == order_id).first()
    if db_order_item:
        db.delete(db_order_item)
        db.commit()
        return {'messages': 'Product removed', 'status': status.HTTP_200_OK}
    return {'messages': 'Error deleting product', 'status': status.HTTP_204_NO_CONTENT}



def save_payment_info(db: Session, billing_details: schema.BillingDetailsCreate):
    print(billing_details)
    save_payment_detail = models.Billing(**billing_details.dict())
    db.add(save_payment_detail)
    db.commit()
    db.refresh(save_payment_detail)
    db.query(models.OrderCart).delete()
    db.commit()
    return {'messages': 'Payment successful', 'status': status.HTTP_202_ACCEPTED}
    


# def get_order_detail(db: Session, skip: int = 0, limit: int = 100):
#     db_order_detail = db.query(models.OrderCart).offset(skip).limit(limit).all()
#     order_detail_list = []
    
#     for order in db_order_detail:
#         products = db.query(models.Product).filter(models.Product.id == order.product_id).first()
#         order_detail_object = {
#             'name': products.name,
#             'quantity': order.quantity,
#             'total_product_price': products.price * order.quantity,            
#         }
#         order_detail_list.append(order_detail_object)
#     return order_detail_list



    