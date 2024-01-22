import { useOrderStore } from "~/stores/order"

export default defineNuxtRouteMiddleware((to, from) => {

    const orderStore = useOrderStore()

    if (orderStore.getTotal().total === 0 && orderStore.getTotal().subTotal === 0 && to.path !== from.path) {
        return navigateTo(from.path)
    } else if (from.name == 'checkout') {
        return navigateTo('/cart')
    }

})
