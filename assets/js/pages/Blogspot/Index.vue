<script setup>
import { Link } from '@inertiajs/inertia-vue3';

const props = defineProps({
    posts: Object
});
</script>


<template> 
    <div class="container mx-auto">
        <h2 class="text-3xl capitalize text-teal-600 m-4">Posts</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 auto-rows-max">
            <div v-for="(post, index) in posts" :key="index" class="p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                <Link :href="$route('home')">
                    <h5 v-if="post.title"
                        class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
                    >{{ post.title }}
                    </h5>
                    <p class="font-normal text-gray-700 dark:text-gray-400">
                        {{ post.summary }}
                    </p>
                    <p  class="font-thin text-2 ">
                        Created: {{ post.created }}
                    </p>
                    <p>
                        Updated: {{ post.last_modified }}
                    </p>
                </Link>
            </div>
        </div>
    </div>
</template>
