
create table categoryMap (
    categoryMapID smallint not null primary key unique auto_increment,
    QID smallint unsigned not null,
    categoryID tinyint unsigned not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into categoryMap (QID, categoryID) values(1, 1);

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

create table tags (
    tagID tinyint unsigned not null primary key auto_increment,
    tag varchar(30) not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into tags (tag) values('Mail');
insert into tags (tag) values('MAILER-DAEMON');

create table services (
    serviceID tinyint unsigned not null primary key auto_increment,
    service varchar(30) not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into services (service) values('Mail');

create table scope(
    scopeID tinyint unsigned not null primary key auto_increment,
    scope varchar(30) not null
)DEFAULT CHARSET=utf8 auto_increment=1;
    
insert into scope (scope) values('非公開');
insert into scope (scope) values('社内のみ');
insert into scope (scope) values('社外公開可');

create table JP (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answer varchar(2048) not null
)DEFAULT CHARSET=utf8 auto_increment=1;

insert into JP (scopeID, serviceID, question, answer)
       values(
        1,
        1, 
        '大量送信を行いたい',
        '本サービスは、大量送信を想定したサービスではありません。
        直接お客様サーバよりインターネットに向けて、弊社設備を介さず送信するようご検討ください。' 
);

create table EN (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answer varchar(2048) not null
)DEFAULT CHARSET=utf8 auto_increment=1;


create table CN (
    QID smallint unsigned not null primary key unique auto_increment,
    scopeID smallint unsigned not null,
    serviceID smallint unsigned not null,
    question varchar(255) not null ,
    answeR varchar(2048) not null
)DEFAULT CHARSET=utf8 auto_increment=1;


