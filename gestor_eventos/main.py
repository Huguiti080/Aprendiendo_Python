from evento import Evento, EventoRecurrente
from calendario import Calendario
from excepciones import FechaInvalidaError, FrecuenciaInvalidaError, EventoDuplicadoError

# 1. Crear eventos
e1 = Evento("Reunión", "Junta de equipo", "2026-06-15 10:00")
e2 = Evento("Cumpleaños", "Fiesta sorpresa", "2026-03-12 18:00")  # ← en 24h
e3 = EventoRecurrente("Gym", "Entrenamiento semanal", "2026-01-01 07:00", "semanal")

# 2. Crear calendario y agregar eventos
cal = Calendario()
cal.agregar_evento(e1)
cal.agregar_evento(e2)
cal.agregar_evento(e3)

# 3. Probar métodos
cal.listar_todos()
print("\n---------Eventos futuros:---------")
for e in cal.eventos_futuros():
    print(e)
    print("-" * 50)
print("\n---------Eventos en próximas 24h:---------")
for e in cal.proximas_24h():
    print(e)
    print("-" * 50)

# 4. Probar excepción
try:
    e_malo = Evento("Error", "Fecha rota", "no-es-una-fecha")
except FechaInvalidaError as e:
    print(f"Error capturado: {e}")