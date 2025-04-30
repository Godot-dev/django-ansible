<script setup>
import {inject} from "vue";
import axios from "axios";
import { useLinksStore } from '@/stores/links'

const linksStore = useLinksStore()
//let links = ref([]);
const API_URL = inject('API_URL');

axios.get(API_URL + 'current-user/', { withCredentials: true }).then((response) => {
  if('username' in response.data){
    sessionStorage.setItem("username", response.data.username);
    linksStore.updateLinks(true)
  }else{
      // Nobody is connected
    linksStore.updateLinks(false)
  }
});
</script>

<template>
<nav>
  <ul>
    <li v-for="item in linksStore.links" :key="item.label">
      <router-link :to="item.route">{{item.label}}</router-link>
    </li>
  </ul>
</nav>
</template>

<style scoped>
nav{
  text-align: center;
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
    a{
      color: white;
      text-decoration: none;  /* Enlève le soulignement */
    }

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
      a{
        color: black;
        &:hover{
          color: red;
        }
      }

    }
  }
}

</style>