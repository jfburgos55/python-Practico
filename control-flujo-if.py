#Autor: John Burgos
#Fecha: 2022/02/08
#Descripción: Programa creado para aprender control de flujo
print("\n+---------- Control de Flujo - IF ----------+")
numero = int(input("Digita un número del 1 al 1000: "))
if numero < 400:
    print("El número que has escrito es menor a 400!!")
else:
    print("El número que has escrito es mayor o igual a 400!!")
print("Has escrito el número: " + str(numero))
#Cadena de texto:
cadena=input("Introduzca una cadena de texto: ")
if cadena.endswith("a") or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
    print("La cadena de texto acaba en vocal!!")
print("La cadena escrita es: " + cadena)