export default defineEventHandler((event) => {
    console.log('from nuxt server component =>', event)
    return {
        api: 'works'
    }
})