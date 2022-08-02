#Autor: John Burgos
#Fecha: 2022/01/10
#Descripción: Programa creado para aprender condicional IF
print()
print("+----- CONDICIONAL IF -----+")
print()

def calificacion(nota):
    valoracion="Aprobado"
    if nota <= 5:
        valoracion="No Aprobado"
    return valoracion

nota_alumno=int(input("Digite la nota alumno: "))
print(calificacion(nota_alumno))