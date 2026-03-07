#Práctica Introducción a las funciones
#
#Objetivo
#Crear un "Analizador de Títulos de Libros" utilizando la función len() en Python.
#
#Instrucciones
#•	Escribe un programa en Python que analice la longitud de los títulos de varios libros utilizando la función len()
#•	El programa tendrá predefinidos varios títulos de libros como strings.
#•	Usa la función len() para calcular la longitud de cada título (número de caracteres, incluyendo espacios).
#•	Después de calcular la longitud de cada título, usa print para mostrar el título del libro y su respectiva longitud. Recuerda que puedes hacer uso del concepto de f-string que exploramos en ejercicios anteriores.
#
#Resultado esperado
#La longitud del título del libro 1 es: 20
#La longitud del título del libro 2 es: 23
#La longitud del título del libro 3 es: 24 


libro_20Caracteres = "El Principito(Nuevo)"
libro_23Caracteres = "Cien100 Años de Soledad"
libro_24Caracteres = "Don Quijote de la Mancha"

longitud_libro_20 = len(libro_20Caracteres)
longitud_libro_23 = len(libro_23Caracteres)
longitud_libro_24 = len(libro_24Caracteres)

print(f"La longitud del título {libro_20Caracteres} es: {longitud_libro_20}")
print(f"La longitud del título {libro_23Caracteres} es: {longitud_libro_23}")
print(f"La longitud del título {libro_24Caracteres} es: {longitud_libro_24}")
