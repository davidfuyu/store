export const user= {
  namespaced: true,
  state: {
    isAuthenticated: false,
  },
  mutations: {
    userLogin(state) {
      state.isAuthenticated = true
    },
    userLogout(state) {
      state.isAuthenticated = false
    },
  },
  getters: {
    isAuthenticated: state => { return state.isAuthenticated; },
  }
};
