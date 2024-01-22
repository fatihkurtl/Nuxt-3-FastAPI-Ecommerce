export async function addCart(id: number): Promise<any> {
    try {
        const response = await fetch(`${baseURL().url}/api/add/cart/${id}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          }
        })
    
        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`)
        }
    
        const res: any = await response.json()
        console.log(res)
        return res
      } catch (error) {
        console.error('Error fetching products:', error)
        throw error
      }

}