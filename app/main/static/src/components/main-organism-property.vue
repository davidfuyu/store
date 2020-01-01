<template>
  <v-container fluid>
    <div :hidden="!displayContent">
      <b style="font-size:2em">{{name}}</b>
      <!-- <div v-for="(c, i) in categories" :key="i">
        <b style="font-size:1.5em">{{c}}</b>
        <div v-for="(p,j) in categorizedProperty[c]" :key="j">
          {{p['property_name']}}
          <span v-show="op[p['property_id']]">{{op[p['property_id']]['value']}}</span>
        </div>
      </div>-->
      <v-data-table :headers="headers" :items="op" :hide-default-footer="true"></v-data-table>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  data() {
    return {
      displayContent: false,
      name: "",
      // op: {
      //   type: Object,
      //   default: {}
      // },
      op: [],
      headers: [
        {
          text: "Property",
          align: "right",
          value: "property_name",
          sortable: true
        },
        {
          text: "Value",
          align: "left",
          value: "value",
          sortable: true
        }
      ]
    };
  },
  computed: {
    ...mapState("property", ["property", "categories", "categorizedProperty"])
  },
  created() {
    if (!this.$route.params.id) return;
    let id = this.$route.params.id;
    axios.get("organism-property/" + id).then(response => {
      if (response.data.success) {
        let records = response.data.records;
        this.name = records[0]["name"];
        // for (let i = 0; i < records.length; i++) {
        //   this.op[records[i]["property_id"]] = records[i];
        // }
        this.op = records;
        this.displayContent = true;
      }
    });
  // },
  // watch: {
  //   property: "calculateDisplay",
  //   name: "calculateDisplay"
  // },
  // methods: {
  //   calculateDisplay: function() {
  //     if (this.categorizedProperty && this.categories && this.name) {
  //       this.displayContent = true;
  //     }
  //   }
  }
};
</script>