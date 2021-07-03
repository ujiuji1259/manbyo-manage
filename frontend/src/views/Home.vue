<template>
  <div class="home">
    <search/>
  </div>
</template>

<script>
// @ is an alias to /src
import search from '@/components/Search.vue'

export default {
  name: 'Home',
  components: {
    search
  }
}
</script>
