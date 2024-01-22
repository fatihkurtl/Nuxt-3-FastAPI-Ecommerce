import type { BillingDetails } from "~/interfaces/billing"
import { useOrderStore } from '~/stores/order'

export async function postPaymentDetails(billingDetails: BillingDetails): Promise<any> {
  const order_store = useOrderStore()
    try {
        const response = await fetch(`${baseURL().url}/api/payment`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(billingDetails)
        })
    
        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`)
        }
    
        const res: any = await response.json()
        console.log('res', res)
        if (res.status === 202) {
          order_store.setTotal(0)
          order_store.setsubTotal(0)
        }
        return res
      } catch (error) {
        console.error('Error fetching products:', error)
        throw error
      }

}