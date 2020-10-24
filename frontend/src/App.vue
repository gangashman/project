<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height content-div">
        <v-avatar class="mr-10" color="grey darken-1" size="42"></v-avatar>

        <v-btn text>Title</v-btn>

        <v-spacer></v-spacer>

        <AuthWindow/>
        
        <v-responsive max-width="260">
          <v-text-field dense flat hide-details rounded solo-inverted></v-text-field>
        </v-responsive>

      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container class="content-div">
        <v-row>
          <v-col cols="2" class="menu-column">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <template v-for="link in links">
                  <router-link :to="link.url" :key="link.title">
                    <v-list-item :key="link.title" link>

                      <v-list-item-icon>
                        <v-icon>{{ link.icon }}</v-icon>
                      </v-list-item-icon>

                      <v-list-item-content>
                        <v-list-item-title>{{ link.title }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </router-link>

                  <!-- <v-divider class="my-2"></v-divider> -->
                </template>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
 .content-div {
     max-width: 1200px!important;
 }
 .menu-column {
     min-width: 180px!important;
 }
</style>

<script>
 import AuthWindow from "@/components/AuthWindow.vue";
 export default {
   components: {
     AuthWindow
   },
   data: () => ({
     backend_url: process.env.VUE_APP_BACKEND_URL,
     links: [
       { title: 'Home', url: '/', icon: 'mdi-home' },
       { title: 'About', url: '/about',icon: 'mdi-help-box' },
     ]
   }),
 }
</script>
