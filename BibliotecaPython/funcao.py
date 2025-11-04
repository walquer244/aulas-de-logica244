def adicionar_livros(listaLivros):
    nome = input("Digite o titulo do seu livro: ")
    autor = input("Digite o nome do autor do seu livro: ")
    status = "Livro Disponivel"
    informacoes = {
        'titulo': nome,
        "autor" : autor,
        "status" : status
    }
    listaLivros.append(informacoes)
    return listaLivros

def emprestar_livro(listaLivros):
    titulo = input("Digite o título do livro a ser emprestado: ")
    for livro in listaLivros:
        if livro["titulo"] == titulo:
            livro["status"] = "Livro emprestado"
            print(f'O livro "{titulo}" foi emprestado com sucesso.')
            return
    print("Livro não encontrado.")

def devolver_livro(listaLivros):
    titulo = input("Digite o título do livro a ser devolvido: ")
    dia = input("Diga o dia em que o livro foi devolvido: ")
    for livro in listaLivros:
        if livro["titulo"] == titulo:
            livro["status"] = f"Livro devolvido em {dia}"
            print(f'O livro "{titulo}" foi devolvido com sucesso.')
            return
    print("Livro não encontrado.")

def exibir_livros(listaLivros):
    # if not listaLivros:
    #     print("Nenhum livro cadastrado.")
    # else:
    #     for livro in listaLivros:
    #         print(f"{livro['titulo']}")
    print(listaLivros)