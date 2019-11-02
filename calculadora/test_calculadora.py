from multiplicacao import Multiplicacao
from subtracao import Subtracao
from divisao import Divisao
from soma import Soma

def test_soma():
    sun = Soma(8, 12)
    assert sun.soma() == 20

def test_subtracao():
    sub = Subtracao(25, 5)
    assert sub.subtrai() == 20

def test_divisao():
    div = Divisao(10, 2)
    assert div.divide() == 5

def test_multiplicacao():
    mul = Multiplicacao(5, 5)
    assert mul.multiplica() == 25

