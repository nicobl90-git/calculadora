"""
Actividad 1:

Define variables para almacenar el nombre, edad y profesión del usuario.

Solicita estos datos por teclado utilizando input().

Imprime en pantalla un mensaje personalizado incluyendo todos estos datos.


print("¡Bienvenido! Por favor, ingresa tus datos.")
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
profesion = input("¿Cuál es tu profesión? ")

print(f"¡Hola, {nombre}! Tienes {edad} años y tu profesión es {profesion}.")
"""

"""
Actividad 2

Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.

Usa condicionales para validar y mostrar sólo los números pares.
"""

print("Los primeros 10 números pares son:")
for i in range(1, 20):  # Iteramos desde 1 hasta 19
    if i % 2 == 0:  # Verificamos si el número es par
        print(i)
