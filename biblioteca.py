import random
 #Pense na usabilidade do usuário, diga que o número que ele tem que adivinhar está de 1 a 20
numeroadv = random.randint(1,20)
vidas = 3
while True:
    useradv = int(input("Tente adivinhar um numero de 1 a 20:  ")) #"Tente adivinhar o número de 1 a 20"
    if useradv == numeroadv:
        print("Acertou miseravi")
        print(f"Voce está com {vidas} vidas..")
        break
    elif useradv > numeroadv:
        print(f"Quase, é menor que {useradv}")
        vidas -= 1 #Você poderia só trocar o "+" pelo "-", e deixar o número "-1" como "1"
        print(f"Voce está com {vidas} vidas..")
    else:
        print(f"Quase, é maior que {useradv}")
        vidas -= 1   #Você poderia só trocar o "+" pelo "-", e deixar o número "-1" como "1"
        print(f"Voce está com {vidas} vidas..")
    if vidas == 0:
        print("Infelismente voce perdeu")
        print("0 vidas.")
        print(f"este é seu numero: {numeroadv}")
        break    

#Obrigado pelas dicas, =)
#se puder, se identifique 😉