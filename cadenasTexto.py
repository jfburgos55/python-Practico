#Autor: John Burgos
#Fecha: 2022/01/16
#Descripción: Programa creado para aprender cadenas de texto
print()
print("+---------- Cadenas De Texto Concatenada ----------+")
print()
cadena1=input("Introduzca la primera cadena: ")
cadena2=input("Introduzca la segunda cadena: ")
cadena3=input("Introduzca la tercera cadena: ")
cadenaSuma=cadena1
cadenaSuma+=' '
cadenaSuma+=cadena2
cadenaSuma+=' '
cadenaSuma+=cadena3
cadenaSuma+=' '
print()
print("Cadena Concatenada: ", cadenaSuma)
print()
print("+------------ COMPROBAR SI PALABRAS ESTAN CONTENIDAS EN UNA CADENA ------------+")
print()
cadena4=input("Introduzca la primera cadena: ")
cadena5=input("Introduzca la segunda cadena: ")
print("¿Esta la segunda cadena contenida en la primera?",cadena4 in cadena4)
