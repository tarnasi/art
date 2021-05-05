<template>
  <v-app>
    <!-- Header -->
    <front-header :showSlider="true" />

    <!-- Main Content -->
    <v-container>
      <v-main>
        <transition name="scale-transition">
          <router-view />
        </transition>
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import FrontHeader from './Partial/Header.vue'

export default {
  name: "FrontLayout",

  components: {
    FrontHeader,
  }
};
</script>
