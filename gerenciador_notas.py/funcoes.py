lista1 = []
def cadastro(nome):
    return

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
