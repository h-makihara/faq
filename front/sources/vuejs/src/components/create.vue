<template>
  <div class="create">
    <h1>{{ msg }}</h1>
    <button v-on:click="button">ボタン</button>
    <h2 v-show="showText">{{ text }}</h2>
  </div>
</template>

<script>
export default {
  name: 'create',
  data () {
    return {
      msg: 'FAQ作成画面',
      text: 'ここでFAQを作成します\nデザイン未定リリース時期未定',
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
