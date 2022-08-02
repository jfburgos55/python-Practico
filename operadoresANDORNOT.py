#Autor: John Burgos
#Fecha: 2022/01/13
#Descripción: Programa creado para aprender operadores and or not
print()
print("+---------- Operadores AND - OR - NOT ----------+")
print()
def operadorand(ope1,ope2):
    print("Resultado de",ope1,"AND",ope2,"= ",ope1 and ope2)
print("+- Operador AND -+")
operadorand(True,True)
operadorand(True,False)
operadorand(False,True)
operadorand(False,False)

def operadoror(ope1,ope2):
    print("Resultado de",ope1,"OR",ope2,"= ",ope1 or ope2)
print("+- Operador OR -+")
operadoror(True,True)
operadoror(True,False)
operadoror(False,True)
operadoror(False,False)

print("+- Operador NOT -+")
print("Resultador de NOT True: ", not True)
print("Resultado de NOT False: ", not False)