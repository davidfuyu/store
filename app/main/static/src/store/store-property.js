import axios from "axios";

export const property = {
  namespaced: true,
  state: {
    property: {},
    categories: [],
    categorizedProperty: {}
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
      let cp = {};
      let corder = {};
      for (let i = 0; i < payload.length; i++) {
        let p = payload[i];

        // category
        if (!(p["property_category_order"] in corder)) {
          corder[p["property_category_order"]] = p['property_category_name'];
        }

        // category_property
        if (!(p["property_category_name"] in cp)) {
          cp[p["property_category_name"]] = [];
        }
        cp[p["property_category_name"]].push(p);
      }

      let arr = Object.keys(corder);
      arr.sort();
      let category = [];
      for (let j = 0; j < arr.length; j++) {
        category.push(corder[arr[j]]);
      }

      state.property = payload;
      state.categories = category;
      state.categorizedProperty = cp;
    },
  },
  getters: {
    property: state => { return state.property; },
  }
};
