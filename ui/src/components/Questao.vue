<template>
  <v-card
    class="mx-auto"
    light

    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      :src="imagem"
      v-if="hasImage"
    >
      <v-card-title class="black--text">{{ titulo }}</v-card-title>
    </v-img>
    <v-card-title  v-if="!hasImage" class="black--text">{{ titulo }}</v-card-title>

    <v-card-text class="text--primary">
      <v-container fluid>

        <p>{{ descricao }}</p>
        <p>{{radios }}</p>


        <v-container v-if="hasAudio">
          <vuetify-audio :file="audio"></vuetify-audio>
        </v-container>

        <v-radio-group :mandatory="false" v-model="radios">

          <template
            v-for="(alternativa, j) in alternativas"
          >
            <v-radio
              :key="j"
              :label=alternativa.descricao
              :value=alternativa.letra
            />
          </template>

        </v-radio-group>
      </v-container>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        @click="submeter"
        color="orange"
      >
        Submeter resposta
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import VuetifyAudio from 'vuetify-audio';

export default {
  name: 'Questao',
  components: {
    'vuetify-audio': VuetifyAudio,
  },
  props: {
    titulo: {

      type: String,
      required: true,
    },
    descricao: {

      type: String,
      required: true,
    },
    imagem: {
      type: String,
      required: false,
    },
    audio: {
      type: String,
      required: false,
    },
    alternativas: {
      type: Array,
      required: true,
    },
    responder: {
      required: true,
    },
  },
  data() {
    return {
      radios: '',
    };
  },
  computed: {
    hasImage() {
      return !!this.imagem;
    },
    hasAudio() {
      return !!this.audio;
    },
  },
  methods: {
    submeter() {
      console.log(this.imagem);
      console.log('respondeu');
      console.log(this.radios);
      this.responder(this.radios);
    },
  },
};
</script>

<style scoped>

</style>
