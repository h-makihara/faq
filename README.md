# faq
FAQ管理ツールを考えながら作る

## Frontend
gRPC Serverを通じてやりとりする  
Frontに自由をもたせることで使いやすい FAQ を誰もが考え、実装できるようにする
## gRPC Server
その名の通り。  
API Server にアクセスしてデータのやり取りを行う(予定)
## API Server
Python による API サーバ(になる予定)

## FAQ DB
### tables
- basic
    - qid  
      UK  
      FAQのID
    - share  
      公開範囲  
      0: 公開不可  
      1: 社内公開可  
      2: 社外公開可
    - service  
      サービス名
- faq
    - qid  
      UK  
      FAQのID
    - lang  
      言語  
      ex. JP
    - question  
      質問内容  
      必ず lang で宣言した言語で書く
    - answer  
      回答内容  
      必ず lang で宣言した言語で書く
