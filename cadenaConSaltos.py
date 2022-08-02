#Autor: John Burgos
#Fecha: 2022/01/16
#Descripción: Programa creado para aprender cadenas de texto
print()
print("+---------- Cadenas De Texto Con Saltos ----------+")
print()
cadena1=input("Introduzca la primera cadena: ")
cadena2=input("Introduzca la segunda cadena: ")
cadena3=input("Introduzca la tercera cadena: ")
cadenaConSaltos=r"\n" + cadena1 + r"\n\t" + cadena2 + r'\n\t\t' + cadena3
print()
print("Cadena con saltos: ",cadenaConSaltos)