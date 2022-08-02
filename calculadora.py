#Autor: John Burgos
#Fecha: 2022/04/21
#Descripción: Programa calculadora

def sumar():
    print("** SUMA **")
    numero1=int(input("Ingresa el primer numero: "))
    numero2=int(input("Ingresa el segundo numero: "))
    resultado=numero1+numero2
    print("El resultado de la suma es: ", resultado)

def restar():
    print("** RESTA **")
    minuendo = int(input("Ingresa el primer numero: "))
    sustraendo = int(input("Ingresa el segundo numero: "))
    resultado = minuendo - sustraendo
    print("El resultado de la resta es: ", resultado)

def multiplicar():
    print("** MULTIPLICACION **")
    multiplicando = int(input("Ingresa el primer numero: "))
    multiplicador = int(input("Ingresa el segundo numero: "))
    resultado = multiplicando * multiplicador
    print("El resultado de la multiplicacion es: ", resultado)

def dividir():
    try:
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        print("La división es: ", dividendo/divisor)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")

def Factorial():
    factorial=int(input("Introduzca el numero del que quiere calcular el factorial: "))
    print("El factorial de " + str(factorial) + "es: " + str(FactorialCalculo(factorial)))

def FactorialCalculo(numero):
    if numero <= 1:
        return 1
    else:
        return numero * FactorialCalculo(numero-1)

def potencia():
    base=int(input("Introduzca la base de la potencia: "))
    exponente=int(input("Introduzca el exponente de la potencia: "))
    print("El valor de " + str(base) + " elevado a " + str(exponente) + " es: " + str(PotenciaCalculo(base, exponente)))

def PotenciaCalculo(base, exponente):
    if exponente <= 0:
        return 1
    else:
        return base * PotenciaCalculo(base,exponente-1)

def Calculadora():
    fin = False

    while not(fin):
        print("============= Menu Calculadora =============")
        print()
        print("1. Sumar")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Factorial")
        print("6. Potencia")
        print("7. Salir")
        print()
        print()
        opc = int(input("Seleccione la operacion:"))
        if (opc == 1):
            sumar()
        elif (opc == 2):
            restar()
        elif (opc == 3):
            multiplicar()
        elif (opc == 4):
            dividir()
        elif (opc == 5):
            Factorial()
        elif (opc == 6):
            potencia()
        elif (opc == 7):
            fin = 1
            print("Gracias por utilizar el programa!!")

Calculadora()