import random
from tabulate import tabulate

def cadastra_aluno(alunos):
    nome = input("Qual o nome do aluno?: ")
    novo_aluno = {
        "id": random.randint(1000, 9999),
        "nome" : nome
    }
    alunos.append(novo_aluno)
    print(f"{nome} foi cadastrado com sucesso!!")
    return

def exibir_aluno(alunos):
    print(tabulate(alunos, headers = "keys", tablefmt = "grid"))
    return

def buscar_aluno(alunos, id_busca):
    for aluno in alunos:
        if aluno["id"] == id_busca:
            return aluno