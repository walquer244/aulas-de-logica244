# lista = []
# def calcular_media(a=0, b=0, c=0,d=0):
#     lista.append(float(input("Digite suas notas: ")))
#     lista.append(float(input("Digite suas notas: ")))
#     lista.append(float(input("Digite suas notas: ")))
#     lista.append(float(input("Digite suas notas: ")))
#     print(lista)    

lista1 = []
nome_aluno = input("Digite seu nome: ")
for i in range(3):
    lista1.append(float(input(f"Digite suas notas {nome_aluno}: ")))
print(lista1) 

def calcular_media():
    return sum(lista1) / 3
print(calcular_media())


def verifica_situacao():
    if calcular_media() < 5:
        print("Você foi reprovado!!")
    elif calcular_media()  >= 7:
        print("Você esta aprovado !!!") 
    elif 5 <= calcular_media() < 6.9:
        print("Você esta de recuperação !!!")
    return
verifica_situacao()
