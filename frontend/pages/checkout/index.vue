<script setup lang="ts">

definePageMeta({
    middleware: 'auth-checkout'
})

</script>

<template>

    <CheckoutHero />
    <CheckoutForm />

</template>

<style scoped>

</style>