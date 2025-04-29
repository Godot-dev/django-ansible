<template>
  <div>Déconnexion...</div>
</template>

<script setup>
import { onMounted, inject } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const API_URL = inject('API_URL') // ou utilise ton propre système de config
const router = useRouter()
sessionStorage.clear()

onMounted(async () => {
  try {
    await axios.post(API_URL + 'logout/', {}, {
      withCredentials: true
    })
    console.log('Déconnecté avec succès')
  } catch (error) {
    console.error('Erreur de déconnexion', error)
  } finally {
    await router.push('/') // redirection vers page d'accueil
  }
})
</script>
