
create table categoryMap (
    categoryMapID smallint not null primary key unique auto_increment,
    QID smallint unsigned not null,
    categoryID tinyint unsigned not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into categoryMap (QID, categoryID) values(1, 1);
insert into categoryMap (QID, categoryID) values(2, 1);

create table categories (
    categoryID smallint unsigned not null primary key unique auto_increment,
    category varchar(30) not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into categories (category) values('deliver func');

create table tagMap (
    tagMapID smallint not null primary key not null auto_increment,
    QID smallint unsigned not null,
    tagID tinyint unsigned not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into tagMap (QID, tagID) values(1, 1);
insert into tagMap (QID, tagID) values(1, 2);
insert into tagMap (QID, tagID) values(2, 2);

create table tags (
    tagID tinyint unsigned not null primary key auto_increment,
    tag varchar(30) not null unique
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into tags (tag) values('Mail');
insert into tags (tag) values('MAILER-DAEMON');

create table services (
    serviceID tinyint unsigned not null primary key auto_increment,
    service_name varchar(30) not null unique
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into services (service_name) values('Mail');

create table scope(
    scopeID tinyint unsigned not null primary key auto_increment,
    scope varchar(30) not null unique
)DEFAULT CHARSET=utf8 auto_increment=1;
    
insert into scope (scope) values('非公開');
insert into scope (scope) values('社内のみ');
insert into scope (scope) values('社外公開可');

create table JP (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answer varchar(2048) not null,
    createAt DATE not null,
    updateAt DATE not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into JP (scopeID, serviceID, question, answer, createAt, updateAt)
       values(
        1,
        1, 
        '大量送信を行いたい',
        '本サービスは、大量送信を想定したサービスではありません。
        直接お客様サーバよりインターネットに向けて、弊社設備を介さず送信するようご検討ください。',
        '2020-03-16',
        '2020-03-16'
);

insert into JP (scopeID, serviceID, question, answer, createAt, updateAt)
       values(
        1,
        1,
        'MAILER-DAEMONさんからメールが来る',
        '宛先にメールが届かない場合、MAILER-DAEMONからメールが届く場合があります
        本サービスがアドレスを漏洩し、海外の怪しい人からメールが届いているわけではありません。
        今一度宛先情報が正しいかご確認ください。',
        '2020-03-15',
        '2020-03-16'
);

insert into JP (scopeID, serviceID, question, answer, createAt, updateAt)
       values(
        1,
        1,
        '迷惑メールがすり抜けてくる',
        'どのようなメールがすり抜けてくるのかにもよりますが、送信ドメイン認証技術やDMARCといった技術が有効かもしれません。  
        それぞれについては、以下URLをご覧ください  
        - [SPFとは](https://www.nic.ad.jp/ja/basics/terms/spf.html)
        - [DMARCがもっとよくわかる！概要とレコードの読み方](https://sendgrid.kke.co.jp/blog/?p=3137)
        ',
        '2020-03-14',
        '2020-03-15'
);


insert into JP (scopeID, serviceID, question, answer, createAt, updateAt)
       values(
        1,
        1,
        'なりすましメールが来る',
        'なりすましメールの対策としてはSPFが有効です。  
        外部から他者になりすまして送信されてくるメールについては、DMARCが有効です。  
        - [SPFとは](https://www.nic.ad.jp/ja/basics/terms/spf.html)
        - [DMARCがもっとよくわかる！概要とレコードの読み方](https://sendgrid.kke.co.jp/blog/?p=3137)
        ',
        '2020/03/01',
        '2020/03/04'
);


insert into JP (scopeID, serviceID, question, answer, createAt, updateAt)
       values(
        1,
        1,
        'ログインできない',
        'どの画面でしょうか？  
        ログインできない画面、ログインできないアカウント、時間帯、接続元のIPアドレスを合わせて改めてご連絡ください。
        ',
        '2020/03/16',
        '2020/03/16'
);

create table EN (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answer varchar(2048) not null,
    createAt DATE not null,
    updateAt DATE not null
)DEFAULT CHARSET=utf8 auto_increment=1;


create table CN (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answer varchar(2048) not null,
    createAt DATE not null,
    updateAt DATE not null
)DEFAULT CHARSET=utf8 auto_increment=1;


