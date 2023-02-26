<template>
  <v-card
    class="d-flex flex-column text-left"
    min-width="100"
    max-width="360"
    density="compact"
  >
    <v-lazy
      :options="{threshold: .1}"
      transition="fade-transition"
    >
      <!-- src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" -->
      <v-img
        :src="thumbnail.src"
        :lazy-src="thumbnail.lazySrc"
        :aspect-ratio="16/9"
        cover
        class="align-end"
      >
        <v-container class="px-2 py-1 text-body-1 font-weight-bold text-white">
          <span class="title-lines"> {{ item.title }} </span>
        </v-container>
      </v-img>
    </v-lazy>

    <v-card-item class="px-3 pt-2 pb-0">
      <v-chip
        size="small"
        color="primary"
        variant="elevated"
        v-for="category of item.categories"
        :key="category"
        class="mr-1"
      >
        {{ category }}
      </v-chip>
    </v-card-item>

    <v-card-item class="px-3 pt-1 pb-0">
      <v-chip
        size="x-small"
        color="secondary"
        variant="elevated"
        v-for="tag of item.tags"
        :key="tag"
        class="mr-1"
      >
        {{ tag }}
      </v-chip>
    </v-card-item>

    <v-card-text class="px-3 pt-2 pb-0">
      <span class="item-lines"> {{ item.description }} </span>
    </v-card-text>

    <v-spacer></v-spacer>

    <v-card-item class="px-3 pt-2 justify-end">
      <v-btn
        color="primary"
        class="pa-0 mx-1"
        height="30px"
        :href="item.url"
        target="_blank"
      >
        Open
      </v-btn>
    </v-card-item>
  </v-card>

</template>

<script setup>
import { makeThumbnailSrc } from "@/api";
import { onMounted } from '@vue/runtime-core';
import { reactive } from "vue";

const props = defineProps({
  item: Object,
});

const thumbnail = reactive({
  src: null,
  lazySrc: "noimage.jpg"
});

onMounted(() => {
  thumbnail.src = makeThumbnailSrc(props.item);
  if (typeof props.item.categories === "string") {
    props.item.categories = props.item.categories.split(",");
  }
  if (typeof props.item.tags === "string") {
    props.item.tags = props.item.tags.split(",");
  }
})
</script>

<style scoped>
.title-lines {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.25rem;
  text-shadow: 0px 0px 3px black, 0px 0px 5px black;
}

.item-lines {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
