<template>
  <v-app>
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
export default {
  name: "FrontLayout",
};
</script>
