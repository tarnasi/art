<template>
  <div v-if="posts != null">
    <main-page :postsLength="postsLength" :posts="posts" />
  </div>
</template>

<script>
  import MainPage from '../components/MainPage'

  import apis from '../apis/urls'

  export default {
    name: 'Home',

    components: {
      MainPage,
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
