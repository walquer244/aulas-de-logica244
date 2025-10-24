from funcoes import *
while True:
    print("1- cadastrar aluno e notas")
    print("2- Exibir relatorio")
    print("0- sair")
    op = input("Digite uma opção: ")

    if op == "1":
        nome = input("Digite o seu nome: ")
        notas = []
        for i in range(4):
            nt = float(input(f"Digite o {i} notas: "))
            notas.append(nt)
            listaditc = {
                nome : notas
            }
    if op =="2":
        print(nome)
        print(notas)
        print(calcular_media())   
        print(verifica_situacao())
    
    if op== "0":
        print("obrigado por usar nosso sistema")
        break