<template>
  <v-row class="text-left">
    <v-col>
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Posts</div>
            <v-list-item-title class="headline mb-1">
              Number {{ postsLength }}
            </v-list-item-title>
          </v-list-item-content>

          <v-list-item-avatar tile size="80" color="green accent-3">
            <v-icon>{{ icons.mdiPost }}</v-icon>
          </v-list-item-avatar>
        </v-list-item>
      </v-card>
    </v-col>
    <v-col>
      <v-card class="mx-auto" max-width="344" outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Users</div>
            <v-list-item-title class="headline mb-1">
              Number 5
            </v-list-item-title>
          </v-list-item-content>

          <v-list-item-avatar tile size="80" color="yellow darken-4">
            <v-icon>{{ icons.mdiAccountBox }}</v-icon>
          </v-list-item-avatar>
        </v-list-item>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import {
    mdiPost,
    mdiAccountBox,
  } from '@mdi/js'


export default {
  name: "MainPage",

  props: ['postsLength', 'posts'],

  mounted() {
    console.log("posts: ", this.posts);
  },

  data: () => ({
    icons: {
      mdiPost,
      mdiAccountBox,
    },
  }),
};
</script>
