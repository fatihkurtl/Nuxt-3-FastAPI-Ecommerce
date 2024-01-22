import { defineStore } from 'pinia'

export const useOrderStore = defineStore('order', () => {
    const total = ref<number>(0)
    const subTotal = ref<number>(0)

    function setTotal(e: number) {
        total.value = e
    }

    function setsubTotal(e: number) {
        subTotal.value = e
    }

    function getTotal(): { total: number, subTotal: number }  {
        return { 'total': total.value, 'subTotal': subTotal.value }
    }

    return { total, subTotal, setTotal, setsubTotal, getTotal }
},
    {
        persist: {
            storage: persistedState.localStorage
        }
    }
)