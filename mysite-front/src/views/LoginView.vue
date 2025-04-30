<template>

<FormComponent
  :fields="fields"
  form-title="Sign in to your account"
  submit-text="Log in"
  redirection-path="/register"
  redirection-text="Create account"
  acc-text="New here? "
  :submit="login"
/>
</template>

<script setup>
import axios from 'axios'
import Cookies from 'js-cookie'
import {inject} from "vue";
import { useRouter } from 'vue-router'
import { useLinksStore } from '@/stores/links'
import FormComponent from "@/components/FormComponent.vue";


const router = useRouter()

const API_URL = inject('API_URL');

const fields = [
  {'required':true, 'type':'text', name:'username', placeholder:'Enter your username'},
  {'required':true, 'type':'password', name:'password', placeholder:'Enter your password'},
]

async function login(formData) {
  try {
    await axios.get(API_URL + 'login-set-cookie/', { withCredentials: true })
    const response = await axios.post(API_URL + 'login/', {
      username: formData.username,
      password: formData.password
    }, {
      headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'Content-Type': 'application/json'},
      withCredentials: true // 🔥 Important pour les cookies
    })
    console.log('Connecté !', response)
    useLinksStore().updateLinks(true) // Update the header links
    await router.push('/dashboard')
  } catch (err) {
    console.error('Erreur de connexion', err)
  }
}
</script>
