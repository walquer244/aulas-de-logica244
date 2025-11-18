from tabulate import tabulate
from turmas import buscar_turma
from alunos import buscar_aluno


def adicionar_aluno_n_turma(turmas, alunos, relacoes):
    id_aluno = int(input("Qual o id do aluno?: "))
    id_turma = int(input("Qual o id da turma?: "))
    aluno = buscar_aluno(alunos, id_aluno)
    turma = buscar_turma(turmas, id_turma)
    if aluno and turma: 
        relacoes.append({
            "id_aluno": id_aluno, 
            "id_turma" : id_turma
            })
        print(f"{aluno} foi adicionado ao {turma}")
        return
    
def lista_d_alunos_d_turma(relacoes, alunos, turmas):
    id_turma = int(input("Qual o id da turma?: ")) 
    turma = buscar_turma(turmas, id_turma)
       
