<script setup>
const props = defineProps({
    polls: Object
});
</script>


<template>
    <h2 class="m-auto">This is the polls page</h2>
    <div class="container lg-8 m-auto">
        <a v-for="(poll, index) in polls" :key="index"
			href="#"
			class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
		>
			<h5 v-if="poll.title"
				class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
			>{{ poll.title }}
			</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400">
				{{ poll.question_text }}
			</p>
		</a>
    </div>
</template>
