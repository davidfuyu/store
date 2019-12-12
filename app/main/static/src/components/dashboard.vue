<template>
  <v-container>
    Dashboard
    <p>You should see some database records below:</p>
    <div>{{data}}</div>
  </v-container>
</template>

<script>
export default {
  data() {
    return { data: {} };
  },
  mounted() {
    this.$http
      .get("/testdb")
      .then(res => {
        this.data = res.data;
      })
      .catch(function() {
        // console.log("failed");
      });
  }
};
</script>