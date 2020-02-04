export const user = {
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
    userId: state => {
      if (state.user) return state.user['user_id'];
      return null;
    },
    email: state => {
      if (state.user) return state.user['email'];
      return null;
    },
    name: state => {
      if (state.user) return state.user['name'];
      return null;
    },
    isAuthenticated: state => {
      return state.isAuthenticated;
    },
  }
};
