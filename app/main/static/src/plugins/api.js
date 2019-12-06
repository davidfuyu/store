const Api = {
  install(Vue, options) {
    const { axios } = options;

    const loader = new Vue({
      data() {
        return {
          loading: false,
          pendingRequests: 0
        };
      }
    });

    axios.interceptors.request.use(
      config => {
        loader.loading = true;
        loader.pendingRequests++;

        return config;
      },
      error => {
        return Promise.reject(error);
      }
    );

    axios.interceptors.response.use(
      response => {
        loader.pendingRequests--;
        if (loader.pendingRequests === 0) {
          loader.loading = false;
        }

        return response;
      },
      error => {
        return Promise.reject(error);
      }
    );

    Vue.prototype.$http = axios;
    Vue.prototype.$axiosLoader = loader;
  }
};

export default Api;
