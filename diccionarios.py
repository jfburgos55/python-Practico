#Autor: John Burgos
#Fecha: 2022/02/08
#Descripción: Programa creado para aprender diccionarios
print("\n+---------- Diccionario ----------+")
diasSemanaIngles={
    "Lunes":    "Monday",
    "Martes":   "Tuesday",
    "Miercoles":"Wednesday",
    "Jueves":   "Thursday",
    "Viernes":  "Friday"
}
print("Lunes en ingles: ",diasSemanaIngles["Lunes"])
print("Miercoles en ingles: ",diasSemanaIngles["Miercoles"])
print("Viernes en ingles: ",diasSemanaIngles["Viernes"])
#Agregar elementos al diccionario
diasSemanaIngles["Sabado"] = "Saturday"
print(diasSemanaIngles)
#eliminar elementos
del diasSemanaIngles["Lunes"]
print(diasSemanaIngles)
#Numero de elementos, maximo, minimo
print("Números de elementos del diccionario: ", len(diasSemanaIngles))
print("Elemento mayor del diccionario: ",max(diasSemanaIngles))
print("Elemento menor del diccionario: ",min(diasSemanaIngles))