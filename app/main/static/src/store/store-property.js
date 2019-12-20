import axios from "axios";

export const property = {
  namespaced: true,
  state: {
    property: {},
  },
  actions: {
    fetch({ commit }) {
      axios.get("/property").then(
        response => {
          commit("set", response.data);
        }, err => {
          // eslint-disable-next-line
          console.log(err);
        }
      );
    }
  },
  mutations: {
    set(state, payload) {
      state.property = payload;
    },
  },
  getters: {
    property: state => { return state.property; },
  }
};
