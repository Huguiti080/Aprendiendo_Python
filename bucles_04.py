import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import random

#
# Juego: Adivina el número
#  Bucle while principal: Controla las partidas del juego (permite jugar múltiples veces)
#Bucle while not: Maneja los intentos hasta adivinar el número correcto
#Bucle de validación: Asegura que el usuario ingrese respuestas válidas ("si" o "no")
#Contadores: Variable intentos que se incrementa en cada iteración del bucle
#Condiciones de salida: Cambio de variables booleanas para terminar bucles
#continue: Palabra clave para saltar a la siguiente iteración cuando el input es inválido

print("=" * 50)
print(" BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO ")
print("=" * 50)

jugar_de_nuevo = "si"

# BUCLE PRINCIPAL: Se repite mientras el usuario quiera seguir jugando
# Este while controla todo el flujo del juego
while jugar_de_nuevo == "si":
    numero_secreto = random.randint(1, 50)
    intentos = 0
    adivinado = False
    
    print("\nHe pensado en un número entre 1 y 50")
    print("¡Intenta adivinarlo!")
    
    # BUCLE DE JUEGO: Se ejecuta hasta que adivinado sea True
    # La condición "not adivinado" significa "mientras NO haya adivinado"
    # Este bucle terminará cuando el usuario acierte el número
    while not adivinado:
        try:
            intento = int(input("\nIngresa tu número: "))


            if intento < 1 or intento > 50:
                print(" Por favor ingresa un número entre 1 y 50")
                continue  # Vuelve al inicio del bucle sin contar este intento

            intentos += 1  # Incrementamos el contador en cada vuelta del bucle
            
            if intento == numero_secreto:
                # Al cambiar adivinado a True, el bucle while terminará
                adivinado = True
                print(f"\n ¡FELICIDADES! Adivinaste en {intentos} intentos")
                
                if intentos <= 3:
                    print("¡Eres un genio! ")
                elif intentos <= 6:
                    print("¡Muy bien! ")
                else:
                    print("¡Lo lograste! ")
                    
            elif intento < numero_secreto:
                # El bucle continúa porque adivinado sigue siendo False
                print(" El número es MAYOR. Intenta de nuevo.")
            else:
                print(" El número es MENOR. Intenta de nuevo.")

        except ValueError:
            print(" Por favor ingresa solo números")
  
    
    print("\n" + "-" * 50)
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    
    # BUCLE DE VALIDACIÓN: Se repite mientras la respuesta sea inválida
    # Este bucle asegura que solo se acepten "si" o "no"
    while jugar_de_nuevo != "si" and jugar_de_nuevo != "no":
        print("Por favor responde solo 'si' o 'no'")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    # Cuando el usuario escribe "si" o "no", este bucle termina
    # y volvemos al BUCLE PRINCIPAL

print("\n ¡Gracias por jugar! Hasta pronto")