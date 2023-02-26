<template>
  <v-main class="bg-grey-lighten-4">
    <router-view />
    <v-footer class="justify-center bg-grey-lighten-2 text-grey-darken-1">
      ttoda @ {{ new Date().getFullYear() }}
    </v-footer>
  </v-main>
</template>

<script setup>
  //
</script>
