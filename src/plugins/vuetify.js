import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  rtl: true,
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      dark: {
        primary: "purple darken-4",
        secondary: "pink darken-4",
        success: "green lighten-3",
        info: "cyan lighten-4",
        white: "grey lighten-4",
      },
    },
  },
});
