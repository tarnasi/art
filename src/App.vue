<template>
  <v-app>
    <!-- drwaer -->
    <navigation-drawer />

    <!-- Header -->
    <Header />

    <!-- Main Content -->
    <v-container>
      <v-main>
        <transition name="scale-transition">
          <router-view/>
        </transition>
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import Header from './components/Layouts/Header.vue'
import NavigationDrawer from './components/Layouts/NavigationDrawer.vue'


export default {
  name: 'App',

  components: {
    Header,
    NavigationDrawer
  },
};
</script>
