#Ainda estou desenvolvendo :)
"""
cliente = {
    "id": 1,
    "nome" : "Débora",
    "telefone" : "93991529220",
    "cpf" : "01908369205",
    "email" : "debora@gmail.com",
    "endereco" : [],
    "pedidos" : [],
    "status" : "Regular"
}
"""
clientes = []

_prox_id_cliente = 1

def novo_cliente(nome_cliente, telefone, cpf):
    global _prox_id_cliente
    
    cliente = {
        "id_cliente" : _prox_id_cliente,
        "nome_cliente" : nome_cliente,
        "telefone" : telefone,
        "cpf" : cpf,
        "endereco" : [],
        "pedidos" : [],
        "status" : "Regular"
    }
    
    clientes.append(cliente)
    _prox_id_cliente += 1
    
    return cliente

def listar_clientes():
    return clientes

def buscar_cliente_(id_cliente, data, nome_cliente, status_regularidade):
    pass

def editar_cliente(id_cliente, nome_cliente=None, telefone=None, endereco=None):
    pass

def apagar_cliente():
    pass

def visualizar_cliente():
    pass

def adicionar_endereco(id_cliente, nome_endereco, cep, numero, logradouro, complemento, bairro, cidade):
    pass

def pedidos_do_cliente(id_pedido, id_cliente, origem_pedido, data_pedido, status_pedido, status_pagamento):
    pass

novo_cliente("Luisa", "91988421366", "123")
