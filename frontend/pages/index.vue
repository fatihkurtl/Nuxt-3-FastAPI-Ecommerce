<script setup lang="ts">
import { useCounterStore } from '@/stores/counter';

// layouts 
// definePageMeta({
//     layout: 'default'
// })

// pinia store
const store = useCounterStore()

// composables/test.ts
const test = useTest()

// .env with nuxt.config.ts
const config = useRuntimeConfig()
console.log('.env API', config.public.apiUrl)

// datafetching & ts interface
interface Users {
  id: number
  name: string
  username: string
  email: string
  address: {
    street: string;
    suite: string;
    city: string;
    zipcode: string;
    geo: {
      lat: string;
      lng: string;
    }
  }
  /* or
   address: object
   */
}
const { error, pending, data: users } = await useFetch<Users[]>('https://jsonplaceholder.typicode.com/users', {
  lazy: true,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})

</script>

<template>
  <HomeSectionsHero />
  <HomeSectionsProduct />
  <WhyChooseUs />
  <HomeSectionsHelp />
  <PopularProduct />
  <!-- <Testimonials /> -->
    <HomeBlog />
</template>


<style scoped></style>