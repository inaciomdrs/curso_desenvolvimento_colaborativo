CREATE TABLE Usuario (
  login VARCHAR(30)  NOT NULL  ,
  codigo INTEGER UNSIGNED ZEROFILL  NOT NULL   AUTO_INCREMENT,
  senha VARCHAR(30)  NULL  ,
  email VARCHAR(30)  NULL  ,
  imagem BLOB  NULL    ,
PRIMARY KEY(login));



CREATE TABLE Tarefa (
  id INTEGER UNSIGNED  NOT NULL  ,
  Usuario_login VARCHAR(30)  NOT NULL  ,
  titulo VARCHAR(30)  NULL   AUTO_INCREMENT,
  descricao VARCHAR(200)  NOT NULL  ,
  data_limite DATE  NOT NULL  ,
  status_2 INTEGER ZEROFILL  NOT NULL  ,
  prioridade INTEGER ZEROFILL  NOT NULL    ,
PRIMARY KEY(id)  ,
INDEX Tarefa_FKIndex1(Usuario_login),
  FOREIGN KEY(Usuario_login)
    REFERENCES Usuario(login)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);




