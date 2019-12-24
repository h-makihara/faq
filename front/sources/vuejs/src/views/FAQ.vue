<template>
  <div class="show">
    <qaList></qaList>
    <qaShow></qaShow>
    <qaRelation msg="Welcome to FAQ world"/>
  </div>
</template>

<script>
// @ is an alias to /src
import qaRelation from '@/components/faq_component.vue'
import qaList from '@/components/qa_list.vue'
import qaShow from '@/components/qa_show.vue'
//import FAQ from '@/components/FAQ.vue'

export default {
  name: 'show',
  components: {
    qaList,
    qaShow,
    qaRelation
  }
}
</script>
