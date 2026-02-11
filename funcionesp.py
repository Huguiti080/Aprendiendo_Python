# ============================================
# EJERCICIOS PRACTICA
# ============================================

# EJERCICIO 1: Sumar dos números
def sumar_dos_numeros(num1, num2):
    """Suma dos números y retorna el resultado"""
    return num1 + num2


# EJERCICIO 2: Verificar si es par
def es_par(numero):
    """Retorna True si el número es par, False si es impar"""
    return numero % 2 == 0  


# EJERCICIO 3: Saludar persona
def saludar_persona(nombre, hora_dia):
    """Muestra un saludo apropiado según la hora del día"""
    if hora_dia == "mañana":
        print(f"Buenos días, {nombre}!")
    elif hora_dia == "tarde":
        print(f"Buenas tardes, {nombre}!")
    elif hora_dia == "noche":
        print(f"Buenas noches, {nombre}!")
    else:
        print(f"Hola, {nombre}! (hora no reconocida)")


# EJERCICIO 4: Calcular área de rectángulo
def calcular_area_rectangulo(base, altura):
    """Calcula y retorna el área de un rectángulo"""
    return base * altura  #  Más simple, directamente retornas


# ============================================
# MENÚ PRINCIPAL
# ============================================

def menu_principal():
    """Menú interactivo para probar las funciones"""
    print("\n" + "="*50)
    print("PROGRAMA DE PRÁCTICA - FUNCIONES EN PYTHON")
    print("="*50)
    print("\nSelecciona una opción:")
    print("1. Sumar dos números")
    print("2. Verificar si un número es par")
    print("3. Saludar a una persona")
    print("4. Calcular el área de un rectángulo")
    print("5. Salir")
    
    opcion = input("\nIngrese el número de la opción deseada: ")

    if opcion == "1":
        print("\n--- SUMA DE DOS NÚMEROS ---")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar_dos_numeros(num1, num2)
        print(f" La suma de {num1} y {num2} es: {resultado}")
        
    elif opcion == "2":
        print("\n--- VERIFICAR NÚMERO PAR ---")
        numero = int(input("Ingrese un número: "))
        if es_par(numero):
            print(f" {numero} es un número par")
        else:
            print(f" {numero} es un número impar")
            
    elif opcion == "3":
        print("\n--- SALUDAR PERSONA ---")
        nombre = input("Ingrese el nombre: ")
        hora_dia = input("Ingrese la hora (mañana/tarde/noche): ").lower()
        saludar_persona(nombre, hora_dia)
        
    elif opcion == "4":
        print("\n--- ÁREA DE RECTÁNGULO ---")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = calcular_area_rectangulo(base, altura)
        print(f" El área del rectángulo es: {area}")
        
    elif opcion == "5":
        print("\n¡Hasta pronto! ")
        return False  # Para salir del bucle
        
    else:
        print("\n Opción no válida. Seleccione del 1 al 5")
    
    return True  # Continuar el bucle


# ============================================
# EJECUTAR PROGRAMA CON BUCLE
# ============================================

if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = menu_principal()
        if continuar:
            input("\nPresiona ENTER para volver al menú...")