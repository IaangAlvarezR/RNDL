
#Valor por defecto a nombre
nombre = "Iaan"

#Se comenta para evitar que el programa se detenga esperando input y falle en workflow de github
#nombre = input("Ingrese su nombre: ")  #ingresar nombre por teclado


def cabecera():
    print()
    print("10.-Calculadora-Calorias.py")
    print(" ============================================= ")
    print("CALCULADORA DE FITNESS Y SALUD PERSONAL")
    print(" Bienvenido a tu asistente de salud personal, " + nombre + "!")
    print(" ============================================= ")

cabecera()

def calcular_imc(peso_kg, altura_m): 
    """ 
    Calcula el Índice de Masa Corporal (IMC). 
    Fórmula: IMC = peso / (altura^2) 
    Parámetros: 
    peso_kg (float): Peso en kilogramos 
    altura_m (float): Altura en metros 
    Retorna: 
    float: El IMC calculado 
    """ 
    imc = peso_kg / (altura_m ** 2) 
    return imc 

def es_peso_saludable(imc): 
    """ 
    Determina si el IMC está en rango saludable (18.5 - 24.9). 
    Parámetro: 
    imc (float): Índice de Masa Corporal 
    Retorna: 
    bool: True si está en rango saludable, False si no 
    """ 
    # Operadores de comparación y lógicos 
    return imc >= 18.5 and imc <= 24.9 

def tiene_sobrepeso(imc): 
    """ 
    Determina si hay sobrepeso (IMC >= 25). 
    """ 
    return imc >= 25

def tiene_bajo_peso(imc): 
    """ 
    Determina si hay bajo peso (IMC < 18.5). 
    """ 
    return imc < 18.5


def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre): 
    """ 
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.      
    Parámetros: 
    peso_kg (float): Peso en kg 
    altura_cm (float): Altura en cm 
    edad (int): Edad en años 
    es_hombre (bool): True si es hombre, False si es mujer 
    Retorna: 
    float: Calorías diarias recomendadas 
    """ 
    # Operadores aritméticos y booleanos 
    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad) 
    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad) 
    # Usa el hecho de que True=1 y False=0 
    #codigo sin if-else
    calorias = (88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)) * es_hombre + (447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)) * (not es_hombre)
    #Si es_hombre es True (1), se calcula la formula para hombres y se suma 0 (formula para mujeres no se aplica). 
    #Si es_hombre es False (0), se suma 0 (formula para hombres no se aplica) y se calcula la formula para mujeres.
    return calorias


def calcular_agua_diaria(peso_kg): 
    """ 
    Calcula litros de agua recomendados al día (35ml por kg de peso). 
    """ 
    # TU CÓDIGO AQUÍ
    ml_agua = peso_kg * 35
    litros_agua = ml_agua / 1000
    return litros_agua 

def calcular_ritmo_cardiaco_maximo(edad): 
    """ 
    Calcula el ritmo cardíaco máximo (220 - edad). 
    """ 

    # TU CÓDIGO AQUÍ 
    return 220 - edad


print("Ejemplo de uso:")
peso = 60  # kg
altura = 1.80  # m
edad = 26  # años
es_hombre = True


imc = calcular_imc(peso, altura)

print(f"IMC: {imc:.2f}")
print(f"¿Peso saludable? {es_peso_saludable(imc)}")
print(f"¿Tiene sobrepeso? {tiene_sobrepeso(imc)}")
print(f"¿Tiene bajo peso? {tiene_bajo_peso(imc)}")

calorias = calcular_calorias_diarias(peso, altura * 100, edad, es_hombre)
print(f"Calorías diarias recomendadas: {calorias:.2f}")

agua = calcular_agua_diaria(peso)
print(f"Agua diaria recomendada: {agua:.2f} litros")

ritmo_max = calcular_ritmo_cardiaco_maximo(edad)
print(f"Ritmo cardíaco máximo recomendado: {ritmo_max} ppm")        