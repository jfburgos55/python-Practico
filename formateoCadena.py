#Autor: John Burgos
#Fecha: 2022/02/01
#Descripción: Programa creado para aprender cadenas de texto - Formateo de cadena.
print()
print("+---------- Cadena Texto - Formateo de Cadena ----------+")
multiplicando=int(input("\nMultiplicando: "))
multiplicador=int(input("\nMultiplicador: "))
print("\nEl resultado de multiplicar %d por %d es %d " %(multiplicando, multiplicador, multiplicando*multiplicador))

#Format
print("\nEl resultado de multiplicar {0} por {1} es {2}".format(multiplicando,multiplicador, multiplicando*multiplicador))