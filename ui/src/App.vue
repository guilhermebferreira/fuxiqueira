<template>
  <v-app id="inspire">
    <v-navigation-drawer
      app
      v-model="drawer"
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
      <v-toolbar-title>Teste</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <template>
          <v-progress-linear value="15"></v-progress-linear>
        </template>

        <v-row
          height="100%">
          <v-col>


            <v-carousel
              :continuous=false
              :show-arrows=false
              height="100%"
              hide-delimiter-background
              v-model="model"
            >

              <v-carousel-item
                :key="i"
                v-for="(questao, i) in questoes"
              >

                <v-card
                  class="mx-auto"
                  light

                  max-width="400"
                >
                  <v-img
                    class="white--text align-end"
                    height="200px"
                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                  >
                    <v-card-title>{{ questao.titulo }}</v-card-title>
                  </v-img>

                  <v-card-text class="text--primary">
                    <v-container fluid>
                      <p>{{ questao.descricao }}</p>
                      <p>{{radios }}</p>


                      <v-container>
                        <vuetify-audio :ended="audioFinish" :file="file"></vuetify-audio>
                      </v-container>

                      <v-radio-group :mandatory="false" v-model="radios">

                        <template
                          v-for="(alternativa, j) in questao.alternativas"
                        >
                          <v-radio
                            :key="j"
                            :label=alternativa.descricao
                            :value=alternativa.descricao
                          />
                        </template>

                      </v-radio-group>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                      @click="nextItem"
                      color="orange"
                    >
                      nextItem
                    </v-btn>
                  </v-card-actions>
                </v-card>


              </v-carousel-item>
            </v-carousel>
          </v-col>
          <v-col>

            <v-container>

              <vuetify-audio :ended="audioFinish" :file="file"></vuetify-audio>
            </v-container>
          </v-col>
        </v-row>


      </v-container>


    </v-content>
    <v-footer
      app
      color="indigo"
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import VuetifyAudio from 'vuetify-audio';

export default {
  props: {
    source: String,
  },

  components: {
    'vuetify-audio': VuetifyAudio,
  },
  computed: {
    active() {
      return 0;
    },
  },
  data: () => ({
    model: 0,
    arrows: false,
    drawer: null,
    radios: '',
    file: 'http://www.noiseaddicts.com/samples_1w72b820/290.mp3',
    colors: [
      'indigo',
      'warning',
      'pink darken-2',
      'red lighten-1',
      'deep-purple accent-4',
    ],
    slides: [
      'First',
      'Second',
      'Third',
      'Fourth',
      'Fifth',
    ],
    questoes: [
      {
        titulo: 'Questao 1',
        descricao: 'Descricao da questão 1',
        alternativas: [
          {
            descricao: 'Opção A',
          },
          {
            descricao: 'Opção B',
          },
          {
            descricao: 'Opção C',
          },
        ],
      },
      {
        titulo: 'Questao 2',
        descricao: 'Descricao da questão 2',
        alternativas: [
          {
            descricao: 'Opção A',
          },
          {
            descricao: 'Opção B',
          },
          {
            descricao: 'Opção C',
          },
        ],
      },
      {
        titulo: 'Questao 3',
        descricao: 'Descricao da questão 3',
        alternativas: [
          {
            descricao: 'Opção A',
          },
          {
            descricao: 'Opção B',
          },
          {
            descricao: 'Opção C',
          },
          {
            descricao: 'Opção D',
          },
        ],
      },
    ],
  }),

  methods: {
    audioFinish() {
      console.log('You see this means audio finish.');
    },
    nextItem() {
      console.log('next');
      this.model += 1;
    },
    showHideArrows() {
      this.arrows = !this.arrows;
      console.log(this.arrows);
    },
  },
};
</script>
