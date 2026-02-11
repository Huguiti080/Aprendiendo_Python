#======================
#Programa de practica: Funciones en python
# SISTEMA DE GESTION DE ESTUDIANTES
#=========================

#Variables globales (SCOPE)
nombre_escuela= "Academia Python"

# FUNCION SIN PARAMETROS Y SIN RETURN
def mostrar_bienvenida():
    "HOLA BIENVENIDOS A ACADEMIA PYTHON"
    print("="*50)
    print(f"Bienvenido al {nombre_escuela}")
    print ("Sistema de Gestion de Estudiantes")
    print ("="*50 )

#FUNCION CON PARAMETROS Y SIN RETURN
def mostrar_estudiante(nombre, edad, carrera):
    """ MUESTRA LOS DATOS DEL ESTUDIANTE"""
    print("-"*50)
    print("Datos del Estudiante:")
    print(f"Estudiante: {nombre}, Edad: {edad}, Carrera: {carrera}")

#FUNCION CON PARAMETROS Y CON RETURN
def calcular_promedio(nota1, nota2, nota3):
    """ CALCULA EL PROMEDIO DE LAS NOTAS"""
    promedio = [nota1, nota2, nota3]
    if len(promedio) == 0:
        return 0
    promedio = sum(promedio) / len(promedio)
    return promedio

#FUNCION CON PARAMETROS POR DEFECTO Y CON RETURN
def registrar_estudiante(nombre, edad, carrera="Sin Carrera"):
    """ REGISTRA UN ESTUDIANTE CON CARRERA POR DEFECTO"""
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    return estudiante

#FUNCION QUE RETORNA MULTIPLES VALORES
def analizar_promedio (promedio):
    """ ANALIZA LAS CALIFICACIONES Y RETORNA ESTADO Y MENSAJE"""
    if promedio >= 90:
        estado = "Excelente"
        mensaje = "¡Excelente trabajo! Has obtenido una calificación sobresaliente."
    elif promedio >= 70:
        estado = "Aprobado"
        mensaje = "¡Felicidades! Has aprobado."
    elif promedio >= 60:
        estado = "Regular"
        mensaje = "Has aprobado, pero hay áreas de mejora."
    else:
        estado = "Reprobado"
        mensaje = "Lo siento, no has aprobado."
    return estado, mensaje


#FUNCION CON QUE LLAMA A OTRAS FUNCIONES
def proceso_estudiante(nombre, edad, carrera, nota1, nota2, nota3):
    """ PROCESA LOS DATOS DEL ESTUDIANTE Y MUESTRA RESULTADOS"""
    mostrar_estudiante(nombre, edad, carrera)
    promedio = calcular_promedio(nota1, nota2, nota3)
    print(f"Promedio: {promedio:.2f}")
    estado, mensaje = analizar_promedio(promedio)
    print(f"Estado: {estado}")
    print(f"Mensaje: {mensaje}")

#FUNCION CON SCOPE LOCAL + GLOBAL
def modificar_escuela(nuevo_nombre):
    """ MODIFICA EL NOMBRE DE LA ESCUELA (SCOPE GLOBAL)"""
    global nombre_escuela # Indica que se va a modificar la variable global
    nombre_anterior = nombre_escuela
    nombre_escuela = nuevo_nombre
    print(f"El nombre de la escuela ha sido modificado de '{nombre_anterior}' a '{nombre_escuela}'")
   
#FUNCION CON SCOPE LOCAL
def materias_alumno( materias):
    """ MUESTRA LAS MATERIAS DEL ALUMNO (SCOPE LOCAL)"""
    print("Materias del Alumno:")
    for materia in materias:
        print(f"- {materia}")

#FUNCION QUE RETORNA BOOLEANO
"""Verifica si el estudiante es mayor de edad"""
def es_mayor_edad(edad):
    return edad >= 18


def main():

    """FUNCION PRINCIPAL PARA EJECUTAR EL PROGRAMA"""
    mostrar_bienvenida()

    print("\n" + "="*50 + "\n")
    print("EJEMPLO DE USO DE FUNCIONES")
    print("\n" + "="*50 + "\n")

    # Ejemplo 1 funcion sin return
    print("1. Funcion sin parametros y sin return")
    mostrar_bienvenida()

    # Ejemplo 2 funcion con parametros y sin return
    print("\n2. Funcion con parametros y sin return")
    mostrar_estudiante("Maria Lopez", 22, "Ingenieria de Software")

    # Ejemplo 3 funcion con parametros y con return
    print("\n3. Funcion con parametros y con return")
    promedio = calcular_promedio(85, 90, 78)
    print(f"Promedio calculado: {promedio:.2f}")

    # Ejemplo 4 funcion con parametros por defecto y con return
    print("\n4. Funcion con parametros por defecto y con return")
    estudiante1 = registrar_estudiante("Carlos Perez", 19)
    estudiante2 = registrar_estudiante("Ana Gomez", 21, "Medicina")

    print(f"Estudiante registrado: {estudiante1}")
    print(f"Estudiante registrado: {estudiante2}")

    # Ejemplo 5 funcion que retorna multiples valores
    print ("\n5. Funcion con multiples valores")
    estado, mensaje = analizar_promedio(promedio)
    print(f"Estado del estudiante: {estado}, Mensaje: {mensaje}")

    # Ejemplo 6 funcion que llama a otras funciones
    print("\n6. Funcion que llama a otras funciones")
    proceso_estudiante("Luis Martinez", 20, "Derecho", 88, 92, 80)

    # Ejemplo 7 funcion con scope local + global
    print("\n7. Funcion con scope local + global")
    print(f"Nombre de la escuela antes de modificar: {nombre_escuela}")
    modificar_escuela("Instituto Python")   
    print(f"Nombre de la escuela despues de modificar: {nombre_escuela}")

    # Ejemplo 8 funcion con scope local
    print("\n8. Funcion con scope local")
    materias = ["Matematicas", "Programacion", "Fisica"]
    materias_alumno(materias)

    # Ejemplo 9 funcion que retorna booleano
    print("\n9. Funcion que retorna booleano")
    edad_estudiante = 17
    if es_mayor_edad(edad_estudiante):
        print("El estudiante es mayor de edad.")
    else:
        print("El estudiante es menor de edad.")


if __name__ == "__main__":
    main()

