#Autor: John Burgos
#Fecha: 2022/01/16
#Descripción: Programa creado para aprender cadenas de texto
print()
print("+---------- Cadenas De Texto Concatenada ----------+")
print()
cadena1=input("Introduzca la primera cadena: ")
cadena2=input("Introduzca la segunda cadena: ")
cadena3=input("Introduzca la tercera cadena: ")
cadenaConSaltos="\n" + cadena1 + "\n\t" + cadena2 + '\n\t\t' + cadena3
print()
print("Cadena con saltos: ",cadenaConSaltos)