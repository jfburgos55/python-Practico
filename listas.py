#Autor: John Burgos
#Fecha: 2022/02/01
#Descripción: Programa creado para aprender listas
print("\n+---------- Listas ----------+")
lista = ["Python","RA-MA","2019","Libro",3]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#Lista Concatenada
lista1=["Camiseta","Pantalón","Zapatillas"]
lista2=["Abrigo","Jersey","Sudadera","Calcetiles"]
print("\nNúmero de elementos de la lista1: ", len(lista1))
print("Lista1: ", lista1)
print("\nNúmero de elementos de la lista2: ", len(lista2))
print("Lista2: ", lista2)
listaConcatenada=lista1+lista2
print("\nNúmeros de elementos de la lista concatenada: ", len(listaConcatenada))
print("Lista Concatenada: ", listaConcatenada)
#Lista agregando elementos
listaAdd=["Camisa","Pantalon","Zapataillas"]
print("\n",listaAdd)
listaAdd = listaAdd + ["Abrigo"]
print(listaAdd)
listaAdd = listaAdd + ["Jersey","Sudadera"]
print(listaAdd)
listaAdd = listaAdd + ["Calcetines"] + ["Bufanda"]
print(listaAdd)
#Eliminando elementos
listaDel=["Camiseta","Pantalón","Zapatillas"]
print("\n",listaDel)
listaDel[1]="Cazadora"
print(listaDel)
del listaDel[1]
print(listaDel)
#Multiplicando listas
listaM=["Camiseta","Pantalón","Zapatillas"]
print("\n", listaM)
listaMul=listaM*3
print(listaMul)