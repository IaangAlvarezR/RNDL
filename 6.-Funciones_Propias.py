#Práctica Funciones propias de Python
#
#Objetivo
#Combinar el aprendizaje de funciones básicas de Python como print, len, str, int, float, y type con la creación de funciones personalizadas para profundizar en la comprensión y manipulación de tipos de datos básicos.
#
#Instrucciones
#1.	Función para contar caracteres en una cadena:
#•	Define una función llamada contar_caracteres que reciba un string como argumento.
#•	Dentro de la función, usa len para determinar la longitud de la cadena.
#•	Haz que la función imprima la cadena original y su longitud en el siguiente formato: La frase 'Aprender Python es divertido' tiene 28 caracteres.
#•	Llama a esta función con una frase de tu elección.
#2.	Función para convertir y mostrar tipos de números:
#•	Crea una función convertir_numero que tome un número entero como argumento.
#•	Dentro de la función, convierte el número a cadena usando str y a flotante usando float.
#•	Imprime el número en sus tres formas (entero, cadena y flotante) junto con su tipo de dato (usando type) en el siguiente formato:
#1.	Entero: 42, Tipo: <class 'int'>
#2.	Cadena: 42, Tipo: <class 'str'>
#3.	Flotante: 42.0, Tipo: <class 'float'>
#•	Llama a esta función con un número entero de tu elección.
#
#Resultado esperado
#La frase 'Aprender Python es divertido' tiene 28 caracteres.
#Entero: 42, Tipo: <class 'int'>
#Cadena: 42, Tipo: <class 'str'>
#Flotante: 42.0, Tipo: <class 'float'>

def contar_caracteres(frase):
    """Cuenta los caracteres de una frase y muestra la frase junto con su longitud."""
    
    longitud = len(frase)
    print(f"La frase '{frase}' tiene {longitud} caracteres.")

def convertir_numero(numero):
    """Convierte un número entero a cadena y flotante, y muestra sus tipos de dato."""
    
    numero_cadena = str(numero)
    numero_flotante = float(numero)
    
    print(f"1. Entero: {numero}, Tipo: {type(numero)}")
    print(f"2. Cadena: {numero_cadena}, Tipo: {type(numero_cadena)}")
    print(f"3. Flotante: {numero_flotante}, Tipo: {type(numero_flotante)}")

# Pruebas
contar_caracteres("Aprender Python es divertido")
print()
convertir_numero(42)

