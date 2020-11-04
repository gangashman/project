<template>
  <div>
    <v-btn color="primary" dark class="ma-2" @click="dialog_login = !dialog_login">
      Sign in
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
                  v-model="login_data.username"
                  label="Login" hide-details="auto"
                  :disabled="auth_loading"></v-text-field>
                <v-text-field
                  v-model="login_data.password"
                  label="Password" type="password" hide-details="auto"
                  :disabled="auth_loading"></v-text-field>
                <v-col class="text-right">
                  <v-btn
                    v-on:click="login"
                    class="ma-2" :loading="auth_loading" :disabled="auth_loading"
                    color="primary">
                    Login
                  </v-btn>
                </v-col>
                <v-divider class="my-2"></v-divider>
                
                <div class="text-center">
                  <div class="my-2">
                    <v-btn color="#4c75a3" class="white--text auth-button">
                      Auth with vk
                      <v-icon right>mdi-vk</v-icon>
                    </v-btn>
                  </div>
                  <div class="my-2">
                    <v-btn color="error" class="white--text auth-button">
                      Auth with google
                      <v-icon right>mdi-google</v-icon>
                    </v-btn>
                  </div>
                  <div class="my-2">
                    <v-btn color="#3b5998" class="white--text auth-button">
                      Auth with facebook
                      <v-icon right>mdi-facebook</v-icon>
                    </v-btn>
                  </div>
                </div>
              </v-tab-item>
              <v-tab-item>
                <v-text-field
                  label="Login" hide-details="auto"
                  :disabled="auth_loading"></v-text-field>
                <v-text-field
                  label="Email" hide-details="auto"
                  :disabled="auth_loading"></v-text-field>
                <v-text-field
                  label="Password" type="password" hide-details="auto"
                  :disabled="auth_loading"></v-text-field>
                <v-col class="text-right">
                  <v-btn
                    v-on:click="register"
                    class="ma-2" :loading="auth_loading" :disabled="auth_loading"
                    color="primary">
                    Register
                  </v-btn>
                </v-col>
              </v-tab-item>
            </v-tabs>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-dialog>
  </div>
</template>

<style>
 .auth-button {
     min-width: 400px!important;
 }
</style>

<script>
 import gql from 'graphql-tag'
 
 export default {
   components: {
   },
   data: () => ({
     dialog_login: false,
     auth_loading: false,
     auth_tab: null,
     login_data: {},
   }),
   methods: {
     login: function (event) {
       this.auth_loading = true

       this.$apollo.mutate({
         mutation: gql`mutation {
           tokenAuth(username: $username, password: $password) {
             success,
             errors,
             unarchiving,
             token,
             refreshToken,
             unarchiving,
             user {
               id,
               username,
             }
           }
         }`,
         variables: {
           username: this.login_data.username,
           password: this.login_data.password,
         },
       }).then((data) => {
         console.log(data)
         this.auth_loading = false
       }).catch((error) => {
         console.error(error)
         this.auth_loading = false
       })
     },
     register: function (event) {
       this.auth_loading = true
       this.auth_loading = false
     }
   }
 }
</script>
