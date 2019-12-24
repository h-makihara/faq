<template>
  <div class="qaDetailShow">

    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" >FAQ詳細(table版)</a>
    </nav>

    <nav class="navbar navbar-light bg-light">
      <span class="navbar-text">
       以下に選択したFAQの詳細内容が表示されます
      </span>
    </nav>
    <table id="faqDetails" class="table">
      <tbody>
        <tr>
          <th scope="row">Question</th>
          <td> {{ question }} </td>
        </tr>
        <tr>
          <th scope="row">Answer</th>
          <td> {{ answer }} </td>
        </tr>
        <tr>
          <th>tags</th>
          <td> {{ tags }} </td>
        </tr>
      </tbody>
    </table>



    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" >FAQ詳細(List版)</a>
    </nav>
    <ul class="list-group" align="left">
      <li class="list-group-item">Q. {{ question }}</li>
      <li class="list-group-item">A. {{ answer }}</li>
      <li class="list-group-item">tag: {{ tags }}</li>
    </ul>





  </div>
</template>

<script>

export default {
  name: 'qaDetailShow',
  data () {
    return {
      question: '大量送信したいのですが、制限されますか？',
      answer  : '大量送信はいけません。\n影響度合いによっては制限いたします',
      service : 'Mail',
      tags    : 'Mail Deliver',
    }
  }
}
</script>

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
td {
  text-align:center;
  white-space: pre-line;
  word-wrap: break-word;
}
</style>
