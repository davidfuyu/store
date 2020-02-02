<template>
  <v-app>
    <navigation :drawer.sync="drawer"></navigation>

    <v-app-bar dense dark app clipped-left fixed>
      <v-app-bar-nav-icon @click.stop="drawer= !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="width: 400px" class="ml-0 pl-3">
        <span class="title">Information</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <user-profile></user-profile>
    </v-app-bar>
    <v-content>
      <router-view :key="$route.fullPath"></router-view>
    </v-content>
    <dialog-loading :indeterminate="false" msg="Loading..."></dialog-loading>
  </v-app>
</template>

<script>
import Navigation from "@/components/navigation.vue";
import UserProfile from "@/components/user-profile.vue";

export default {
  name: "App",

  components: { Navigation, "user-profile": UserProfile },

  data() {
    return {
      drawer: true,
      dialog: false
    };
  },
  beforeCreate() {
    this.$store.dispatch("organism/fetch");
    this.$store.dispatch("property/fetch");
    this.$store.dispatch("category/fetch");
  }
};
</script>
