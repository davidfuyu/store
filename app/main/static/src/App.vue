<template>
  <v-app>
    <v-app-bar dense dark app clipped-left fixed>
      <v-app-bar-nav-icon @click.stop="drawer= !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="width: 400px" class="ml-0 pl-3">
        <span class="title">Information</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <user-profile></user-profile> -->
      <!-- <v-toolbar-title style="font-weight:300;font-size:21px;" class="ml-0 pl-0">{{ name }}</v-toolbar-title> -->
    </v-app-bar>
    <v-content>
      <router-view :key="$route.fullPath"></router-view>
    </v-content>
    <dialog-loading :indeterminate="false" msg="Loading..."></dialog-loading>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data() {
    return {
      drawer: true,
      dialog: false
    };
  },
  beforeCreate() {
    this.$store.dispatch("organism/fetch");
    this.$store.dispatch("property/fetch");
  }
};
</script>
