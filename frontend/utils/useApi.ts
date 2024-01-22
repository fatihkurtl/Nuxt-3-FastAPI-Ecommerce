const baseURL = () => {
    const config = useRuntimeConfig()
    return {
        url: config.public.apiUrl
    }
}

export {
    baseURL
}