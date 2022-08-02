#Autor: John Burgos
#Fecha: 2022/01/16
#Descripción: Programa creado para aprender cadenas de texto - Eliminando espacios en blanco.
print()
print("+---------- Cadena Texto - Eliminando espacios en blanco ----------+")
cadena = input("Introduzca una cadena de texto, con espacios en blanco al inicio y al final: ")
print("Longitud de la cadena: ", len(cadena))
cadenalstrip = cadena.lstrip()
print("Cadena (lstrip):",cadenalstrip,end=".")
print("\nLongitud de la cadena: (lstrip):",len(cadenalstrip))
cadenarstrip=cadena.rstrip()
print("Cadena (rstrip):",cadenarstrip,end=".")
print("\nLongitud de la cadena: (rstrip):",len(cadenarstrip))
cadenastrip=cadena.strip()
print("Cadena (strip):",cadenastrip,end=".")
print("\nLongitud de la cadena: (strip):",len(cadenastrip))
