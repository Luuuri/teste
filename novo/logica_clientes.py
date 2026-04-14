import json  # Trabalhar com arquivos JSON
from pathlib import Path  # Manipular caminhos de arquivos

# =========================================================
# CONFIGURAÇÃO INICIAL
# =========================================================

lista_clientes = []  # Lista principal de clientes em memória

# Define o caminho do arquivo clientes.json dentro da pasta dados
ARQUIVO_CLIENTES = Path(__file__).resolve().parent.parent / "dados" / "clientes.json"

# =========================================================
# MANIPULAÇÃO DE ARQUIVO (LOAD / SAVE)
# =========================================================

def carregar_clientes():
    # Verifica se o arquivo existe antes de tentar ler
    if not ARQUIVO_CLIENTES.exists():
        return []

    # Abre o arquivo em modo leitura com codificação UTF-8
    with ARQUIVO_CLIENTES.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)  # Converte JSON em lista Python


def salvar_clientes(lista_clientes):
    # Garante que a pasta existe antes de salvar
    ARQUIVO_CLIENTES.parent.mkdir(parents=True, exist_ok=True)

    # Abre o arquivo em modo escrita
    with ARQUIVO_CLIENTES.open("w", encoding="utf-8") as arquivo:
        # Salva a lista em formato JSON organizado
        json.dump(lista_clientes, arquivo, ensure_ascii=False, indent=4)

# =========================================================
# CRUD DE CLIENTES
# =========================================================

def novo_cliente(lista_clientes, nome, cpf, telefone, email="", endereco=None):
    # Cria um dicionário com os dados do cliente
    cliente = {
        "id": len(lista_clientes) + 1,  # ID incremental baseado na lista
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "endereco": endereco or {},  # Usa dicionário vazio se não informado
        "pedidos": [],  # Lista de pedidos do cliente
        "status_cliente": "Regular"
    }

    lista_clientes.append(cliente)  # Adiciona o cliente na lista


def listar_clientes(lista_clientes):
    # Percorre e exibe cada cliente
    for cliente in lista_clientes:
        return lista_clientes
        

def buscar_cliente(lista_clientes, nome_busca):
    # Procura cliente pelo nome (ignorando maiúsculas/minúsculas)
    for cliente in lista_clientes:
        if nome_busca.lower() in cliente["nome"].lower():
            return cliente
    return None  # Retorna None se não encontrar


def editar_cliente(cliente, novo_nome):
    # Atualiza apenas o nome do cliente
    cliente["nome"] = novo_nome

# =========================================================
# REGRAS DE NEGÓCIO (STATUS DO CLIENTE)
# =========================================================

def calcular_status(cliente):
    pedidos = cliente["pedidos"]  # Lista de pedidos do cliente
    
    # Se não houver pedidos, status padrão
    if len(pedidos) == 0:
        return "Regular"
    
    nao_pagos = 0  # Contador de pedidos não pagos
    
    # Conta quantos pedidos não foram pagos
    for pedido in pedidos:
        if pedido["status_pagamento"] != "pago":
            nao_pagos += 1
    
    # Define o status com base na quantidade de pendências
    if nao_pagos == 0:
        return "Regular"
    elif nao_pagos == 1:
        return "Pendente"
    else: 
        return "Irregular"


def atualizar_status(cliente):
    # Atualiza o status do cliente com base nos pedidos
    cliente["status_cliente"] = calcular_status(cliente)