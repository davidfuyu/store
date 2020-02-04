<template>
  <v-menu
    :close-on-content-click="false"
    :nudge-left="150"
    :nudge-bottom="20"
    v-model="showUser"
    offset-y
  >
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" icon style="margin-right:0;">
        <v-avatar size="36px" tile>
          <v-icon>fas fa-user-circle</v-icon>
        </v-avatar>
      </v-btn>
    </template>
    <v-card width="480">
      <v-card-title>
        <span class="headline">{{ name }}</span>
      </v-card-title>
      <v-card-text>
        <v-container fill-height fluid grid-list-md>
          <v-layout row wrap>
            <v-flex xs12>{{ email }}</v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn @click.native="showUser = false">close</v-btn>
        <v-spacer></v-spacer>
        <v-btn v-if="!isAuthenticated" color="primary" dark @click="login">Login</v-btn>
        <v-btn v-else color="primary" dark @click="logout">Logout</v-btn>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>
<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  name: "UserProfile",
  data() {
    return {
      showUser: false
    };
  },
  props: {},
  computed: {
    ...mapGetters("user", ["email", "name", "isAuthenticated"])
  },
  methods: {
    ...mapMutations("user", ["userLogout"]),
    login() {
      this.showUser = false;
      this.$router.push("/login");
    },
    logout() {
      this.userLogout();
      this.showUser = false;
      this.$router.push("/");
    }
  }
};
</script>
