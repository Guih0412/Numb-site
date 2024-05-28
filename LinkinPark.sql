show databases;
create database linkin_park;
use linkin_park; 



create table avaliacaotable (
nome varchar(70) not null,
email varchar(70) not null,
feedback varchar(255) not null,
nota varchar(2) not null,
sugestao varchar(255) not null,
musica varchar(255) not null
);

select * from avaliacaotable;