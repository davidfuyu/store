import axios from "axios";

export const property = {
  namespaced: true,
  state: {
    properties: [],
    categorizedProperties: {}
  },
  actions: {
    fetch({ commit }) {
      axios.get("/property").then(
        response => {
          commit("set", response.data.records);
        }, err => {
          // eslint-disable-next-line
          console.log(err);
        }
      );
    }
  },
  mutations: {
    set(state, payload) {
      // properties keyed by category
      let cp = {};

      for (let i = 0; i < payload.length; i++) {
        let p = payload[i];

        if (!(p["property_category_name"] in cp)) {
          cp[p["property_category_name"]] = [];
        }

        // category_property
        cp[p["property_category_name"]].push(p);
      }

      state.properties = payload;
      state.categorizedProperties = cp;
    },
  }
};
