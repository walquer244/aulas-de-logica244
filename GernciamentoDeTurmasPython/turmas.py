import random
from tabulate import tabulate

def criar_turma(turmas):
    nome = input("Qual o nome da turma?: ")
    nova_turma = {
        "id": random.randint(1000,9999), 
        "nome" : nome
        }
    turmas.append(nova_turma)
    print("Turma criada com sucesso!!!")
    return

def lista_turmas(turmas):
    print(tabulate(turmas, headers="keys", tablefmt = "grid"))
    return

def buscar_turma(turmas, id_busca):
    for turma in turmas:
        if turma["id"] == id_busca:
            return turma
        
