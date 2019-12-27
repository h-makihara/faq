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
            <router-link to="/" id="grpcQtest">
            </router-link>
          </td>
          <td>
            <router-link to="/" id="grpcStest">
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>


  </div>
</template>

<script>
/* eslint-disable */
import { FaqShowRequest } from "../protos/faq_pb"
import { FaqGatewayClient } from '../protos/faq_grpc_web_pb'
/* eslint-enable */

export default {
  name: 'qaListShow',
  data () {
    return {
      question: '大量送信したいのですが、制限されますか？',
      answer  : '大量送信はいけません。\n影響度合いによっては制限いたします',
      service : 'Mail',
      tags    : 'Mail Deliver',
    }
  },
  created: function () {
    this.client = new FaqGatewayClient('http://tp-iij1940.ds.iiji.jp:8001', null, null)
    let request = new FaqShowRequest()
    request.setTimestamp('2019/12/27 10:00:00')
    console.log(this.client)
    this.client.faqShow(request, {}, (err, response) => {
      console.log(response)
      //this.grpcQtest = response.toObject()
    })
//  },
//  methods: {
//    showFAQ: function() {
//      let request = new FaqShowRequest()
//      request.setTimestamp('2019/12/27 10:00:00')
//      console.log(request)
//      this.client.faqShow(request, {}, (err, response) => {
//        this.faq = response.toObject()
//        console.log(this.faq)
//      })
//    }
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
