use faq;

create table basic (
    QID smallint unsigned,
    share tinyint unsigned,
    service varchar(100)
)DEFAULT CHARSET=utf8;

show columns from basic;

insert into basic values( 1, 1, 'Mail' );
create table faq (
    QID smallint unsigned,
    lang varchar(2),
    question varchar(255),
    answer varchar(2048)
)DEFAULT CHARSET=utf8;

show columns from faq;

insert into faq values(
    1,
    'JP',
    '大量送信を行いたい',
    '本サービスは、大量送信を想定したサービスではありません。
    直接お客様サーバよりインターネットに向けて、弊社設備を介さず送信するようご検討ください。' 
);

