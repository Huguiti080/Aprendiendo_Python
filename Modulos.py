import math
import random
import datetime

# 1. Calcular distancia entre dos puntos (ciudades)
def calcular_distancia(x1, y1, x2, y2):
    # Tu código aquí
    distancia = math.hypot(x2 - x1, y2 - y1)
    return distancia

# 2. Sugerir actividad aleatoria
def sugerir_actividad():
    actividades = ["Visitar un museo", "Ir al cine", "Practicar deporte", "Leer un libro", "Cocinar algo nuevo"]  # Llena esta lista con al menos 5 actividades
    # Tu código aquí
    return random.choice(actividades)

# 3. Mostrar fecha/hora y decir si es día o noche
def info_tiempo():
    # Tu código aquí
    ahora = datetime.datetime.now()
    hora = ahora.hour
    if 6 <= hora < 18:
        periodo = "Buen día"
    else:
        periodo = "Buenas noches"
    return ahora, periodo

# --- Programa principal ---
print("️ Bienvenido al Asistente de Viajes\n")

# Ejemplo de uso:
distancia = calcular_distancia(0, 0, 3, 4)
print(f"Distancia entre las ciudades: {distancia:.2f} unidades")

actividad = sugerir_actividad()
print(f"Actividad sugerida: {actividad}")

fecha_hora, periodo = info_tiempo()
print(f"Fecha y hora actual: {fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}, es {periodo}.")





