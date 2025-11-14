from tabulate import tabulate

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("Digite o destino da viagem: ")
    distancia = float(input("Digite a distância percorrida (em km): "))
    consumo = 6.20 * distancia
    gasto = float(input("Digite o valor gasto com combustível (em R$): "))

    

    viagem = {
        "motorista": motorista,
        "destino": destino,
        "distancia": distancia,
        "gasto": gasto,
        "consumo": consumo
    }

    listaViagens.append(viagem)
    print("✅ Viagem registrada com sucesso!")

def exibir_viagens(listaViagens):
    if not listaViagens:
        print("⚠️ Nenhuma viagem registrada.")
        return
    print(tabulate(listaViagens, headers="keys", tablefmt="grid"))

def buscar_motorista(listaViagens):
    nome = input("Digite o nome do motorista para buscar: ")
    viagens_motorista = [v for v in listaViagens if v["motorista"].lower() == nome.lower()]
    if viagens_motorista:
        print(tabulate(viagens_motorista, headers="keys", tablefmt="grid"))
    else:
        print("🚫 Nenhuma viagem encontrada para esse motorista.")

def viagem_mais_cara(listaViagens):
    if not listaViagens:
        print("⚠️ Nenhuma viagem registrada.")
        return
    mais_cara = max(listaViagens, key=lambda v: v["gasto"])
    print("💰 Viagem mais cara:")
    print(tabulate([mais_cara], headers="keys", tablefmt="grid"))

def media_consumo(listaViagens):
    if not listaViagens:
        print("⚠️ Nenhuma viagem registrada.")
        return
    media = sum(v["consumo"] for v in listaViagens) / len(listaViagens)
    print(f"📊 Média geral de consumo: {round(media, 2)} R$/km")




