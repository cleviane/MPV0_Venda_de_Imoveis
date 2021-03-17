--CREATE DATABASE SISTEMA_IMOVEL;

CREATE TABLE tb_cliente(
    id_cliente SERIAL PRIMARY KEY,
    nm_cliente VARCHAR(100) NOT NULL,
    cpf_cliente VARCHAR(30) NOT NULL,
    rg_cliente VARCHAR(30)NOT NULL,
    endereco VARCHAR(250) NOT NULL,
    cep VARCHAR(15) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    data_nascimento DATE NOT NULL,
    estado_civil VARCHAR(30)NOT NULL,
    profissao VARCHAR(30)NOT NULL
);

CREATE TABLE tb_proprietario (
    id_proprietario SERIAL PRIMARY KEY,
    nm_proprietario VARCHAR(100) NOT NULL,
    cpf_proprietario VARCHAR(30) NOT NULL,
    rg_proprietario VARCHAR(30) NOT NULL,
    data_nascimento DATE NOT NULL,
    estado_civil VARCHAR(30) NOT NULL,
    profissao VARCHAR(30) NOT NULL
);

CREATE TABLE tb_imovel(
    id_imovel SERIAL PRIMARY KEY,
    tipo_imovel VARCHAR(255) NOT NULL,
    endereco VARCHAR(250) NOT NULL,
    complemento VARCHAR(50) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    id_proprietario INTEGER,
    FOREIGN KEY (id_proprietario) REFERENCES tb_proprietario (id_proprietario)
    ON UPDATE CASCADE ON DELETE CASCADE,
    adquirido_em DATE NOT NULL,
    valor_imovel INTEGER
);

CREATE TABLE tb_banco(
    id_banco SERIAL PRIMARY KEY,
    nm_banco VARCHAR(100)
);


CREATE TABLE tb_gastos_imovel(
    id_gasto SERIAL PRIMARY KEY,
    id_imovel INTEGER NOT NULL,
    FOREIGN KEY (id_imovel) REFERENCES tb_imovel( id_imovel)
    ON UPDATE CASCADE ON DELETE CASCADE,
    tipo_gasto VARCHAR(50) NOT NULL,
    valor_gasto INTEGER NOT NULL
);

CREATE TABLE tb_compra(
    id_compra SERIAL PRIMARY KEY,
    id_imovel INTEGER,
    id_cliente INTEGER,
    FOREIGN KEY (id_imovel) REFERENCES tb_imovel (id_imovel)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente)
    ON UPDATE CASCADE ON DELETE CASCADE,
    tipo_pagamento VARCHAR(20),
    id_banco INTEGER UNIQUE,
    FOREIGN KEY (id_banco) REFERENCES tb_banco (id_banco)
    ON UPDATE CASCADE ON DELETE CASCADE,
    valor_pagamento INTEGER
);