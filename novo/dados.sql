CREATE DATABASE poit_dos_sabores;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(200) NOT NULL,
telefone VARCHAR(20) NOT NULL,
cpf CHAR(12) UNIQUE NOT NULL,
endereco VARCHAR(255) NOT NULL,
numero VARCHAR(10),
bairro VARCHAR(60) NOT NULL,
cidade VARCHAR(60) NOT NULL,
estado VARCHAR(50),
cep VARCHAR(8) NOT NULL,
complemento VARCHAR(100) NOT NULL,
data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pedido (
id_pedido INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
tipo_de_pedido ENUM('presencial','delivery', 'retirada')  NOT NULL,
status_do_pedido ENUM('preparo','pronto', 'entregue') NOT NULL,
data_do_pedido DATETIME NOT NULL,
tempo_estimado TIME NULL,
valor_total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
taxa_entrega DECIMAL(10,2) DEFAULT 0.00,
numero_mesa INT,
observacoes TEXT
);

CREATE TABLE IF NOT EXISTS produto (
id_produto INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(200) NOT NULL,
preco DECIMAL(10,2)NOT NULL CHECK(preco > 0),
categoria VARCHAR(100) NOT NULL,
estoque INT DEFAULT 0,
descricao TEXT
);

CREATE TABLE IF NOT EXISTS funcionario (
id_funcionario INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome VARCHAR(200) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
senha_hash VARCHAR(255) NOT NULL,
cargo VARCHAR(100) NOT NULL,
nivel_acesso ENUM('funcionario','administrador') NOT NULL DEFAULT 'funcionario',
ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS pagamento (
id_pagamento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
valor DECIMAL(10,2) NOT NULL DEFAULT 0.00,
tipo_de_pagamento ENUM('dinheiro','pix','cartao','dividir') NOT NULL,
status_pagamento ENUM('pendente','pago','cancelado') DEFAULT 'pendente',
data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP
);



