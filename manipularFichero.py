#Autor: John Burgos
#Fecha: 2022/06/21
#Descripción: Programa creado para aprender booleanos
print("========== Programa Creado Manipular Fichero ==========")
f = open("fichero.txt","r")
texto=f.read()
print(texto)
f.close

#read line for line
for linea in open("fichero.txt","r"):
    print(linea)

#Write
print("Fichero Inicial")
flectura=open("fichero.txt","r")
texto=flectura.read()
flectura.close()
print(texto)

print("Insertando Linea.....\n")
fescritura=open("fichero.txt","a")
fescritura.write("Nueva linea en el fichero\n")
fescritura.close()
flectura=open("fichero.txt","r")
texto=flectura.read()
flectura.close()
print(texto)