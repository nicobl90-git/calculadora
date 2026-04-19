"""
Pytest

1-Casos de prueba por operación Crea dos tests para cada función (sumar, restar, multiplicar, dividir):

Éxito : resultado correcto.

Error : comportamiento esperado ante fallo (p. ej. dividir debe lanzar ValueError al dividir por 0)

2-Fixtures

Conserva el fixture de enteros existente.

Añade un segundo fixture con valores flotantes (0.1, 0.2) y utilízalo donde corresponda.
"""




import pytest
from calculadora import sumar, restar, multiplicar, dividir


"""------------------------------ FIXTURES --------------------------------------------"""

@pytest.fixture
def numeros_enteros():
    """ Par de enteros: 2 y 3"""
    return 2, 3

@pytest.fixture
def numeros_negativos():
    """ Par de negativos: -2 y -3"""
    return -2, -3

@pytest.fixture
def numeros_flotantes():
    """ Par de flotantes: 0.1 y 0.2"""
    return 0.1, 0.2

@pytest.fixture
def numeros_division_cero():
    """ Par para división: 10 y 0"""
    return 10, 0

"""-------------------------- TEST: SUMAR ------------------------------------------------"""


def test_sumar_enteros(numeros_enteros): # Pongo entre parentesis la función del fixture que quiero usar
    a, b = numeros_enteros # Desempaquetamos el fixture para obtener los valores individuales
    assert sumar(a, b) == 5  

def test_sumar_negativos(numeros_negativos):
    a, b = numeros_negativos
    assert sumar(a, b) == -5

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert sumar(a, b) == pytest.approx(0.3) # Al trabajar con flotantes, hay que poner el pytest.approx para evitar problemas de precisión


"""-------------------------- TEST: RESTAR ------------------------------------------------"""


def test_restar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) == -1   

def test_restar_negativos(numeros_negativos):
    a, b = numeros_negativos
    assert restar(a, b) == 1

def test_restar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert restar(a, b) == pytest.approx(-0.1)


"""-------------------------- TEST: MULTIPLICAR ------------------------------------------------"""


def test_multiplicar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 6

def test_multiplicar_negativos(numeros_negativos):
    a, b = numeros_negativos
    assert multiplicar(a, b) == 6

def test_multiplicar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert multiplicar(a, b) == pytest.approx(0.02)


"""-------------------------- TEST: DIVIDIR ------------------------------------------------"""


def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == pytest.approx(0.6666666666666666)

def test_dividir_negativos(numeros_negativos):
    a, b = numeros_negativos
    assert dividir(a, b) == pytest.approx(0.6666666666666666)

def test_dividir_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert dividir(a, b) == pytest.approx(0.5)

def test_dividir_por_cero(numeros_division_cero):
    a, b = numeros_division_cero
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        dividir(a, b)
 

"""-------------------------- NO INCLUIMOS LA FUNCION PRINCIPAL DE LA CALCULADORA ------------------------------------------------"""