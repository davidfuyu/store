<template>
  <v-dialog v-model="showDialog" persistent max-width="640" @keydown.esc="showDialog = false">
    <v-card flat>
      <v-toolbar dense dark color="primary">
        <v-toolbar-title>Please Register ...</v-toolbar-title>
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
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword ? 'text' : 'password'"
                  class="text-xs"
                  @click:append="showPassword = !showPassword"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field label="name" v-model="name" class="text-xs" required></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-form>

      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="close">Cancel</v-btn>
        <v-btn text color="primary" @click="register">Register</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
/* eslint-disable */
import axios from "axios";
// import EventBus from './EventBus'
export default {
  name: "Register",
  data() {
    return {
      showDialog: true,
      showPassword: false,
      email: "",
      password: "",
      name: ""
    };
  },
  methods: {
    register() {
      axios
        .post("/user/register", {
          name: this.name,
          password: this.password,
          email: this.email
        })
        .then(res => {
          // router.push({ name: "Profile" });
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