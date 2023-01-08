<script setup>
const props = defineProps({
    polls: Object,
    choices: Object
});
</script>


<template>
    <h2>This is the events page</h2>
    <div class="container lg-8 m-auto">
        <article v-for="(poll, index) in polls" :key="index">
            <img v-if="poll.img"/>
            <h3 v-if="poll.header">{{ poll.header }}</h3>
            <p> {{ poll.question_text }}</p>
        </article>
    </div>
</template>
