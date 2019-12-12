import Vue from "vue";
import Vuex from "vuex";
import { userProfile} from "./store-user";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    userProfile
  }
});
