#====================================
#PROGRAMA: Calculadora de Perfil Personal
# TEMA: Variables y tipos de datos
# FECHA: 28/01/2026
#====================================

print ("===BIENVENIDO A TU PERFIL PERSONAL===\n")

#STRING (Texto)
nombre = input("¿Cual es tu nombre?")
ciudad = input ("¿En que ciudad vives? ")

#INTEGER (Números enteros)
edad = int(input("¿Cuantos años tienes? "))
año_actual = 2026

#FLOAT (Números decimales)
estatura = float(input("¿Cual es tu estatura en metros? Ejemplo: 1.75 "))
peso = float(input("¿Cual es tu peso en kilogramos? Ejemplo: 70.5 "))   

#BOOLEAN (Verdadero o Falso)
estudia = input("¿Estas estudiando actualmente? (si/no) ")
es_estudiante = estudia.lower() == "si"


#====================================
#CÁLCULOS
#====================================

año_nacimiento = año_actual - edad
imc = peso / (estatura ** 2)
altura_cm = estatura * 100

#====================================
#SALIDA DE DATOS
#====================================
print ("\n" + "="*40)
print ("\n===TU PERFIL PERSONAL===")
print ("="*40)


print (f"Nombre:", nombre)
print (f"Ciudad:", ciudad)
print (f"Año de Nacimiento:", año_nacimiento)
print (f"Edad:", edad, "años")
print (f"Estatura:", estatura, "metros (", altura_cm, "cm )")
print (f"¿Estudiante?:", es_estudiante)

print (f"\n Tipo de dato de cada variable:")
print (f"Nombre:", type(nombre))
print (f"Ciudad:", type(ciudad))
print (f"Edad:", type(edad))
print (f"Estatura:", type(estatura))
print (f"Peso:", type(peso))
print (f"¿Estudiante?:", type(es_estudiante))