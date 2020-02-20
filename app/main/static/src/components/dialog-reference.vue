<template>
  <v-dialog v-model="show" persistent max-width="960">
    <v-card flat>
      <v-toolbar dense dark color="primary">
        <v-toolbar-title>Please provide reference:</v-toolbar-title>
      </v-toolbar>

      <v-card-text class="pb-0">
        <v-container grid-list-md fluid>
          <v-row>
            <v-col cols="2">
              <v-subheader>Reference</v-subheader>
            </v-col>
            <v-col cols="9">
              <v-combobox
                v-model="reference"
                :items="items"
                :loading="isLoading"
                :search-input.sync="search"
                item-text="value"
                item-value="reference_id"
                placeholder="Start typing to search or input new reference"
                required
                class="mt-0 pt-0"
              ></v-combobox>
            </v-col>
            <v-col cols="1">
              <v-btn v-if="showCheck" text color="primary" @click="showReference = true">
                <v-icon>fas fa-check</v-icon>
              </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <div v-if="showReference">
              The following reference will be submitted:
              <br />
              {{referenceDisplay}}
            </div>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="onCloseReferenceButton">close</v-btn>
        <v-btn text color="primary" @click="onSubmitReferenceButton(reference)">submit</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
/* eslint-disable */
import axios from "axios";

export default {
  data() {
    return {
      isLoading: false,
      showCheck: false,
      showReference: false,
      reference: null,
      search: null,
      items: []
    };
  },
  computed: {
    show() {
      return this.showReferenceDialog;
    },
    referenceDisplay() {
      if (this.reference == null) return null;
      if (typeof this.reference === "string") {
        return this.reference;
      }
      if (typeof this.reference === "object") {
        return this.reference.value;
      }
      return null;
    }
  },
  props: [
    "showReferenceDialog",
    "onCloseReferenceButton",
    "onSubmitReferenceButton"
  ],
  watch: {
    search(val) {
      if (this.isLoading) return;
      this.showCheck = true;
      this.isLoading = true;
      this.searchReference(val);
    },
    show() {
      if (this.show) {
        this.reference = null;
        this.showCheck = false;
      }
    }
  },
  methods: {
    searchReference(val) {
      this.items = [];
      axios
        .get("reference/search", { params: { search: val } })
        .then(res => {
          this.items = res.data.records;
        })
        .catch(err => console.log(err))
        .finally(() => (this.isLoading = false));
    }
  }
};
</script>