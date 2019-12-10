<template>
  <v-dialog v-model="showDialog" persistent max-width="640" @keydown.esc="showDialog = false">
    <v-card flat>
      <v-toolbar dense dark color="primary">
        <v-toolbar-title>Please Login ...</v-toolbar-title>
      </v-toolbar>

      <v-form ref="form">
        <v-card-text>
          <v-container grid-list-md fluid>
            <v-row>
              <v-col cols="12">
                <v-text-field label="email" v-model="email" class="text-xs" required></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="password"
                  v-model="password"
                  type="password"
                  class="text-xs"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-form>

      <v-divider></v-divider>
      <v-card-actions>
        <v-btn text color="primary" @click="close">Register</v-btn>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="close">Cancel</v-btn>
        <v-btn text color="primary" @click="login">Login</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
import axios from "axios";
import router from "../router";
export default {
  name: "Login",
  data() {
    return {
      showDialog: true,
      username: "",
      password: ""
    };
  },
  methods: {
    login() {
      axios
        .post("/user/login", {
          email: this.email,
          password: this.password
        })
        .then(res => {
          localStorage.setItem("usertoken", res.data);
          this.email = "";
          this.password = "";
          router.push({ name: "Profile" });
        });
      this.emitMethod();
    },
    close() {
      this.showDialog = false;
    },
    emitMethod() {
      //   EventBus.$emit('logged-in', 'loggedin')
    }
  }
};
</script>