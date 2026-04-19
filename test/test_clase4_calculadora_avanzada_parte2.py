"""
Markers

3-Parametrización
Para sumar y restar, usa @pytest.mark.parametrize con al menos tres datasets distintos.

Etiqueta los tests de sumar con @pytest.mark.smoke.

Etiqueta los tests de dividir que validan la excepción con @pytest.mark.exception.


4-Muestra cómo filtrar la ejecución:

pytest -m smoke        # solo tests “sumar”

pytest -m exception    # solo tests “dividir” con error



5-Reporte HTML

Genera el informe con: pytest --html=report.html.

Sube report.html junto con tu Pull Request.

#Para una PR, tenemos que cambiar de rama, hacer un commit con los cambios, subir la rama a GitHub y luego crear el Pull Request desde GitHub.

"""



import pytest
from calculadora import sumar, restar, multiplicar, dividir
 
 
# ── FIXTURES ──────────────────────────────────────────────────────────────────
 
@pytest.fixture
def enteros():
    """Par de enteros: (10, 2)"""
    return 10, 2
 
 
@pytest.fixture
def flotantes():
    """Par de flotantes: (0.1, 0.2)"""
    return 0.1, 0.2
 
 
# ── TESTS: SUMAR (con parametrize + mark smoke) ───────────────────────────────
 
@pytest.mark.smoke
@pytest.mark.parametrize("a, b, esperado", [
    (1,   2,   3),       # positivos simples
    (-5,  3,  -2),       # negativo + positivo
    (0,   0,   0),       # casos borde con ceros
])
def test_sumar_parametrizado(a, b, esperado): #Esta función llama al parámetro
    assert sumar(a, b) == esperado
 
@pytest.mark.smoke
def test_sumar_flotantes(flotantes): #Esta función llama al fixture
    a, b = flotantes
    assert sumar(a, b) == pytest.approx(0.3)
 
 
# ── TESTS: RESTAR (con parametrize) ──────────────────────────────────────────
 
@pytest.mark.parametrize("a, b, esperado", [
    (10,  2,   8),       # positivos simples
    (0,   5,  -5),       # resultado negativo
    (-3, -1,  -2),       # ambos negativos
])
def test_restar_parametrizado(a, b, esperado):
    assert restar(a, b) == esperado
 
def test_restar_flotantes(flotantes):
    a, b = flotantes
    assert restar(a, b) == pytest.approx(-0.1)
 
 
# ── TESTS: MULTIPLICAR ────────────────────────────────────────────────────────
 
def test_multiplicar_exito(enteros):
    a, b = enteros
    assert multiplicar(a, b) == 20
 
def test_multiplicar_flotantes(flotantes):
    a, b = flotantes
    assert multiplicar(a, b) == pytest.approx(0.02)
 
 
# ── TESTS: DIVIDIR ────────────────────────────────────────────────────────────
 
def test_dividir_exito(enteros):
    a, b = enteros
    assert dividir(a, b) == 5.0
 
@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(10, 0)

"""-------------------------- NO INCLUIMOS LA FUNCION PRINCIPAL DE LA CALCULADORA ------------------------------------------------"""