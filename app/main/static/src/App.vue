<template>
  <v-app>
    <navigation :drawer.sync="drawer"></navigation>

    <v-app-bar color="primary" dense dark app clipped-left fixed>
      <v-app-bar-nav-icon @click.stop="drawer= !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="width: 400px" class="ml-0 pl-3">
        <span class="title">Information</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <span v-if="organisms.length > 0" class="mt-7">
        <v-autocomplete
          :items="organisms"
          item-text="organism_name"
          item-value="organism_id"
          :filter="filterName"
          v-model="organismId"
          append-icon="fas fa-search"
          solo-inverted
          flat
        ></v-autocomplete>
      </span>
      <user-profile></user-profile>
    </v-app-bar>
    <v-content>
      <router-view :key="$route.fullPath"></router-view>
    </v-content>
    <dialog-loading :indeterminate="false" msg="Loading..."></dialog-loading>
  </v-app>
</template>

<script>
/* eslint-disable */
import Navigation from "@/components/navigation.vue";
import UserProfile from "@/components/user-profile.vue";
import { mapGetters } from "vuex";

export default {
  name: "App",

  components: { Navigation, "user-profile": UserProfile },

  data() {
    return {
      drawer: true,
      dialog: false,
      organismId: null
    };
  },
  computed: {
    ...mapGetters("organism", { organisms: "organism" })
  },
  beforeCreate() {
    this.$store.dispatch("organism/fetch");
    this.$store.dispatch("property/fetch");
    this.$store.dispatch("category/fetch");
  },
  watch: {
    organismId: function() {
      this.$router.push(`/organism/${this.organismId}`);
    }
  },
  methods: {
    filterName(item, queryText, itemText) {
      const textOne = item.organism_name.toLowerCase();
      const searchText = queryText.toLowerCase();

      return ( textOne.indexOf(searchText) > -1);
    }
  }
};
</script>
