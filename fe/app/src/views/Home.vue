<template>
  <Gallery :items="items" />
</template>

<script setup>
import { api } from "@/api";
import Gallery from '@/components/Gallery.vue';
import { ref } from "vue";

const items = ref([]);
api.get("/items").then((response) => {
  items.value = response.data;
});
</script>
