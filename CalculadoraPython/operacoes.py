#Sistema de calculadora PY
def soma(x,y):
    return x + y
def subtracao(x,y):
    return x - y
def multiplicacao(x,y):
    return x * y
def divisao(x,y):
    return x / y
def tabuada(x):
    for i in range(1,11):
        print(f"{x} x {i} = {x * i}")
