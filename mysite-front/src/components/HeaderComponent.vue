<script setup>
import {inject, ref} from "vue";
import axios from "axios";
let user_connected = ref(false);
let username = ref("");
let links = ref([
  {"label": "Home", route: "/"},
  {"label": "About", route: "/about"},
]);
const API_URL = inject('API_URL');

if(!sessionStorage.getItem("username")){
  axios.get(API_URL + 'current-user/', { withCredentials: true }).then((response) => {
    username.value = response.data.username;
    console.log(username.value);
    if(username.value !== "" ){
      user_connected.value = true
      sessionStorage.setItem("username", username.value);
    }
  });
}else{
  username.value = sessionStorage.getItem("username");
  //user_connected.value = true
}
</script>

<template>
<nav>
  <ul>
    <li v-for="item in links" :key="item.label">
      <router-link to="{{item.route}}">{{item.label}}</router-link>
    </li>
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link> |-->
<!--    <router-link to="/test">Test</router-link> |-->
<!--    <span v-if="user_connected">-->
<!--    <router-link to="/manage">Manage</router-link> |-->
<!--    <router-link to="/dashboard">Dashboard</router-link> |-->
<!--    <router-link to="/logout">Logout</router-link>-->
<!--    </span>-->
<!--    <span v-else>-->
<!--    <router-link to="/login" >Login</router-link> |-->
<!--    <router-link to="/register">Register</router-link>-->
<!--    </span>-->
  </ul>
</nav>
</template>

<style scoped>
body {
  background: url("https://hdqwalls.com/download/stranger-things-season-3-2019-4k-5k-38-1920x1080.jpg") center / cover no-repeat;
  height: 100vh;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

ul{
  border-radius: 25px;
  height: fit-content;
  display: inline-flex;
  background-color: rgba(0, 0, 0, .4);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  align-items: center;
  padding: 0 10px;
  margin: 50px 0 0 0;
  li {
    list-style: none;
    color: white;
    font-family: sans-serif;
    font-weight: bold;
    padding: 12px 16px;
    margin: 0 8px;
    position: relative;
    cursor: pointer;
    white-space: nowrap;
    &::before {
      content: " ";
      position: absolute;
      top: 0;
      left:0;
      height:100%;
      width: 100%;
      z-index:-1;
      transition: .2s;
      border-radius: 25px;
    }
    &:hover {
      &::before {
        background: linear-gradient(to bottom, #e8edec, #d2d1d3);
        box-shadow: 0px 3px 20px 0px black;
        transform: scale(1.2);
      }
      color: black;
    }
  }
}

</style>