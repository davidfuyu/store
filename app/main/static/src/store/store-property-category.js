import axios from "axios";

export const category = {
  namespaced: true,
  state: {
    categories: [],
  },
  actions: {
    fetch({ commit }) {
      axios.get("/category").then(
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
      state.categories = payload;
    },
  }
};
