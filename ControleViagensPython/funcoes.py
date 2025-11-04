import tabulate

def registrar_viagens(listaViagens):
    Nome_do_Motorista = input("Digite o nome do motorista: ")
    Destino = input("Digite o seu destino: ")
    Distancia = float(input("Digite a quilometragem do percurso: "))
    Valor_do_Combustivel = 6.20
    gasto_por_KM = 6.20 * Valor_do_Combustivel
    consumo = Valor_do_Combustivel / Distancia
    Viagem = {
        "Nome do Motorista" : Nome_do_Motorista,
        "Destino ": Destino,
        "Distancia": Distancia,
        "consumo por Km percorrido" : consumo
    }

    listaViagens.append(Viagem)
    return("✅ Viagem registrada com sucesso!!!")
