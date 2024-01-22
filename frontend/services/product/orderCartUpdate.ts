export async function orderCartSettings(order_id: number, status: string, method: string = 'PUT'): Promise<any> {
    console.log(order_id, 'order_id')
    console.log(status, 'status')
    console.log(method, 'method')
    event?.preventDefault()
    try {
        const response = await fetch(method === 'PUT' ? `${baseURL().url}/api/update/orderItem/${order_id}` : `${baseURL().url}/api/delete/orderItem/${order_id}`, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                order_id: order_id,
                status: status
            })
        })

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`)
        }
        window.location.reload()
        const res: any = await response.json()
        console.log(res)
    } catch (error) {
        console.error('Error increase products quantity:', error)
        throw error
    }
}