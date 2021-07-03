<template>
  <GlobalHeader/>
  <router-view/>
</template>

<script>
import GlobalHeader from '@/views/GlobalHeader.vue'

export default {
  components: {
    GlobalHeader
  }
}
</script>


<style>
#app {
  font-family: Noto Sans Japanese, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #002a5a;
  line-height: 1.7;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
