<template>
  <v-container fluid>
    <div :hidden="!show">
      <b style="font-size:2em">{{name}}</b>
      <v-divider></v-divider>
      <v-btn title="Edit" @click="onClickEditButton" :hidden="isEditing || isVerifying">Edit</v-btn>
      <v-btn
        title="Cancel"
        @click="onClickEditCancelButton"
        :hidden="!isEditing || isVerifying"
      >Cancel</v-btn>
      <v-btn
        title="Save"
        @click="onClickEditSavelButton"
        :hidden="!showEditSavelButton || isVerifying"
      >Save</v-btn>

      <v-btn title="Verify" @click="onClickVerifyButton" :hidden="isVerifying || isEditing">Verify</v-btn>
      <v-btn
        title="Cancel"
        @click="onClickVerifyCancelButton"
        :hidden="!isVerifying || isEditing"
      >Cancel</v-btn>
      <v-btn
        title="Confirm"
        @click="onClickVerifyConfirmButton"
        :hidden="!showVerifyConfirmButton || isEditing"
      >Confirm</v-btn>

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
                      v-model="editContent[p['property_id']]['value']"
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

      <div v-else-if="isVerifying">
        <v-form>
          <div v-for="(c, i) in categories" :key="i">
            <b style="font-size:1.5em">{{c.property_category_name}}</b>
            <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
              <div v-if="keyed[p['property_id']] && ifUserCanVerify(keyed[p['property_id']])">
                <v-checkbox
                  style="margin-left:40px"
                  v-model="verifyContent"
                  :label="p['property_name']"
                  :value="keyed[p['property_id']]"
                ></v-checkbox>
              </div>
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
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      show: false,
      organismId: 0,
      name: "",
      keyed: {},

      isEditing: false,
      editContent: {},

      isVerifying: false,
      verifyContent: []
    };
  },
  computed: {
    ...mapState("category", ["categories"]),
    ...mapState("property", ["properties", "categorizedProperties"]),
    ...mapGetters("user", ["userId"]),
    showEditSavelButton: function() {
      return this.isEditing;
    },
    showVerifyConfirmButton: function() {
      return this.verifyContent.length;
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
          let pid = records[i]["property_id"];
          this.keyed[pid] = records[i];
        }
        this.show = true;
      }
    });
  },
  methods: {
    onClickEditButton: function() {
      for (let i = 0; i < this.properties.length; i++) {
        let pid = this.properties[i]["property_id"];
        if (this.keyed[pid] != null) {
          this.editContent[pid] = JSON.parse(JSON.stringify(this.keyed[pid]));
        } else {
          this.editContent[pid] = {};
          this.editContent[pid]["organism_id"] = this.organismId;
          this.editContent[pid]["property_id"] = pid;
          this.editContent[pid]["value"] = null;
        }
      }
      this.isEditing = true;
    },
    onClickEditCancelButton: function() {
      this.editContent = {};
      this.isEditing = false;
    },
    onClickEditSavelButton: function() {
      let todo = {};
      for (let i = 0; i < this.properties.length; i++) {
        let pid = this.properties[i]["property_id"];
        if (
          (this.keyed[pid] == undefined &&
            this.editContent[pid]["value"] != null) ||
          (this.keyed[pid] != undefined &&
            this.editContent[pid]["value"] != this.keyed[pid]["value"])
        ) {
          todo[pid] = JSON.parse(JSON.stringify(this.editContent[pid]));
        }
      }

      axios
        .post(`/organism-property/${this.organismId}`, todo)
        .then(response => {
          if (response.data.success) {
            let records = response.data.records;
            for (let i = 0; i < records.length; i++) {
              let pid = records[i]["property_id"];
              this.keyed[pid] = records[i];
            }
          }
          this.isEditing = false;
        });
    },
    onClickVerifyButton: function() {
      this.verifyContent = [];
      this.isVerifying = true;
    },
    onClickVerifyCancelButton: function() {
      this.verifyContent = [];
      this.isVerifying = false;
    },
    onClickVerifyConfirmButton: function() {
      axios
        .post(
          `/organism-property/${this.organismId}/verify`,
          this.verifyContent
        )
        .then(response => {
          this.isVerifying = false;
          this.verifyContent = [];
        });
    },
    ifUserCanVerify: function(op) {
      if (op["status_name"] == "verified") return false;
      if (op["user_id"] == this.userId) return false;
      return true;
    }
  }
};
</script>