<template>
  <v-container fluid>
    <div :hidden="!show">
      <b style="font-size:2em">{{name}}</b>
      <v-divider></v-divider>
      <v-btn title="Edit" @click="onClickEditButton" :hidden="isEditing">Edit</v-btn>
      <v-btn title="Cancel" @click="onClickCancelButton" :hidden="!isEditing">Cancel</v-btn>
      <v-btn title="Save" @click="onClickSaveButton" :hidden="!showSaveButton">Save</v-btn>
      <div v-if="isEditing">
        <v-form>
          <div v-for="(c, i) in categories" :key="i">
            <b style="font-size:1.5em">{{c.property_category_name}}</b>
            <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
              <v-container>
                <v-row>
                  <v-col cols="5">
                    <b>{{p['property_name']}}</b>:
                  </v-col>
                  <v-col cols="5">
                    <v-text-field
                      v-model="formField[p['property_id']]['value']"
                      class="text-xs"
                      solo
                      hide-details
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </div>
        </v-form>
      </div>
      <div v-else :hidden="!show">
        <div v-for="(c, i) in categories" :key="i">
          <b style="font-size:1.5em">{{c.property_category_name}}</b>
          <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
            <div v-if="keyed[p['property_id']]">
              <b style="margin-left:40px">{{p['property_name']}}</b>
              {{keyed[p['property_id']]['value']}}
            </div>
          </div>
        </div>
      </div>
    </div>
  </v-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import { mapState } from "vuex";

export default {
  data() {
    return {
      isEditing: false,
      show: false,
      organismId: 0,
      name: "",
      keyed: {}
    };
  },
  computed: {
    ...mapState("category", ["categories"]),
    ...mapState("property", ["properties", "categorizedProperties"]),
    showSaveButton: function() {
      return this.isEditing;
    },
    formField: function() {
      let form = {};
      for (let i = 0; i < this.properties.length; i++) {
        let p = this.properties[i]["property_id"];
        if (this.keyed[p] != null) {
          form[p] = JSON.parse(JSON.stringify(this.keyed[p]));
        } else {
          form[p] = {};
          form[p]["organism_id"] = this.organismId;
          form[p]["property_id"] = p;
          form[p]["value"] = null;
        }
      }

      return form;
    }
  },
  created() {
    if (!this.$route.params.id) return;
    this.organismId = this.$route.params.id;
    axios.get(`organism-property/${this.organismId}`).then(response => {
      if (response.data.success) {
        let records = response.data.records;
        this.name = records[0]["name"];
        for (let i = 0; i < records.length; i++) {
          let p = records[i]["property_id"];
          this.keyed[p] = records[i];
        }
        this.show= true;
      }
    });
  },
  methods: {
    onClickEditButton: function() {
      this.isEditing = true;
    },
    onClickCancelButton: function() {
      this.isEditing = false;
    },
    onClickSaveButton: function() {
      let todo = {};
      for (let i = 0; i < this.properties.length; i++) {
        let p = this.properties[i]["property_id"];
        if (
          (this.keyed[p] == undefined && this.formField[p]["value"] != null) ||
          (this.keyed[p] != undefined &&
            this.formField[p]["value"] != this.keyed[p]["value"])
        ) {
          todo[p] = JSON.parse(JSON.stringify(this.formField[p]));
        }
      }

      axios
        .post(`/organism-property/${this.organismId}`, todo)
        .then(response => {
          if (response.data.success) {
            let records = response.data.records;
            for (let i = 0; i < records.length; i++) {
              let p = records[i]["property_id"];
              this.keyed[p] = records[i];
            }
          }
          this.isEditing = false;
        });
    }
  }
};
</script>