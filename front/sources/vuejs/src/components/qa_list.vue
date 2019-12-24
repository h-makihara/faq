<template>
  <div class="qaListShow">

    <table id="faqList" class="table table-hover">
      <thead class="thead-dark">
        <tr>
          <th>Question</th>
          <th>Service</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <router-link to="/">
              {{ question }}
            </router-link>
          </td>
          <td>
            <router-link to="/">
              {{ service }}
            </router-link>
          </td>
        </tr>
        <tr>
          <td>
            <router-link to="/">
              Question
            </router-link>
          </td>
          <td>
            <router-link to="/">
              service
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>





  </div>
</template>

<script>

export default {
  name: 'qaListShow',
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
