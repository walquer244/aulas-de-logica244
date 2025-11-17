# def carregar_cardapio():
#     return[
#         { id: 1, "nome": "Hambúrguer", "preco": 12.5},
#         { id: 2, "nome": "Pizza", "preco": 30},
#         { id: 3, "nome": "Refrigerante", "preco": 5}
#         ] 
#     return

# def exibir_cardapio(cardapio):
#     print(cardapio)
#     return


# def adicionar_pedido(cardapio, pedido):
#     opção = int(input("Qual o numero do seu pedido??? : "))
#     quantidade = int(input("Quantas unidades você deseja??? : "))
#     dict = {
#         "pedido": opção,
#         "quantidade": quantidade,
#         "preco": opção["preco"] * quantidade
#         }

#     pedido.append(dict)
#     return pedido

# def exibir_pedido(pedido):
#     print(pedido)
#     return

# def remover_item(pedido):
#     item = input("diga qual item você deseja retirar: ")
#     removido = False
#     for i in pedido:
#         if i == item:
#             pedido.remove(item)
#             removido = True
#             return

def carregar_cardapio():
    return [
        { "id": 1, "nome": "Hambúrguer", "preco": 12.5 },
        { "id": 2, "nome": "Pizza", "preco": 30 },
        { "id": 3, "nome": "Refrigerante", "preco": 5 }
    ]

def exibir_cardapio(cardapio):
    print(cardapio)

def adicionar_pedido(cardapio, pedido):
    opção = int(input("Qual o número do seu pedido? "))
    quantidade = int(input("Quantas unidades você deseja? "))
    item = next((i for i in cardapio if i["id"] == opção), None)
    if item:
        novo_item = {
            "pedido": item["nome"],
            "quantidade": quantidade,
            "preco": item["preco"] * quantidade
        }
        pedido.append(novo_item)
    else:
        print("❌ Item não encontrado.")
    return pedido

def exibir_pedido(pedido):
    print(pedido)

def remover_item(pedido):
    item = input("Diga qual item você deseja retirar: ")
    removido = False
    for i in pedido:
        if i["pedido"].lower() == item.lower():
            pedido.remove(i)
            removido = True
            break
    if not removido:
        print("❌ Item não encontrado no pedido.")


