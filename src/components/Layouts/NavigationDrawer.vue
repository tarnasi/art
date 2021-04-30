<template>
  <v-navigation-drawer class="light-blue darken-4" dark app>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="title">Codesider</v-list-item-title>
        <v-list-item-subtitle>Site Manager</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>
    <v-list>
      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <template v-slot:append>
      <div class="pa-2">
        <v-btn block> Logout </v-btn>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "NavigationDrawer",

  data() {
    return {
      items: [
        { title: "Dashboard", icon: "mdi-view-dashboard" },
        { title: "Account", icon: "mdi-account-box" },
        { title: "Admin", icon: "mdi-gavel" },
      ],
    };
  },
};
</script>
