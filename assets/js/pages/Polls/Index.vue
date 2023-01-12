<script setup>
import { Link } from '@inertiajs/inertia-vue3';

const props = defineProps({
    polls: Object
});
</script>


<template> 
    <div class="container mx-auto">
        <h2 class="text-3xl capitalize text-teal-600 m-4">Polls</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 auto-rows-max">
            <div v-for="(poll, index) in polls" :key="index" class="p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                <Link :href="$route('home')">
                    <h5 v-if="poll.title"
                        class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
                    >{{ poll.title }}
                    </h5>
                    <p class="font-normal text-gray-700 dark:text-gray-400">
                        {{ poll.question_text }}
                    </p>
                </Link>
            </div>
        </div>
    </div>
</template>
