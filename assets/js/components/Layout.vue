<script setup>
import { Link } from "@inertiajs/inertia-vue3";
import MainNav from "./MainNav";
</script>

<template>
	<MainNav />
	<main class="mt-20">
		<slot />
	</main>
</template>

<style scoped></style>
