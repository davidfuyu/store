<template>
  <v-overlay :value="$axiosLoader.loading">
    <v-progress-circular indeterminate size="64"></v-progress-circular>
  </v-overlay>
</template>
<script>
export default {
  name: "DialogLoading",
  data() {
    return {};
  },
  props: {
    msg: {
      type: String,
      default: "Loading, please wait..."
    },
    width: {
      type: Number,
      default: 300
    },
    color: {
      type: String,
      default: "primary"
    },
    dark: {
      type: Boolean,
      default: true
    },
    light: {
      type: Boolean,
      default: false
    },
    barColor: {
      type: String,
      default: "white"
    }
  }
};
</script>
