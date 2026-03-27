# Estructura
{clave: valor for elemento in iterable if condición}

# Ejemplo
cuadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Estructura
[expresión for lista in matriz for elemento in lista]

# Ejemplo — "aplanar" una matriz
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6]

# Ejemplo — contar la frecuencia de palabras en un texto
texto = "hola mundo hola python"
frecuencia = {palabra: texto.split().count(palabra) for palabra in set(texto.split())}
# {'hola': 2, 'mundo': 1, 'python': 1}

print(frecuencia)

precios = {"manzana": 20, "laptop": 15000, "libro": 80, "cafe": 35, "auriculares": 650}
precios_descuento = {item: precio * 0.9 for item, precio in precios.items() if precio > 100}
print(precios_descuento)

#invertir un diccionario dado un diccionario, crear un nuevo diccionario donde 
# las claves sean los valores originales y los valores sean las claves originales.
diccionario_original = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = {valor: clave for clave, valor in diccionario_original.items()}
print(diccionario_invertido)

# Reto 5 — Tabla de multiplicar
# Genera una tabla de multiplicar del 1 al 5 como lista de listas, donde cada lista interior representa una fila.
tabla_multiplicar = [[f"{i} x {j} = {i*j}" for j in range(1, 6)] for i in range(1, 6)]
for fila in tabla_multiplicar:
    print(fila)


#Tienes una lista de estudiantes, 
# cada uno con su nombre y sus calificaciones.
#  Crea un diccionario donde la clave sea el nombre del estudiante 
# y el valor sea su promedio, pero solo incluye a los que tienen promedio mayor o igual a 7.0.

estudiantes = [
    {"nombre": "Alice", "calificaciones": [8, 9, 7]},
    {"nombre": "Bob", "calificaciones": [6, 5, 7]},
    {"nombre": "Charlie", "calificaciones": [9, 10, 8]},
    {"nombre": "David", "calificaciones": [4, 6, 5]},
]

promedios = {estudiante["nombre"]: sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"]) for estudiante in estudiantes if sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"]) >= 7.0}
print(promedios)