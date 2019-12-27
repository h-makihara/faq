<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button v-on:click="toggle">toggle</button>
    <h2 v-show="showText">{{ text }}</h2>
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Holy guacamole!</strong> You should check in on some of those fields below.
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <md-button class="md-raised md-primary">Sample</md-button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js Test App',
      text: 'test data',
      showText: false
    }
  },
  methods: {
    toggle: function () {
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
