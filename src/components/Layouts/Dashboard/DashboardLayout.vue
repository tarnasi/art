<template>
  <v-app>
    <!-- HEADER -->
    <Header />

    <!-- NavigationDrawer -->
    <navigation-drawer />

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
import NavigationDrawer from './Partial/NavigationDrawer.vue';
import Header from './Partial/Header.vue'

export default {
  name: "DashboardLayout",

  components: {
    Header,
    NavigationDrawer,
  },
};
</script>
