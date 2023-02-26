<template>
  <v-container class="d-flex align-center text-center fill-height">
    <v-row>
      <v-col
        :cols="cols"
        v-for="item in items"
        :key="item.uid"
        class="d-flex justify-center"
      >
        <item-card :item="item"></item-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { computed } from "vue";
import { useDisplay } from 'vuetify';
import ItemCard from "./ItemCard.vue";

const props = defineProps({
  items: Object,
});

const { name } = useDisplay();
const cols = computed(() => {
  switch (name.value) {
      case 'xs': return 12;
      case 'sm': return 6;
      case 'md': return 4;
      case 'lg': return 3;
      case 'xl': return 3;
      default: return 3;
    }
});
</script>
