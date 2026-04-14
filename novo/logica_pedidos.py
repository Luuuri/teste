# =========================================================
# CONFIGURAÇÕES DE PEDIDO
# =========================================================

# Tipos possíveis de pedido
tipo = "presencial", "online", "retirada"

# Valor total inicial padrão
valor_total = 0

# Status possíveis de pagamento
status_pagamento = "esperando_pagamento", "pago", "cancelado"


# =========================================================
# CRIAÇÃO DE PEDIDOS
# =========================================================

def novo_pedido(cliente, tipo, valor_total, status_pagamento): 

    # Importa a lógica de clientes para atualizar o status
    from app import logica_clientes

    # Cria um dicionário com os dados do pedido
    pedido = {
        "id": len(cliente["pedidos"]) + 1,  # ID incremental por cliente
        "tipo": tipo,
        "valor_total": valor_total,
        "status_pagamento": status_pagamento
    }
    
    # Adiciona o pedido à lista do cliente
    cliente["pedidos"].append(pedido)
    
    # Atualiza automaticamente o status do cliente
    logica_clientes.atualizar_status(cliente)
    
    return pedido  # Retorna o pedido criado