<script setup>
import { Link } from '@inertiajs/inertia-vue3';
</script>

<template>
    <nav>
        <ul>
            <li><Link :href="$route('home')">Home</Link></li>
            <li><Link :href="$route('contact')">Contact</Link></li>
        </ul>
    </nav>
    <main>
        <slot />
    </main>
</template>


<style scoped>

</style>
