ALTER TABLE pedido ADD COLUMN id_cliente INT NOT NULL; --adicionar a coluna

ALTER  TABLE pedido  
ADD CONSTRAINT fk_cliente
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) 
;

ALTER TABLE pedido ADD COLUMN id_funcionario INT NOT NULL;

ALTER TABLE pedido 
ADD CONSTRAINT fk_funcionario
FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
;

ALTER TABLE pagamento ADD COLUMN id_pedido INT NOT NULL;

ALTER TABLE pagamento 
ADD CONSTRAINT fk_pedido
FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
;
 