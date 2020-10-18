<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height">
        <v-avatar class="mr-10" color="grey darken-1" size="42"></v-avatar>

        <v-btn text>Title</v-btn>

        <v-spacer></v-spacer>

        <v-btn color="primary" dark class="ma-2" @click="dialog_login = !dialog_login">
          Open Dialog 2
        </v-btn>
        <v-dialog v-model="dialog_login" max-width="500px" :persistent="auth_loading">
          <v-list three-line subheader>
            <v-list-item>
              <v-list-item-content>
                <v-tabs v-model="auth_tab">
                  <v-tab :disabled="auth_loading">Login</v-tab>
                  <v-tab :disabled="auth_loading">Registration</v-tab>

                  <v-tab-item>
                    <v-text-field
                      label="Login" :rules="rules" hide-details="auto"
                      :disabled="auth_loading"></v-text-field>
                    <v-text-field
                      label="Password" type="password" :rules="rules" hide-details="auto"
                      :disabled="auth_loading"></v-text-field>
                    <v-col class="text-right">
                      <v-btn
                        class="ma-2" :loading="auth_loading" :disabled="auth_loading"
                        color="primary" @click="auth_loading = 'loading'">
                        Login
                      </v-btn>
                    </v-col>
                    <v-divider class="my-2"></v-divider>
                    <v-btn depressed>
                      Normal
                      <v-icon right><GoogleSVG/></v-icon>
                    </v-btn>
                  </v-tab-item>
                  <v-tab-item>
                    <v-text-field
                      label="Login" :rules="rules" hide-details="auto"
                      :disabled="auth_loading"></v-text-field>
                    <v-text-field
                      label="Email" :rules="rules" hide-details="auto"
                      :disabled="auth_loading"></v-text-field>
                    <v-text-field
                      label="Password" type="password" :rules="rules" hide-details="auto"
                      :disabled="auth_loading"></v-text-field>
                    <v-col class="text-right">
                      <v-btn
                        class="ma-2" :loading="auth_loading" :disabled="auth_loading"
                        color="primary" @click="auth_loading = 'loading'">
                        Register
                      </v-btn>
                    </v-col>
                  </v-tab-item>
                </v-tabs>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-dialog>
        
        <v-responsive max-width="260">
          <v-text-field dense flat hide-details rounded solo-inverted></v-text-field>
        </v-responsive>

      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
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
            <v-sheet min-height="70vh" rounded="lg" >
              <router-view></router-view>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
 import GoogleSVG from "@/assets/logo-google.svg";
 export default {
   components: {
     GoogleSVG
   },
   data: () => ({
     dialog_login: false,
     auth_loading: false,
     auth_tab: null,
     links: [
       { title: 'Home', url: '/', icon: 'mdi-home' },
       { title: 'About', url: '/about',icon: 'mdi-help-box' },
     ]
   }),
 }
</script>
