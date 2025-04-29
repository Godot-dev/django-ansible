<template>
  <HeaderComponent/>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.account-form{
  height: 100%;
  display: flex;
  justify-content: center; /* Centre horizontalement */
  align-items: center;     /* Centre verticalement */
  align-content: center;
  flex-direction: column;
}
</style>
<script setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
</script>