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
  </div>
</template>

<style>
 .auth-button {
     min-width: 400px!important;
 }
</style>

<script>
 export default {
   components: {
   },
   data: () => ({
     dialog_login: false,
     auth_loading: false,
     auth_tab: null,
   }),
 }
</script>
