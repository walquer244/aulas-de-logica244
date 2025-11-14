from funcao import *

listaLivros = []

while True:
    print("1 - Adicionar livro")
    print("2 - Exibir todos os livros ")
    print("3 - Emprestar livros")
    print("4 - Devolver livro ")
    print("0 - Sair")
    op = input("Digite uma opção: ")

    if op == "1":
        adicionar_livros(listaLivros)

    elif op == "2":
        exibir_livros(listaLivros)

    elif op == "3":
        emprestar_livro(listaLivros)

    elif op == "4":
        devolver_livro(listaLivros)

    elif op == "0":
        print("Obrigado por usar nossa biblioteca!!!. Volte sempre!!!")
        break 
    else:
        print("Opção invalida!!")
