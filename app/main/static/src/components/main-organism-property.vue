<template>
  <v-container fluid>
    <div :hidden="!show">
      <b style="font-size:2em">{{organismName}}</b>
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

      <v-btn
        title="Verify"
        @click="onClickVerifyButton"
        :hidden="isVerifying || isEditing || Object.keys(verifyContent).length == 0"
      >Verify</v-btn>
      <v-btn
        title="Cancel"
        @click="onClickVerifyCancelButton"
        :hidden="!isVerifying || isEditing"
      >Cancel</v-btn>
      <v-btn
        title="Verify All"
        @click="onClickVerifyAllButton"
        :hidden="!isVerifying || isEditing"
      >Verify All</v-btn>
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
              <v-container fluid>
                <v-row>
                  <v-col cols="3">
                    <b>{{p['property_name']}}</b>:
                  </v-col>
                  <v-col cols="5">
                    <div v-if="p['property_type_name'] == 'positive/negative'">
                      <v-autocomplete
                        :items="defaultPositiveNegative"
                        v-model="editContent[p['property_id']]['value']"
                        :disabled="editContent[p['property_id']]['status_name'] == 'verified'"
                        dense
                      ></v-autocomplete>
                    </div>
                    <div v-else-if="p['property_name'] == 'Yes/No'">
                      <v-autocomplete
                        :items="defaultYesNo"
                        v-model="editContent[p['property_id']]['value']"
                        :disabled="editContent[p['property_id']]['status_name'] == 'verified'"
                        dense
                      ></v-autocomplete>
                    </div>
                    <div v-else>
                      <v-text-field
                        v-model="editContent[p['property_id']]['value']"
                        class="text-xs"
                        solo
                        hide-details
                        :disabled="editContent[p['property_id']]['status_name'] == 'verified'"
                        dense
                      ></v-text-field>
                    </div>
                  </v-col>
                  <v-col cols="4">{{editContent[p['property_id']]['reference']}}</v-col>
                </v-row>
              </v-container>
            </div>
          </div>
        </v-form>
      </div>

      <div v-else-if="isVerifying">
        <div v-for="(c, i) in categories" :key="i">
          <b style="font-size:1.5em">{{c.property_category_name}}</b>
          <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
            <div v-if="verifyContent[p['property_id']]">
              <v-checkbox
                style="margin-left:40px"
                v-model="verifyCandidates"
                :label="p['property_name']"
                :value="verifyContent[p['property_id']]"
              ></v-checkbox>
            </div>
          </div>
        </div>
      </div>

      <div v-else :hidden="!show">
        <div v-for="(c, i) in categories" :key="i">
          <b style="font-size:1.5em">{{c.property_category_name}}</b>
          <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
            <div v-if="keyed[p['property_id']]">
              <v-row>
                <v-col cols="8">
                  <span style="margin-left:40px">{{p['property_name']}}:</span>
                  <span v-if="keyed[p['property_id']]['status_name'] == 'verified'">
                    <b>{{keyed[p['property_id']]['value']}}</b>
                  </span>
                  <span v-else>{{keyed[p['property_id']]['value']}}</span>
                </v-col>
                <v-col cols="4">{{keyed[p['property_id']]['reference']}}</v-col>
              </v-row>
            </div>
          </div>
        </div>
      </div>
    </div>
    <reference-dialog
      :showReferenceDialog="showReferenceDialog"
      :onCloseReferenceButton="onCloseReferenceButton"
      :onSubmitReferenceButton="onSubmitReferenceButton"
    ></reference-dialog>
  </v-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import { mapState, mapGetters } from "vuex";
import ReferenceDialog from "@/components/dialog-reference.vue";

export default {
  data() {
    return {
      show: false,
      organismId: 0,
      organismName: "",
      keyed: {},

      isEditing: false,
      editContent: {},

      isVerifying: false,
      verifyCandidates: [],
      verifyContent: {},

      showReferenceDialog: false,

      defaultPositiveNegative: [
        "positive",
        "negative",
        "0-10% positive",
        "26-75% positive",
        "90-100% positive",
        "76-89% positive",
        "11-25% positive",
        "strain instability",
        "Different reactions in different taxa"
      ],

      defaultYesNo: [
        "positive",
        "negative",
        "0-10% positive",
        "+ or -",
        "90-100% positive",
        "strain instability",
        "Different reactions in different taxa"
      ]
    };
  },
  components: {
    ReferenceDialog
  },
  computed: {
    ...mapState("category", ["categories"]),
    ...mapState("property", ["properties", "categorizedProperties"]),
    ...mapGetters("user", ["userId"]),
    showEditSavelButton: function() {
      return this.isEditing;
    },
    showVerifyConfirmButton: function() {
      return this.verifyCandidates.length;
    }
  },
  created() {
    if (!this.$route.params.id) return;
    this.organismId = this.$route.params.id;
    axios
      .get(`organism/${this.organismId}`)
      .then(response => {
        if (response.data.success) {
          let records = response.data.records;
          this.organismName = records[0]["organism_name"];
        }
      })
      .then(
        axios.get(`organism-property/${this.organismId}`).then(res => {
          if (res.data.success) {
            this.updateVuex(res.data.records);
            this.show = true;
          }
        })
      );
  },
  methods: {
    updateVuex: function(records) {
      this.keyed = {};
      this.verifyContent = {};

      for (let i = 0; i < records.length; i++) {
        let record = records[i];
        let pid = record["property_id"];
        this.keyed[pid] = record;

        if (record["status_name"] == "verified") continue;
        if (record["user_id"] == this.userId) continue;
        this.verifyContent[pid] = record;
      }
    },

    // edit
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
      this.showReferenceDialog = true;
    },
    onCloseReferenceButton: function() {
      this.showReferenceDialog = false;
    },
    onSubmitReferenceButton: function(payload) {
      let data = {};
      for (let i = 0; i < this.properties.length; i++) {
        let pid = this.properties[i]["property_id"];
        if (
          (this.keyed[pid] == undefined &&
            this.editContent[pid]["value"] != null) ||
          (this.keyed[pid] != undefined &&
            this.editContent[pid]["value"] != this.keyed[pid]["value"])
        ) {
          data[pid] = JSON.parse(JSON.stringify(this.editContent[pid]));
        }
      }

      axios
        .post(`/organism-property/${this.organismId}`, {
          reference: payload,
          data: data
        })
        .then(response => {
          if (response.data.success) {
            this.updateVuex(response.data.records);
          }
          this.isEditing = false;
        });
      this.showReferenceDialog = false;
    },

    // verify
    onClickVerifyButton: function() {
      this.verifyCandidates = [];
      this.isVerifying = true;
    },
    onClickVerifyCancelButton: function() {
      this.verifyCandidates = [];
      this.isVerifying = false;
    },
    onClickVerifyAllButton: function() {
      this.verifyCandidates = Object.values(this.verifyContent);
    },
    onClickVerifyConfirmButton: function() {
      axios
        .post(
          `/organism-property/${this.organismId}/verify`,
          this.verifyCandidates
        )
        .then(response => {
          if (response.data.success) {
            this.updateVuex(response.data.records);
          }
          this.verifyCandidates = [];
          this.isVerifying = false;
        });
    }
  }
};
</script>