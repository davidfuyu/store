<template>
  <v-container>
    <div :hidden="!show">
      Welcom to the database.
      <br />
      <br />There are
      <b>{{countOrganism}}</b> organism and
      <b>{{countOrganismProperty}}</b> records in database.
      <br />You have input
      <b>{{countOther}}</b> and verified
      <b>{{countVerified}}</b> records.
      <br />
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
      countOrganismProperty: 0,
      countVerified: 0,
      countOther: 0
    };
  },
  mounted() {
    axios.get("metrics").then(response => {
      if (response.data.success) {
        let record = response.data.records[0];
        this.countOrganism = record["count_organism"][0]["count"];
        this.countOrganismProperty =
          record["count_organism_property"][0]["count"];
        this.countVerified = record["count_verified"][0]["count"];
        this.countOther = record["count_other"][0]["count"];
        this.show = true;
      }
    });
  }
};
</script>