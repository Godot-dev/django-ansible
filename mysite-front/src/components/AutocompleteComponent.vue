<script setup>
import {inject, ref} from 'vue'
import axios from "axios";
const API_URL = inject('API_URL');

defineProps({
  updateSuggestions: Function,
});


const query = ref('')
const suggestions = ref([])

async function onInput() {
  if (query.value.length < 2) {
    suggestions.value = []
    return
  }

  // suggestions.value = updateSuggestions()
  await axios.get(API_URL + 'autocomplete/', { params:{"q": query.value}, withCredentials: true }).then((response) => {
    suggestions.value = []
    response.data['places'].forEach((p) => {
      suggestions.value.push(p.name)
    })
  })
}

function selectSuggestion(suggestion) {
  query.value = suggestion
  suggestions.value = []
}
</script>

<template>
  <div class="autocomplete-container">
    <input
        type="text"
        v-model="query"
        @input="onInput"
        placeholder="Tapez quelque chose..."
    />
    <ul v-if="suggestions.length" class="autocomplete-results">
      <li v-for="(suggestion, index) in suggestions" :key="index" @click="selectSuggestion(suggestion)">
        {{ suggestion }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.autocomplete-container {
  position: relative;
  width: 300px;
}

.autocomplete-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border: 1px solid #ccc;
  list-style: none;
  margin: 0;
  padding: 0;
  z-index: 1000;
}

.autocomplete-results li {
  padding: 8px;
  cursor: pointer;
}

.autocomplete-results li:hover {
  background-color: #f0f0f0;
}
</style>