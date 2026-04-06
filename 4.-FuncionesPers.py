#Práctica de funciones personalizadas.
#
#Objetivo
#Crear un "Generador de Distancia de Planetas" utilizando funciones personalizadas en Python, aprovechando los conocimientos previos de strings.
#
#Instrucciones
#•	Escribe un programa en Python que incluya una función personalizada para generar la distancia a un planeta.
#•	La función debe recibir como argumento un string que proporcionará el nombre del planeta y un número entero que será la distancia en millones de km a dicho planeta.
#•	Tras definir la función, esta imprimirá por pantalla el nombre del planeta y la distancia al mismo.
#
#Resultado esperado
#Nombre del planeta: Marte
#Distancia al planeta: 225 millones de km

#se añade separacion y nombre de archivo
print()
print("4.-FuncionesPersonalizadas.py")

def generar_distancia_planeta(nombre_planeta, distancia_millones_km):
    """Genera la distancia a un planeta dado su nombre y distancia en millones de km."""
    
    print(f"Nombre del planeta: {nombre_planeta}")
    print(f"Distancia al planeta: {distancia_millones_km} millones de km")
    
generar_distancia_planeta("Marte", 225)