<template>
  <div class="base-layout-loader">
    <dashboard-layout v-if="layoutAuth" />
    <front-layout v-if="!layoutAuth" />
  </div>
</template>

<script>
import DashboardLayout from '../components/Layouts/Dashboard/DashboardLayout.vue'
import FrontLayout from '../components/Layouts/Front/FrontLayout.vue'

export default {
  name: "Layout",

  components: {
    DashboardLayout,
    FrontLayout
  },

  data() {
    return {
      layoutAuth: false
    }
  }
}
</script>