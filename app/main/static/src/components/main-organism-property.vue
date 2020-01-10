<template>
  <v-container fluid>
    <div>
      <b style="font-size:2em">{{name}}</b>
      <v-btn title="Edit" @click.prevent.stop="enableEdit = !enableEdit">edit</v-btn>
      <div v-if="enableEdit">
        <v-form>
          <div v-for="(c, i) in categories" :key="i">
            <b style="font-size:1.5em">{{c.property_category_name}}</b>
            <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
              <v-container>
                <v-row>
                  <v-col cols="5">{{p['property_name']}}:</v-col>
                  <v-col cols="5">
                    <v-text-field
                      v-model="formField[p['property_id']]['value']"
                      class="text-xs"
                      solo
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </div>
        </v-form>
      </div>
      <div v-else>
        <div v-for="(c, i) in categories" :key="i">
          <b style="font-size:1.5em">{{c.property_category_name}}</b>
          <div v-for="(p,j) in categorizedProperties[c.property_category_name]" :key="j">
            <div v-if="keyed[p['property_id']]">
              {{p['property_name']}}:{{keyed[p['property_id']]['value']}}
              <!-- <span v-show="op[p['property_id']]">{{op[p['property_id']]['value']}}</span> -->
            </div>
          </div>
        </div>
      </div>

      <!-- <v-data-table :headers="headers" :items="op" :hide-default-footer="true"></v-data-table> -->
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  data() {
    return {
      enableEdit: false,
      name: "",
      keyed: {},
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
    ...mapState("category", ["categories"]),
    ...mapState("property", ["properties", "categorizedProperties"]),
    formField: function() {
      let form = {};
      for (let i = 0; i < this.properties.length; i++) {
        let p = this.properties[i]["property_id"];
        if (this.keyed[p]) {
          form[p] = this.keyed[p];
        } else {
          form[p] = {};
          form[p]["property_id"] = p;
          form[p]["value"] = null;
        }
      }
      return form;
    }
  },
  created() {
    if (!this.$route.params.id) return;
    let id = this.$route.params.id;
    axios.get("organism-property/" + id).then(response => {
      if (response.data.success) {
        let records = response.data.records;
        this.name = records[0]["name"];
        for (let i = 0; i < records.length; i++) {
          let p = records[i]["property_id"];
          this.keyed[p] = records[i];
        }
      }
    });
  },
  methods: {
    buildForm: function() {
    }
  }
};
</script>