import type { OrderItem, OrderList } from "~/interfaces/orderCart"
import { useOrderStore } from "~/stores/order"
import { baseURL } from "~/utils/useApi"

export async function getOrderCart(): Promise<OrderList> {
    const orderStore = useOrderStore()
  try {
    const response = await fetch(`${baseURL().url}/api/orderCart`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`)
    }

    const orders: OrderList = await response.json() as OrderList
    console.log(orders)
    orderStore.setTotal(orders.total_price)
    orderStore.setsubTotal(orders.total_price)
    return orders
  } catch (error) {
    console.error('Error fetching products:', error)
    throw error
  }
}
