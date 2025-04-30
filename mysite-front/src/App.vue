<template>
  <HeaderComponent/>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: 100%;
  width: 100%;
}

router-view{
  flex: 1;
  display: flex;
}

</style>
<script setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
</script>