<template>
  <div class="show">

    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#!">{{ faq_msg }}</a>
    </nav>

    <button v-on:click="button">ボタン</button>
    <h2 v-show="showText">{{ faq_text }}</h2>
  </div>
</template>

<script>

export default {
  name: 'show',
  data () {
    return {
      faq_msg: '関連FAQ一覧',
      faq_text: 'ここに関連FAQを書く予定。\nあくまで予定',
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
  white-space: pre-line;
  word-wrap: break-word;
}
a {
  color: #42b983;
}
</style>
