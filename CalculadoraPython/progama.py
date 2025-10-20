from operacoes import *
import emoji

emoji = emoji.emojize(":red_heart:", variant="emoji_type")


while True:
    print("Seja bem vindo a Calculadora!")
    print("1 - Soma.")
    print("2 - Subtraçao.")
    print("3 - Multiplicaçao.")
    print("4 - Divisao.")
    print("5 - Tabuada.")
    print("0 - Sair")
    op = input("Digite uma opção: ")

    if op == "1":
        x = float(input("Digite um número para efutuar a operaçao : "))
        y = float(input("Digite um número para efutuar a operaçao : "))
        print(f"A divisao dos números é igual a: {soma(x,y)}")
    if op == "2":
        x = float(input("Digite um número para efutuar a operaçao : "))
        y = float(input("Digite um número para efutuar a operaçao : "))
        print(f"A divisao dos números é igual a: {subtracao(x,y)}")
    if op == "3":
        x = float(input("Digite um número para efutuar a operaçao : ")) 
        y = float(input("Digite um número para efutuar a operaçao : "))
        print(f"A divisao dos números é igual a: {multiplicacao(x,y)}")
    if op == "4":
        x = float(input("Digite um número para efutuar a operaçao : "))
        y = float(input("Digite um número para efutuar a operaçao : "))
        print(f"A divisao dos números é igual a: {divisao(x,y)}")
    if op == "5":
        x = float(input("Digite um valor: "))
        tabuada(x)
    if op == "0":
        print(f"Obrigado por usar nossa calculadora, volte sempre {emoji}!!!")
        break
    else:
        print("Desculpe. Informação invalida!!!")
