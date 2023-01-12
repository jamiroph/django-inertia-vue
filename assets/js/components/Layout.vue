<script setup>
import { Link } from "@inertiajs/inertia-vue3";
import MainNav from "./MainNav";
</script>

<template>
	<MainNav />
	<main class="container max-w-5xl 4xl:px-4 mx-auto pt-20">
		<slot />
	</main>
</template>

<style scoped></style>
