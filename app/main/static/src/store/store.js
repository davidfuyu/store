import Vue from "vue";
import Vuex from "vuex";
import { userProfile } from "./store-user";
import { organism } from "./store-organism";
import { property } from "./store-property";
import { category } from "./store-property-category";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    organism,
    property,
    category,
    userProfile,
  }
});
