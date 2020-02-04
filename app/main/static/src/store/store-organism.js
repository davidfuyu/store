import axios from "axios";

export const organism = {
  namespaced: true,
  state: {
    organism: {},
  },
  actions: {
    fetch({ commit }) {
      axios.get("/organism").then(
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
      state.organism = payload;
    },
  },
  getters: {
    organism: state => { return state.organism; },
  }
};
