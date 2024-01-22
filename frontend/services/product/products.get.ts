import type { Product } from "~/interfaces/product"
import { baseURL } from "~/utils/useApi"

export async function getProducts(): Promise<Product[]> {
  try {
    const response = await fetch(`${baseURL().url}/api/products`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`)
    }

    const products: Product[] = await response.json() as Product[]
    return products
  } catch (error) {
    console.error('Error fetching products:', error)
    throw error
  }
}