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

        <v-carousel
          :continuous=false
          hide-delimiter-background
          show-arrows-on-hover
        >

          <v-carousel-item
            v-for="(questao, i) in questoes"
            :key="i"
          >

            <v-card
              class="mx-auto"
              max-width="400"

              light
            >
              <v-img
                class="white--text align-end"
                height="200px"
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              >
                <v-card-title>Top 10 Australian beaches</v-card-title>
              </v-img>

              <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

              <v-card-text class="text--primary">
                <v-container fluid>
                  <p>{{ radios || 'null' }}</p>
                  {{ i }}
                  <v-radio-group :mandatory="false" v-model="radios">
                    <v-radio label="Radio 1" value="radio-1"></v-radio>
                    <v-radio label="Radio 2" value="radio-2"></v-radio>
                  </v-radio-group>
                </v-container>
                <v-btn
                  color="orange"
                  text
                  @click="$emit('input', i+1)"
                >
                  Enviar
                </v-btn>
                <v-btn
                  color="orange"
                  text
                  @click="$emit('next')"
                >
                  next
                </v-btn>
              </v-card-text>

              <v-card-actions>

                teste
                <v-btn
                  color="orange"
                  @click="nextItem"
                >
                  Enviar
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-carousel-item>
        </v-carousel>

      </v-container>
      <v-container>

        <vuetify-audio :ended="audioFinish" :file="file"></vuetify-audio>
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
      this.$emit('change', 1);
    },
  },
};
</script>
