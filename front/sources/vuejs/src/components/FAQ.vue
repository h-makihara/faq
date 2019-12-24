<template>
  <div class="FAQ">
    <h1>{{ faq_msg }}</h1>
    <button v-on:click="button">ボタン</button>
    <h2 v-show="showText">{{ faq_text }}</h2>
  </div>
</template>

<script>
export default {
  name: 'FAQ',
  data () {
    return {
      faq_msg: 'FAQの世界へようこそ',
      faq_text: '押してはいけない。',
      showText: false
    }
  },
  methods: {
    button: function () {
          this.showText = !this.showText
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1,h2 {
  font-weight: normal;
  margin: 40px 0 0;
}
a {
  color: #42b983;
}
</style>
