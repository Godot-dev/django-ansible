<template>
  <label for="fruit">Choisissez un fruit :</label>
  <select id="fruit" name="fruit">
    <option value="pomme">Pomme</option>
    <option value="banane">Banane</option>
    <option value="cerise">Cerise</option>
  </select>

  <h1>Manage</h1>

  <div id="manage">

    <div class="manageBlocks">
      <h2>Manage your train stations</h2>
      <form @submit.prevent="addStation">
        <Multiselect
            v-model="selectedStation"
            :options="suggestions"
            placeholder="Select a station to add to your list"
            :searchable="true"
            label="name"
            track-by="id"
            :loading="isLoading"
            @search-change="onInput"
        />
        <button type="submit">Add</button>

        <ul>

        </ul>
      </form>

    </div>

    <div class="manageBlocks">
      <h2>Manage your Journeys</h2>
<!--      <Multiselect-->
<!--          v-model="selectedJourney.name"-->
<!--          :options="suggestions"-->
<!--          placeholder="Select a station to add to your list"-->
<!--          :searchable="true"-->
<!--          :loading="isLoading"-->
<!--          @search-change="onInput"-->

<!--      />-->
    </div>


  </div>


</template>

<script setup>
import {inject, ref} from 'vue'
import axios from "axios";
import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.css'
import Cookies from 'js-cookie'

const API_URL = inject('API_URL');


const selectedStation = ref({})
const suggestions = ref([])
const isLoading = ref(false);

async function onInput(query) {
  if (query.length < 2) {
    suggestions.value = []
    return
  }
  isLoading.value = true;
  await axios.get(API_URL + 'autocomplete/', { params:{"q": query}, withCredentials: true }).then((response) => {
    suggestions.value = []
    if(response.data['places']) {
      response.data['places'].forEach((p) => {
        suggestions.value.push({'name': p.name, 'id': p.id})
      })
    }
  })
  isLoading.value = false;
}

async function addStation() {
  try {
    console.log(selectedStation.value['id'])
    await axios.get(API_URL + 'login-set-cookie/', { withCredentials: true })
    await axios.post(API_URL + 'stations/', {
      id: selectedStation.value['id'],
      name: selectedStation.value['name']
    }, {
      headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'Content-Type': 'application/json'},
      withCredentials: true // 🔥 Important pour les cookies
    })
  } catch (err) {
    console.error('Erreur de connexion', err)
  }
}
</script>

<style scoped>
#manage {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: space-around;

}

.manageBlocks {
  display: flex;
  flex-flow: column nowrap;
}

h1, h2{
  text-align: center;
}

form{
  display: flex;
  border: 1px solid #ccc;
}

</style>
