export const user= {
  namespaced: true,
  state: {
    isAuthenticated: false,
    user: null,
  },
  mutations: {
    userLogin(state, payload) {
      state.isAuthenticated = true;
      state.user = payload;
    },
    userLogout(state) {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
  getters: {
    userId: state => { return state.user['user_id']; },
  }
};
