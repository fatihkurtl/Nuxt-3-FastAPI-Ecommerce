<script setup lang="ts">
import { getProducts } from '~/services/product/products.get'
import type { Product } from "~/interfaces/product"
import { addCart } from '~/services/product/addCart.post';

const products = ref<Product[]>(await getProducts())


</script>

<template>

<div class="untree_co-section product-section before-footer-section">
		    <div class="container">
		      	<div class="row">

		      		<!-- Start Column 1 -->
					<div v-for="product in products" :key="product.id" class="col-12 col-md-4 col-lg-3 mb-5">
						<a class="product-item" href="#">
							<img :src="product.image_url" class="img-fluid product-thumbnail">
							<h3 class="product-title">{{ product.name}}</h3>
							<strong class="product-price">${{product.price}}</strong>

							<span class="icon-cross">
								<img @click="addCart(product.id)" src="images/cross.svg" class="img-fluid">
							</span>
						</a>
					</div> 
					<!-- End Column 1 -->

		      	</div>
		    </div>
		</div>

</template>


<style scoped>

</style>