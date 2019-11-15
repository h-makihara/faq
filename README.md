# faq
FAQ管理ツールを考えながら作る

# やりたいこと
まだ社内にも公開できない内部情報として管理したいものもある  
社内には公開できるが、社外秘となる情報として管理したいものもある  
社外にも公開できる情報として管理したいものもある  
これらが複数のツールにまたがって存在し、場合によっては二重三重管理になっている  
それは情報が陳腐化したり、誤りのある情報を見て誤認識してしまうリスクがある  
じゃあ、これらひっくるめて一元管理すればいいじゃん。  
という思想のもとで作っていく。  

## 運用
1. まずKCSの思想を踏襲し、存在しない情報を内部情報として登録する  
1. 登録した情報を精査し、社内発信できる形に整形する  
1. 整形された情報を基に、社外に発信できそうなら、社外向けの表記に修正し、発信する

## 注意点
- ワークフローをきっちり定めて承認しないと、社外公開は誤発信が笑い事では済まない
- 認証認可どうするかきちんと考えないといけない  
社外発信できるとしても、そのFAQが、全く関係のない第三者に見えていいものではない  
かもしれない。


# 構成
## Frontend
gRPC Serverを通じてやりとりする  
Frontに自由をもたせることで使いやすい FAQ を誰もが考え、実装できるようにする  
protoを踏襲すれば、gRPCサーバを介して情報の授受ができる
## gRPC Server
その名の通り。  
API Server にアクセスしてデータのやり取りを行う  
## API Server
Python による API サーバ  
DB 操作は基本的に API サーバからのみ行う

## FAQ DB
### tables
#### Maps  
- Tagmap  
FAQとタグテーブルを管理  
| ID | qID | tagID |
|--- |---  |---    |
|uint|uint |uint   |
|1   |1    |1      |
|2   |1    |2      |
|3   |1    |3      |
|4   |2    |2      |
|5   |2    |4      |  
- CategoryMap  
FAQとカテゴリテーブルを管理  
| ID | qID | categoryID |
|--- |---  |---         |
|uint|uint |uint        |
|1   |1    |1           |
|2   |1    |2           |
|3   |2    |1           |
|4   |2    |3           |
|5   |3    |3           |

- ScopeMap  
FAQと公開範囲を管理  
管理用に主キーは新たに作らない  
QIDがそのままユニークに紐づくため  
QIDから公開範囲を特定・管理するためのテーブル  
| qID | scopeID |
|---  |---      |
|uint |uint     |
|1    |1        |
|2    |1        |
|3    |0        |
|4    |2        |
|5    |2        |

- ServiceMap  
FAQとサービスを管理  
ScopeMap同様、QIDがそのまま一意にデータを特定するので、管理用の主キーは新たに作らない
| qID | serviceID |
|---  |---        |
|uint |uint       |
|1    |1          |
|2    |1          |
|3    |1          |
|4    |1          |
|5    |1          |

#### FAQ
3つのテーブルのQIDはすべて同期が取れていること  
QID1の質問や回答は、必ず英語、中国語でも言語が変わっても内容が同じこと  
QID同期におけるマスタはJPテーブル  
EN,CNはQIDで検索した場合、作ってなければ存在しない場合がある  
- JP
日本語用FAQ管理テーブル  
| QID | question | answer     | update_at |
|---  |---       |---         |---        |
|uint |string    |string      |date       |
|1    |質問内容  |回答内容    |YYYY/MM/DD |

- EN
英語用FAQ管理テーブル  
| QID | question | answer     | update_at |
|uint |string    |string      |date       |
|---  |---       |---         |---        |
|1    |質問内容  |回答内容    |YYYY/MM/DD |

- CN
中国語用FAQ管理テーブル  
| QID | question | answer     | update_at |
|---  |---       |---         |---        |
|uint |string    |string      |date       |
|1    |質問内容  |回答内容    |YYYY/MM/DD |

#### Others
タグとかカテゴリとか  
- Tags  
タグ情報  
| tagID | tag          |
|---    |---           |
|uint   |string        |
|1      |送信          |
|2      |届かない      |
|3      |MAILER-DAEMON |

- Categories  
カテゴリ情報  
| categoryID | category     |
|---         |---           |
|uint        |string        |
|1           |配送機能      |
|2           |アドレス管理  |
|3           |MAILER-DAEMON |
|4           |フィルタリング|


- Services  
サービス情報  
| serviceID | service |
|---        |---      |
|1          |メール   |
|2          |DNS      |

- Scope  
公開範囲  
| scopeID | scope     |
|---      |---        |
|1        |公開不可   |
|2        |社内公開可 |
|3        |社外公開可 |


# 注意
faq_pb2_grpc.py の faq_pb2 を import する行が、 Python の現在の仕様で  
import に失敗する  
この場合、 4 行目の行頭に from . を追記する。  
