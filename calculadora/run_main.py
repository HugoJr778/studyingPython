from multiplicacao import Multiplicacao
from subtracao import Subtracao
from divisao import Divisao
from soma import Soma

numero1 = 5
numero2 = 4

def run():
    mul = Multiplicacao(numero1, numero2)
    sub = Subtracao(numero1, numero2)
    div = Divisao(numero1, numero2)
    sun = Soma(numero1, numero2)
    
    print("RESULT--------------------\n")
    print("Número 1: " + str(numero1) + "\n"  + "Número 2: " + str(numero2) + "\n")
    print("MULTIPLICAÇÃO: " + str(mul.multiplica()))
    print("SUBTRAÇÃO: " + str(sub.subtrai()))
    print("DIVISÃO: " + str(div.divide()))
    print("SOMA: " + str(sun.soma()) + "\n")
    print("--------------------------")

run()
