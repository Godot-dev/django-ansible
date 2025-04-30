<template>

  <FormComponent
      :fields="fields"
      form-title="Create your new account"
      submit-text="Create"
      redirection-path="/login"
      redirection-text="Sign in"
      acc-text="Already here? "
      :submit="register"
  />
</template>

<script setup>
import axios from 'axios'
import Cookies from 'js-cookie'
import {inject} from "vue";
import { useRouter } from 'vue-router'
import FormComponent from "@/components/FormComponent.vue";


const router = useRouter()

const API_URL = inject('API_URL');

const fields = [
  {'required':true, 'type':'text', name:'username', placeholder:'Enter your username'},
  {'required':true, 'type':'email', name:'email', placeholder:'Enter your mail address'},
  {'required':true, 'type':'password1', name:'password1', placeholder:'Enter your password'},
  {'required':true, 'type':'password2', name:'password2', placeholder:'Confirm your password'},
]

async function register(formData) {
  console.log(formData)
  console.log(formData.username)
  try {
    await axios.get(API_URL + 'login-set-cookie/', { withCredentials: true })
    const response = await axios.post(API_URL + 'register/', {
      username: formData.username,
      password1: formData.password1,
      password2: formData.password2,
      email: formData.email,
    }, {
      headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'Content-Type': 'application/json'},
      withCredentials: true // 🔥 Important pour les cookies
    })
    console.log('Compte créé !', response)
    await router.push('/login')
  } catch (err) {
    console.error('Erreur de connexion', err)
  }
}
</script>