"""
Actividad 1: Mejorando la calculadora

Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación. Como ser: Sumar(), Restar(), Multiplicar() y Dividir()

Añadir manejo de excepciones para entradas inválidas y división por cero.

"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


print("¡Bienvenido a la calculadora mejorada!")
print(f"1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")

input_opcion = input("Ingrese el número de la operación que desea realizar: ")
while input_opcion not in ['1', '2', '3', '4']:
    print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
    input_opcion = input("Ingrese el número de la operación que desea realizar: ")

if input_opcion == '1':
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"La suma es: {sumar(num1, num2)}")
    except ValueError as e:
        print(f"Error: {e}")

if input_opcion == '2':
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"La resta es: {restar(num1, num2)}")
    except ValueError as e:
        print(f"Error: {e}")

if input_opcion == '3':
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {multiplicar(num1, num2)}")
    except ValueError as e:
        print(f"Error: {e}")

if input_opcion == '4':
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"La división es: {dividir(num1, num2)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

"""
Actividad 2: Git y Github

Git local

Crear una carpeta nueva para el proyecto de calculadora.

Inicializar un repositorio con git init.

Agregar y confirmar cambios con git add y git commit.

GitHub

Crear una cuenta en github.com si no tenés una.

Crear un nuevo repositorio desde tu perfil (usá el mismo nombre del proyecto).

Copiar la URL del repositorio (HTTPS).

Enlazar el repositorio local con GitHub.

Subir los archivos usando git push.


"""