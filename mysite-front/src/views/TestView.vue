<template>
  <form @submit.prevent="sendRequest">
    <input v-model="apisuite" placeholder="suite lien api" />
    <button type="submit">Connexion</button>
  </form>
</template>

<script setup>
import axios from 'axios'
import {inject, ref} from "vue";

let apisuite = ref('');
const API_URL = inject('API_URL');

async function sendRequest() {
  try {
    const response = await axios.get(API_URL + apisuite.value, {
      username: apisuite.value,
    }, {
      'Content-Type': 'application/json',
      withCredentials: true // 🔥 Important pour les cookies
    })
    console.log('reussi', response)
  } catch (err) {
    console.error('rate', err)
  }
}
</script>
