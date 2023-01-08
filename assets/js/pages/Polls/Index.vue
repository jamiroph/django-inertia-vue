<script setup>
const props = defineProps({
    polls: Object
});
</script>


<template>
    <h2 class="m-auto">This is the polls page</h2>
    <div class="container lg-8 m-auto">
        <article v-for="(poll, index) in polls" :key="index">
            <img v-if="poll.img"/>
            <h3 v-if="poll.title">{{ poll.title }}</h3>
            <p> {{ poll.question_text }}</p>
        </article>
    </div>
</template>
