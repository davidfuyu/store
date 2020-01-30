<template>
  <v-navigation-drawer v-model="drawer" width="290" fixed clipped disable-route-watcher app>
    <v-list dense>
      <template v-for="item in navigationTree">
        <v-list-group v-if="item.children" :key="item.text" :prepend-icon="item.icon">
          <template v-slot:activator>
            <v-list-item>
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item>
          </template>
          <v-list-item
            v-for="child in item.children"
            :key="child.text"
            :to="child.to"
            :disabled="child.disabled"
          >
            <v-list-item-content>
              <v-list-item-title>{{ child.text }}</v-list-item-title>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon small>{{ child.icon }}</v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
        <v-list-item v-else :key="item.text" :to="item.to" :disabled="item.disabled">
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "Navigation",
  data() {
    return {};
  },
  props: {
    drawer: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    ...mapGetters("user", ["isAdmin"]),
    ...mapGetters("organism", { organisms: "organism" }),
    navigationTree: function() {
      let tree = [
        {
          text: "Dashboard",
          icon: "fas fa-tachometer-alt",
          to: "/dashboard",
          disabled: false,
          model: false
        }
      ];

      if (this.organisms.length) {
        let childOrganisms = [];
        for (let i = 0; i < this.organisms.length; i++) {
          let o = this.organisms[i];
          childOrganisms.push({
            text: o["name"],
            to: "/organism-property/" + o["organism_id"],
          });
        }
        tree.push({
          text: "Organisms",
          icon: "fas fa-microscope",
          model: false,
          children: childOrganisms
        });
      }

      return tree;
    }
  },
  methods: {
    toggleDrawer() {
      this.$emit("update:drawer", !this.drawer);
    },
    assignTreeOpen() {
      // once assigned, no update
      if (this.navigationTree.length === 0) {
        for (let i = 0; i < this.myExperimentsOpen.length; i++) {
          let exp = this.myExperimentsOpen[i];
          this.navigationTreeOpen.push({
            text: exp["experiment_id"],
            to: "/experiment/" + exp["experiment_id"],
            icon: "fas fa-list"
          });
        }
      }
    }
  }
};
</script>
