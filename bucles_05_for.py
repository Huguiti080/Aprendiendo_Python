#Calculado de Promedio de Calificaciones

print("---------------------------------------")
print("Calculadora de Promedio de Calificaciones")
print("---------------------------------------")

#Solicitar al usuario el número de calificaciones
#Usamos int por que necesitamos un número entero
num_calificaciones = int(input("Ingrese el número de calificaciones a promediar: "))

#Variable acumuladora para la suma de calificaciones (ira sumando todas las calificaciones
#comienza en 0)
suma_calificaciones = 0

#Bucle for para ingresar cada calificación
for i in range(num_calificaciones): #repite el codifo un numero especificio de veces
    calificacion = float(input(f"Ingrese la calificación #{i + 1}: "))
    suma_calificaciones += calificacion #Sumar la calificación a la suma total

#Calcular el promedio}
promedio = suma_calificaciones / num_calificaciones # Dividimos la suma total entre el número de calificaciones

#Mostrar el resultado
print(f"El promedio de las calificaciones es: {promedio:.2f}")

#validacion si aprobo o no
if promedio >= 6.0:
    print("¡Felicidades! Has aprobado.")    
else:
    print("Lo siento, no has aprobado.")

#========================================================================================
print("=====TABLA DE MULTIPLICAR=====")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
limite = int(input("¿Hasta qué número quieres que aparezcan las multiplicaciones?: "))

print(f"-----TABLA DEL {numero} (del 1 al {limite})-----")

for i in range(1, limite + 1):
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")

