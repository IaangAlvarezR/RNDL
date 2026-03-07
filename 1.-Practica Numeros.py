#Práctica Números 
#Objetivo 
#Complementar el "Diario de un Astronauta" agregando una cabecera. Aprender a manejar variables en Python, utilizando tipos de datos básicos como números y cadenas de texto (strings). 
#Instrucciones: 
#Crea una variable llamada nombre_astronauta y asígnale tu nombre como un string. 
#Crea una variable edad_astronauta y asígnale tu edad como un número. 
#Crea una variable destino y asígnale el nombre de un planeta como string (por ejemplo, "Marte"). 
#Imprime un mensaje de introducción utilizando estas variables, que diga: "Hola, soy [nombre_astronauta], tengo [edad_astronauta] años y mi próximo destino es [destino]." 
#Crea dos variables, combustible y velocidad, asignándoles valores numéricos. 
#Imprime un mensaje que diga: "Estoy navegando a [velocidad] km/s con [combustible]% de combustible restante hacia [destino]." 
#Explora el concepto de f-string para insertar las variables en las cadenas de texto y mostrarlas por pantalla utilizando print. 
#Al usar f-strings, debes colocar el nombre de la variable entre {} dentro del string. Por ejemplo: print(f"Texto {variable}").  
#
#Resultado esperado:
#Diario de un Astronauta 
#Hola, soy Max, tengo 25 años y mi próximo destino es Marte. 
#Estoy navegando a 27000 km/s con 85% de combustible restante hacia Marte. 
#Fecha: 2026-01-10 
#Hoy experimentamos con el cultivo de plantas en microgravedad. 
#Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba! 
#Fecha: 2026-01-11 
#Realizamos una caminata espacial para reparar un panel solar. 
#Mensaje personal: Flotar en el espacio nunca deja de asombrarme. 
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

nombre_astronauta = "Iaan" 
edad_astronauta = 26 
destino = "Marte"
introduccion = f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}."
titulo = "Diario de un Astronauta"

print(titulo)
print(introduccion)

mensaje_navegacion = f"Estoy navegando a 27000 km/s con 85% de combustible restante hacia {destino}."
print(mensaje_navegacion)

fecha_1 = "2026-01-10"
actividad_1 = "Hoy experimentamos con el cultivo de plantas en microgravedad."
mensaje_personal_1 = "¡Es increíble ver cómo crecen las lechugas aquí arriba!"
print(f"Fecha: {fecha_1}")
print(actividad_1)  
print(f"Mensaje personal: {mensaje_personal_1}")

fecha_2 = "2026-01-11"
actividad_2 = "Realizamos una caminata espacial para reparar un panel solar."
mensaje_personal_2 = "Flotar en el espacio nunca deja de asombrarme."
print(f"Fecha: {fecha_2}")
print(actividad_2)
print(f"Mensaje personal: {mensaje_personal_2}")

