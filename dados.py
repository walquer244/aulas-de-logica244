#contar pares e impares 
contapar = 0
contaimpar = 0
# numeros = int(input("Digite 10 numeros diferentes"))
for i in range(3):
    numeros = int(input("Digite numeros diferentes: ")) #sempre que pedir algo ao usuário, coloque ": "(dois pontos e um espaço, pra quando for digitar, ficar melhor entendível)
    if numeros %2 == 0 :
        contapar += 1
    elif numeros %2 != 0:
        contaimpar += 1
print(contaimpar) #Descreva melhor os outputs
#exemplo: print(f'Quantidade de números ímpares: {contaimpar}')
print(contapar)            
#Pense na usabilidade do usuário