<template>
  <v-container>
    <div :hidden="!show">
      Welcom to the database.
      <br />
      <br />There are
      <b>{{countOrganism}}</b> organism and
      <b>{{countOrganismProperty}}</b> records currently in the database
      <br />
      <br />Login to continue.
    </div>
  </v-container>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  data() {
    return {
      show: false,
      countOrganism: 0,
      countOrganismProperty: 0
    };
  },
  mounted() {
    axios.get("metrics/general").then(response => {
      if (response.data.success) {
        let record = response.data.records[0];
        this.countOrganism = record["count_organism"][0]["count"];
        this.countOrganismProperty =
          record["count_organism_property"][0]["count"];
        this.show = true;
      }
    });
  }
};
</script>