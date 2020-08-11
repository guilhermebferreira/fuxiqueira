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
            <v-list-item-title>Realizar Teste</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contato</v-list-item-title>
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
      <v-toolbar-title>Fuxiqueira</v-toolbar-title>
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
              :progress=false
              :cycle=false
              height="100%"
              hide-delimiters
              hide-delimiter-background
              v-model="model"
            >

              <v-carousel-item
                :key="i"
                v-for="(questao, i) in questoes"
              >

                <questao
                  :titulo="questao.titulo"
                  :descricao="questao.descricao"
                  :alternativas="questao.alternativas"
                  :imagem="questao.imagem"
                  :audio="questao.audio"
                  v-bind:responder="addResposta"

                ></questao>


              </v-carousel-item>
            </v-carousel>
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

import mp3file16b from '@/assets/audio/16b.mp3';
import mixirica1 from '@/assets/img/3mixirica1.jpeg';
import Questao from '@/components/Questao.vue';

export default {
  props: {
    source: String,
  },

  components: {
    questao: Questao,
  },
  computed: {
    active() {
      return 0;
    },
  },
  mounted() {
  },
  data: () => ({
    model: 0,
    drawer: null,
    respostas: [],
    colors: [
      'indigo',
      'warning',
      'pink darken-2',
      'red lighten-1',
      'deep-purple accent-4',
    ],


    questoes: [
      {
        titulo: 'Questao 3',
        descricao: 'Independente da variedade, qual o nome das frutas das fotos?',
        imagem: mixirica1,
        audio: mp3file16b,
        alternativas: [{
          letra: 'a',
          descricao: '﻿Mimosa',
        },

        {
          letra: 'b',
          descricao: 'Tanja',
        },

        {
          letra: 'c',
          descricao: 'Mexerica / Mixirica',
        },

        {
          letra: 'd',
          descricao: 'Poncã / Ponkã',
        },

        {
          letra: 'e',
          descricao: 'Pocã / Pokan',
        },

        {
          letra: 'f',
          descricao: 'Tangerina',
        },

        {
          letra: 'g',
          descricao: 'Bergamota / Vergamota',
        },

        {
          letra: 'h',
          descricao: 'Laranja-cravo',
        },

        {
          letra: 'i',
          descricao: 'Laranja-crava',
        },

        {
          letra: 'j',
          descricao: 'Mangota (Mangote, Mongote, Margota)',
        },

        {
          letra: 'k',
          descricao: 'Morgota',
        },

        {
          letra: 'l',
          descricao: 'Fuxiqueira',
        },

        {
          letra: 'm',
          descricao: 'Mandarina',
        },

        {
          letra: 'n',
          descricao: 'Carioquinha',
        },

        {
          letra: 'o',
          descricao: 'Maricota/Maricote',
        },

        {
          letra: 'p',
          descricao: 'Muricota/Moricota (Muricote, Morocota, Morocote)',
        },

        {
          letra: 'q',
          descricao: 'Murcote/Morcote (Marcota, Morcota, Mucote)',
        },
        ],
      },
      {
        titulo: 'Questao 2',
        descricao: 'Descricao da questão 2',
        alternativas: [
          {
            letra: 'q',
            descricao: 'Opção A',
          },
          {
            letra: 'q',
            descricao: 'Opção B',
          },
          {
            letra: 'q',
            descricao: 'Opção C',
          },
        ],
      },
      {
        titulo: 'Questao 3',
        descricao: 'Descricao da questão 3',
        alternativas: [
          {

            letra: 'q',
            descricao: 'Opção A',
          },
          {
            letra: 'q',
            descricao: 'Opção B',
          },
          {
            letra: 'q',
            descricao: 'Opção C',
          },
          {
            letra: 'q',
            descricao: 'Opção D',
          },
        ],
      },
    ],
  }),
  methods: {
    addResposta(resp) {
      this.respostas.push(resp);
      console.log(this.respostas);
      this.nextItem();
    },
    nextItem() {
      console.log('next');
      this.model += 1;
    },
  },
};
</script>
