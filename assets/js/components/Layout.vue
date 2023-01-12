<script setup>
import { Link } from '@inertiajs/inertia-vue3';
</script>

<template>
    <nav class="flex text-teal-500 gap-4 justify-items-end">
        <ul>
            <li class="text-3xl font-bold underline"><Link :href="$route('home')">Home</Link></li>
            <li class="text-3xl font-bold underline"><Link :href="$route('contact')">Contact</Link></li>
        </ul>
    </nav>
    <main>
        <slot />
    </main>
</template>


<style scoped>

</style>
