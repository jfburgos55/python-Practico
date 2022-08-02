#Autor: John Burgos
#Fecha: 2022/02/08
#Descripción: Programa creado para aprender tuplas
print("\n+---------- Tuplas ----------+")
tupla=('Casa','2',345,'Perro',99)
print("\nElementos de la tupla: ", tupla)
print("Elementos de la tupla: 0: ", tupla[0])
print("Elementos de la tupla: 1: ", tupla[1])
print("Elementos de la tupla: 2: ", tupla[2])
print("Elementos de la tupla: 3: ", tupla[3])
print("Elementos de la tupla: 4: ", tupla[4])
#tupla datos
tuplaN=(1,2,3,4,5,6,7,8,9)
print(tuplaN)
print(tuplaN[4:9])
print(tuplaN[:3])
print(tuplaN[2:])
tuplaConcatenada=tupla+tuplaN
print(tuplaConcatenada)
print("Elementos de la tuplaConcatenada: ",len(tuplaConcatenada))