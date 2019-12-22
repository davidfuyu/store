<template>
  <v-container fluid fill-height>
    <div :hidden="!displayContent">
      {{op}}
      <!-- <v-row no-gutters>
      <v-card flat @click="openDialog">
        <v-col cols="12" sm="12">
          <b style="font-size:2em">{{experiment.title}}</b>
          &nbsp;&nbsp;&nbsp;&nbsp;by: {{experiment.added_by_name}}
        </v-col>
        <v-col cols="12" sm="12">
          ID:
          <b>{{experiment.experiment_id}}</b>
        </v-col>
        <v-col cols="12" sm="12">
          Experiment Date:
          <b>{{experiment.date_experiment}}</b>
        </v-col>
        <v-col v-if="experiment.note" cols="12" sm="12">
          Note:
          <span v-html="experiment.note"></span>
        </v-col>
      </v-card>
      <v-col cols="12" sm="12">
        <v-tabs vertical>
          <v-tab v-for="(section, n) in experiment.detail" :key="n">
            <div class="text-left">{{section.experiment_section_type}}</div>
          </v-tab>
          <v-tab-item v-for="(section, n) in experiment.detail" :key="n">
            <div v-show="displayEditor">
              <tinymce
                :init="init"
                :toolbar="toolbar"
                :plugins="plugins"
                inline:true
                v-model="section.value"
              ></tinymce>

              <v-divider></v-divider>

              <v-btn text color="primary" @click="updateSection(section)">save</v-btn>
              <v-btn text color="primary" @click="displayEditor = !displayEditor">close</v-btn>
            </div>
            <div
              v-show="!displayEditor"
              :key="n"
              v-html="section.value"
              @dblclick="displayEditor= !displayEditor"
            ></div>
          </v-tab-item>
        </v-tabs>
      </v-col>
      </v-row>-->
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      displayContent: false,
      op: {
        type: Object,
        default: {}
      }
    };
  },
  computed: {
    ...mapGetters("projects", ["projects"])
  },
  created() {
    if (!this.$route.params.id) return;
    let id = this.$route.params.id;
    axios.get("organism-property/" + id).then(response => {
      if (response.data.success) {
        this.op = response.data.records;
      }
      this.displayContent = true;
    });
  },
  methods: {
    saveDialog() {
      var form = new FormData();
      var experiment = this.dialogExperiment;
      Object.keys(experiment).forEach(function(key) {
        form.append(key, experiment[key]);
      });

      axios
        .post("experiment", form)
        .then(response => {
          if (response.data.records.length === 1) {
            this.experiment = response.data.records[0];
          }
        })
        .then(() => {
          this.$store.dispatch("userExperiments/fetch");
          this.showDialog = false;
        });
    },
    // updateExperiment: function(event) {
    //   if (this.content.detail) {
    //     var detail = this.content.detail;
    //   }

    //   this.content = event.experiment;

    //   if (detail) {
    //     this.content.detail = detail;
    //   }
    // },
    updateSection: function(section) {
      this.displayEditor = false;
      var form = new FormData();
      Object.keys(section).forEach(function(key) {
        form.append(key, section[key]);
      });

      // axios
      //   .post("experiment-section", form)
      //   .then(response => {
      //     // if (response.data.records.length === 1) {
      //     //   this.content = response.data.records[0];
      //     //   this.callParent({ experiment: this.content });
      //     // }
      //   })
      //   .then(() => {
      //     // this.$store.dispatch("userExperiments/fetch");
      //     // this.close();
      //   });
    }
  }
};
</script>

// hide tiny cloud notice
<style>
.tox-notifications-container {
  display: none !important;
}
</style>