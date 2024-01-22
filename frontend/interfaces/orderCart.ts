export interface OrderItem {
    id: number
    name: string
    image_url: string
    price: number
    order_id: number
    product_id: number
    sum_products_price: number
    quantity: number
}
export interface OrderList {
    order_list: OrderItem[]
    total_price: number
}
