#Instrucciones
#1.	Escribe un programa en Python que contenga una función llamada calcular_calorias. Esta función debe tomar tres argumentos: carbohidratos (cantidad en gramos), proteínas (cantidad en gramos) y grasas (cantidad en gramos).
#2.	Dentro de la función, utiliza operadores aritméticos para calcular las calorías totales, considerando que cada gramo de carbohidratos y proteínas aporta 4 calorías y cada gramo de grasas aporta 9 calorías.
#3.	La función debe devolver el total de calorías calculado.
#4.	Después de definir la función, realiza llamadas a calcular_calorias con diferentes cantidades de macronutrientes y muestra los resultados. 
#5.	Como ejemplo se propone calcular las calorías de una comida con 10 gr de carbohidratos, 40 gr de proteínas y 5 gr de grasa.
#
#Resultado esperado
#Calorías totales: 245

#se añade separacion y nombre de archivo
print()
print("7.-Operadores-Aritmeticos.py")

def calcular_calorias(carbohidratos, proteinas, grasas):
    #docstring
    """Calcula las calorías totales a partir de la cantidad de carbohidratos, proteínas y grasas."""
    calorias_carbohidratos = carbohidratos * 4
    calorias_proteinas = proteinas * 4
    calorias_grasas = grasas * 9
    calorias_totales = calorias_carbohidratos + calorias_proteinas + calorias_grasas
    return calorias_totales

carbohidratos = 10
proteinas = 40
grasas = 5
calorias = calcular_calorias(carbohidratos, proteinas, grasas)
print(f"Calorías totales: {calorias}")