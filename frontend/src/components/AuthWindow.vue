<template>
  <div>
    <v-btn color="primary" dark class="ma-2" @click="dialog_auth = !dialog_auth">
      Sign in
    </v-btn>
    <v-dialog v-model="dialog_auth" max-width="500px" :persistent="auth_loading">
      <v-list three-line subheader>
        <v-list-item>
          <v-list-item-content>
            <v-tabs v-model="auth_tab">
              <v-tab :disabled="auth_loading">Login</v-tab>
              <v-tab :disabled="auth_loading">Registration</v-tab>

              <v-tab-item>
                <v-form v-model="login_valid" ref="login_form">
                  <v-text-field
                    v-model="login_data.username"
                    label="Username" :counter="32"
                    :rules="rules.required"
                    :hint="login_errors.username" persistent-hint
                    :disabled="auth_loading"></v-text-field>
                  <v-text-field
                    v-model="login_data.password"
                    label="Password" type="password"
                    :rules="rules.required"
                    :hint="login_errors.password" persistent-hint
                    :disabled="auth_loading"></v-text-field>

                  <v-col class="error-block"
                         v-for="error in login_nonfield_errors" v-bind:key="error.message">
                    <v-alert dense outlined type="error">
                      {{ error.message }}
                    </v-alert>
                  </v-col>

                  <v-col class="text-right">
                    <v-btn
                      v-on:click="login"
                      :loading="auth_loading" :disabled="auth_loading||!login_valid"
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
                </v-form>
              </v-tab-item>
              <v-tab-item>
                <v-form v-model="register_valid" ref="register_form">
                  <v-text-field
                    label="Username"
                    v-model="register_data.username" :counter="32"
                    :rules="rules.required"
                    :hint="register_errors.username" persistent-hint
                    :disabled="auth_loading"></v-text-field>
                  <v-text-field
                    label="Email" v-model="register_data.email"
                    :rules="rules.email|rules.required"
                    :hint="register_errors.email" persistent-hint
                    :disabled="auth_loading"></v-text-field>
                  <v-text-field
                    label="Password" type="password"
                    :rules="rules.required"
                    v-model="register_data.password"
                    :hint="register_errors.password1" persistent-hint
                    :disabled="auth_loading"></v-text-field>
                  
                  <v-col class="error-block"
                         v-for="error in register_nonfield_errors" v-bind:key="error.message">
                    <v-alert dense outlined type="error">
                      {{ error.message }}
                    </v-alert>
                  </v-col>

                  <v-col class="text-right">
                    <v-btn
                      v-on:click="register"
                      :loading="auth_loading" :disabled="auth_loading||!register_valid"
                      color="primary">
                      Register
                    </v-btn>
                  </v-col>
                </v-form>
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
 .error-block {
     padding-bottom: 0px!important;
 }
 .error-block .v-alert {
     margin-bottom: 3px;
 }
</style>

<script>
 import gql from 'graphql-tag'
 
 export default {
   components: {
   },
   data: () => ({
     dialog_auth: false,
     login_valid: false,
     register_valid: false,

     auth_loading: false,
     login_errors: {},
     login_nonfield_errors: [],
     register_errors: {},
     register_nonfield_errors: [],

     auth_tab: null,
     login_data: {},
     register_data: {},

      rules: {
        required: [value => !!value || "Required."],
        email: [
          v => !!v || 'Field is required',
          v => !v || /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ],
      }
   }),
   methods: {
     format_field_errors(errors) {
       let result = {}
       for (const [key, value] of Object.entries(errors)) {
         result[key] = value[0].message
       }
       return result
     },
     login: function (event) {
       if (!this.$refs.login_form.validate()) {
         return
       }
       this.auth_loading = true
       this.login_errors = {}
       this.login_nonfield_errors = []

       this.$apollo.mutate({
         mutation: gql`mutation ($password: String!, $username: String!) {
           tokenAuth(username: $username, password: $password) {
             success,
             errors,
             token,
             refreshToken,
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
         if (!data.data.tokenAuth.success) {
           this.login_nonfield_errors = data.data.tokenAuth.errors.nonFieldErrors
           this.login_errors = this.format_field_errors(data.data.tokenAuth.errors)
         } else {
           localStorage.setItem('auth-token', data.data.tokenAuth.token)
           localStorage.setItem('auth-refresh-token', data.data.tokenAuth.refreshToken)
           this.dialog_auth = false
         }
         this.auth_loading = false
       }).catch((error) => {
         this.login_nonfield_errors = error.graphQLErrors
         this.auth_loading = false
       })
     },
     register: function (event) {
       if (!this.$refs.register_form.validate()) {
         return
       }
       this.auth_loading = true
       this.register_errors = {}
       this.register_nonfield_errors = []

       this.$apollo.mutate({
         mutation: gql`mutation (
           $username: String!, $email: String!, $password1: String!, $password2: String!
         ) {
           register(
             username: $username,
             email: $email,
             password1: $password1,
             password2: $password2,
           ) {
             success,
             errors,
             token,
             refreshToken,
           }
         }`,
         variables: {
           username: this.register_data.username,
           email: this.register_data.email,
           password1: this.register_data.password,
           password2: this.register_data.password,
         },
       }).then((data) => {
         if (!data.data.register.success) {
           this.register_nonfield_errors = data.data.register.errors.nonFieldErrors
           this.register_errors = this.format_field_errors(data.data.register.errors)
         } else {
           localStorage.setItem('auth-token', data.data.register.token)
           localStorage.setItem('auth-refresh-token', data.data.register.refreshToken)
           this.dialog_auth = false
         }
         this.auth_loading = false
       }).catch((error) => {
         this.register_nonfield_errors = error.graphQLErrors
         this.auth_loading = false
       })
     }
   }
 }
</script>
