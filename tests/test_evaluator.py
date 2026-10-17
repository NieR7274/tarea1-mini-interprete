"""Pruebas del evaluador: del AST a un numero."""

import pytest

from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis
from mini_interprete.errores import ErrorDeEvaluacion, ErrorDeSintaxis


def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14

# Pruebas Tarea

    #Casos normaler

def test_Suma_Resta():
    assert interpretar("3 + 4 - 5") == 2

def test_Multiplicacion_Divicion():
    assert interpretar("5 * 6 / 3") == 10

    #Casos Frontera

def test_Multiples_Parentesis():
    assert interpretar("((5))") == 5

def test_Resta_Positivo_Negativo():
    assert interpretar("1 - (0-1)") == 2

def test_Multiplicacion_Negativos():
    assert interpretar("(0-1) * (0 -1 )") == 1


def test_division_por_cero():
    with pytest.raises(ErrorDeEvaluacion, match="division entre cero"):
        interpretar("5 / 0")

def test_operador_incompleto():
    with pytest.raises(ErrorDeSintaxis): 
        interpretar("3 +")

def test_dato_no_numerico():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("a + b")