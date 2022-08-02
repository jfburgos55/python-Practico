#Autor: John Burgos
#Fecha: 2022/01/10
#Descripción: Programa creado para validar usuario y clave
from crypt import *
import crypt
import os
print("+---------- Validar Usuario y Clave ----------+")
print()
username=input("Por favor digite usuario: ")
user=crypt.crypt(username,'salt')
print()
password=input("Por favor digite contraseña: ")
passwd=crypt.crypt(password,'salt')
print(user)
print(passwd)