<template>
  <v-container fluid>
    <v-dialog v-model="showDialog" persistent max-width="640">
      <v-card flat>
        <v-toolbar dense dark color="primary">
          <v-toolbar-title>New Organism</v-toolbar-title>
        </v-toolbar>

        <v-form>
          <v-card-text>
            <v-container grid-list-md fluid>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="new organism name"
                    v-model="title"
                    class="text-xs"
                    :rules="[rules.required]"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-form>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="closeDialog">close</v-btn>
          <v-btn text color="primary" @click="saveDialog">save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      showDialog: true,
      title: "",
      rules: { required: v => !!v || "Required." }
    };
  },
  methods: {
    closeDialog: function() {
      this.showDialog = false;
      this.title = "";
      this.$router.go(-1);
    },
    saveDialog: function() {
      axios.put("/organism", { title: this.title }).then(response => {
        if (response.data.success) {
          let id = response.data.records[0]["organism_id"];
          this.$router.push(`/organism/${id}`);
        }
      });
    }
  }
};
</script>