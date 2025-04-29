<template>
  <form @submit.prevent="login">
    <input v-model="username" placeholder="Nom d'utilisateur" />
    <input v-model="password" type="password" placeholder="Mot de passe" />
    <button type="submit">Connexion</button>
  </form>

  <div class="container">
    <div class="heading">SignIn to your account</div>
    <form @submit.prevent="login">
      <div class="input-field">
        <input required type="text" id="username" v-model="username" placeholder="Enter your username"/>
        <label for="username">Username</label>
      </div>
      <div class="input-field">
        <input required type="password" id="password" v-model="password" placeholder="Enter your password"/>
        <label for="password">Password</label>
      </div>

      <div class="btn-container">
        <button class="btn" type="submit">Submit</button>
        <div class="acc-text">
          New here ?
          <span style="color : #0000ff; cursor : pointer;">Create Account</span>
        </div>
      </div>
    </form>
  </div>

</template>

<script setup>
import axios from 'axios'
import Cookies from 'js-cookie'
import {inject, ref} from "vue";

let username = ref('');
let password = ref('');
const API_URL = inject('API_URL');

async function login() {
  try {
    await axios.get(API_URL + 'login-set-cookie/', { withCredentials: true })
    // console.log(res.data)
    // console.log(username)
    // console.log(password.value)
    const response = await axios.post(API_URL + 'login/', {
      username: username.value,
      password: password.value
    }, {
      headers: { 'X-CSRFToken': Cookies.get('csrftoken')},
                  'Content-Type': 'application/json',
                  withCredentials: true // 🔥 Important pour les cookies
    })
    console.log('Connecté !', response)
  } catch (err) {
    console.error('Erreur de connexion', err)
  }
}
</script>

<style scoped>
.container {
  border: solid 1px #8d8d8d;
  padding: 20px;
  border-radius: 20px;
  background-color: #fff;
}

.container .heading {
  font-size: 1.3rem;
  margin-bottom: 20px;
  font-weight: bolder;
}

form {
  max-width: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  gap: 20px;
}

form .btn-container {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 20px;
}

form .btn {
  padding: 10px 20px;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 3px;
  border-radius: 10px;
  border: solid 1px #1034aa;
  border-bottom: solid 1px #90c2ff;
  background: linear-gradient(135deg, #0034de, #006eff);
  color: #fff;
  font-weight: bolder;
  transition: all 0.2s ease;
  //box-shadow: 0px 2px 3px #000d3848, inset 0px 4px 5px #0070f0,
  //inset 0px -4px 5px #002cbb;
  box-shadow: inset 0px 4px 5px #0070f0, inset 0px -4px 5px #002cbb;
  transform: scale(0.995);
}

.input-field {
  position: relative;
}

.input-field label {
  position: absolute;
  color: #8d8d8d;
  pointer-events: none;
  background-color: transparent;
  left: 15px;
  transform: translateY(0.6rem);
  transition: all 0.3s ease;
}

.input-field input {
  padding: 10px 15px;
  font-size: 1rem;
  border-radius: 8px;
  border: solid 1px #8d8d8d;
  letter-spacing: 1px;
  width: 100%;
}

.input-field input:focus,
.input-field input:valid {
  outline: none;
  border: solid 1px #0034de;
}

.input-field input:focus ~ label,
.input-field input:valid ~ label {
  transform: translateY(-51%) translateX(-10px) scale(0.8);
  background-color: #fff;
  padding: 0px 5px;
  color: #0034de;
  font-weight: bold;
  letter-spacing: 1px;
  border: none;
  border-radius: 100px;
}

form .passicon {
  cursor: pointer;
  font-size: 1.3rem;
  position: absolute;
  top: 6px;
  right: 8px;
}

form .close {
  display: none;
}

</style>
