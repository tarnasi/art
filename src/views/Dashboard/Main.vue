<template>
  <div v-if="posts != null">
    <Dashboard :postsLength="postsLength" :posts="posts" />
  </div>
</template>

<script>
  import Dashboard from '../../components/Dashboard'

  import apis from '../../apis/urls'

  export default {
    name: 'DashboardMainPage',

    components: {
      Dashboard,
    },

    data: () => {
      return {
        postsLength: 0,
        posts: null,
      }
    },

    mounted () {
      apis.fetchAllPosts(res => {
        this.posts = res.data
        this.postsLength = res.data.length
      })
    },
  }
</script>
