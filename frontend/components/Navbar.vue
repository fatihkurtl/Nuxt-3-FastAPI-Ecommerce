<script setup lang="ts">

</script>

<template>
    <nav class="custom-navbar navbar navbar navbar-expand-md navbar-dark bg-dark" arial-label="Furni navigation bar">

        <div class="container">
            <NuxtLink class="navbar-brand" to="/">Furni<span>.</span></NuxtLink>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsFurni"
                aria-controls="navbarsFurni" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarsFurni">
                <ul class="custom-navbar-nav navbar-nav ms-auto mb-2 mb-md-0">
                    <li class="nav-item active">
                        <NuxtLink class="nav-link" to="/">Home</NuxtLink>
                    </li>
                    <li><NuxtLink class="nav-link" to="/shop">Shop</NuxtLink></li>
                    <li><NuxtLink class="nav-link" to="/about">About us</NuxtLink></li>
                    <li><NuxtLink class="nav-link" to="/services">Services</NuxtLink></li>
                    <li><NuxtLink class="nav-link" href="/blog">Blog</NuxtLink></li>
                    <li><NuxtLink class="nav-link" href="/contact">Contact us</NuxtLink></li>
                </ul>

                <ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
                    <li><a class="nav-link" href="#"><img src="images/user.svg"></a></li>
                    <li><NuxtLink class="nav-link" href="/cart"><img src="images/cart.svg"></NuxtLink></li>
                </ul>
            </div>
        </div>

    </nav>
</template>

<style scoped></style>