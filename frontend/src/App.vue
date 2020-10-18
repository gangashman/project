<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height">
        <v-avatar class="mr-10" color="grey darken-1" size="42"></v-avatar>

        <v-btn text>Title</v-btn>

        <v-spacer></v-spacer>

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
  export default {
    data: () => ({
      links: [
        { title: 'Home', url: '/', icon: 'mdi-home' },
        { title: 'About', url: '/about',icon: 'mdi-help-box' },
      ]
    }),
  }
</script>
