<template>
  <div class="create">
    <faq_create msg="Welcome to FAQ world"/>
  </div>
</template>

<script>
// @ is an alias to /src
import faq_create from '@/components/create.vue'
//import FAQ from '@/components/FAQ.vue'

export default {
  name: 'create',
  components: {
    faq_create
  }
}
</script>
