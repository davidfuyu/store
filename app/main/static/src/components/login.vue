<template>
  <v-dialog v-model="showDialog" persistent max-width="640" @keydown.esc="showDialog = false">
    <v-card flat>
      <v-toolbar dense dark color="primary">
        <v-toolbar-title>Please Login ...</v-toolbar-title>
      </v-toolbar>

      <v-card-text>
        <v-container grid-list-md fluid>
          <v-row>
            <v-col cols="12">
              <v-text-field label="email" v-model="email" class="text-xs" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field label="password" v-model="password" type="password" class="text-xs" required ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-divider></v-divider>
      <v-card-actions>
        <v-btn text color="primary" @click="register">Register</v-btn>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="close">Cancel</v-btn>
        <v-btn text color="primary" @click="login">Login</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
import { mapMutations } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      showDialog: true,
      email: "",
      password: ""
    };
  },
  computed: {},
  methods: {
    ...mapMutations("user", ["userLogin"]),
    login() {
      this.$http
        .post("/user/login", {
          email: this.email,
          password: this.password
        })
        .then(res => {
          if (res.data.success) {
            this.userLogin(res.data.records);
            this.showDialog = false;
            this.$router.push(this.$route.query.redirect || "/");
          }
        });
    },
    register() {
      this.$router.push("/register");
      this.showDialog = false;
    },
    close() {
      this.showDialog = false;
    }
  }
};
</script>