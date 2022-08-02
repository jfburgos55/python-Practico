## Autor: Erika Burgos - Universidad Nacional
# Fecha: 07 Mayo del 2022
# Descripcion: Programa que genera un bingo

def bingo(jugador1, jugador2, moderador):

    tablero=""
    contadorJugador1=0
    contadorJugador2=0

    for x in moderador:

        for j1 in jugador1:
            if j1 == x:
                contadorJugador1 += 1

        for j2 in jugador2:
            if j2 == x:
                contadorJugador2 += 1

        if contadorJugador1 > contadorJugador2:
            tablero = tablero + "V"

        if contadorJugador2 > contadorJugador1:
            tablero = tablero + "F"

        if contadorJugador2 == contadorJugador1:
            tablero = tablero + "≈"
    return tablero
#jugador1=input("+XMY*|")
#jugador2=input("+XWY.-")
#moderador=input("WWX.-.+M-M||+..+XM|XM")
jugador1=input("")
jugador2=input("")
moderador=input("")
imprimirTablero=bingo(jugador1, jugador2, moderador)
#imprimirTablero=bingo("+XMY*|", "+XWY.-", "WWX.-.+M-M||+..+XM|XM")
print(imprimirTablero)