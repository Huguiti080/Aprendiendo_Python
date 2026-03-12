from datetime import datetime, timedelta
from excepciones import FechaInvalidaError, FrecuenciaInvalidaError

# Diccionario para meses en español
MESES_ESP = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}

# Diccionario para días de la semana en español
DIAS_ESP = {
    0: 'lunes', 1: 'martes', 2: 'miércoles', 3: 'jueves',
    4: 'viernes', 5: 'sábado', 6: 'domingo'
}

class Evento:
    def __init__(self, nombre, descripcion, fecha_str):
        self.nombre = nombre
        self.descripcion = descripcion
        try:
            self.__fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        except ValueError:
            raise FechaInvalidaError(f"La fecha '{fecha_str}' no es válida. Formato esperado: YYYY-MM-DD HH:MM")

    @property
    def fecha(self):
        return self.__fecha
        
    def tiempo_restante(self):
        return self.__fecha - datetime.now()

    def fecha_formateada(self):
        dia_semana = DIAS_ESP[self.__fecha.weekday()]
        mes = MESES_ESP[self.__fecha.month]
        return f"{dia_semana.capitalize()} {self.__fecha.day} de {mes} de {self.__fecha.year} a las {self.__fecha.strftime('%H:%M')}"

    def ya_ocurrio(self):
        return self.__fecha < datetime.now()

    def __str__(self):
        estado = "(ya ocurrió)" if self.ya_ocurrio() else "(próximo)"
        return f"{self.nombre} - {self.fecha_formateada()} {estado}\n   Descripción: {self.descripcion}"

    def __repr__(self):
        return self.__str__()


class EventoRecurrente(Evento):
    def __init__(self, nombre, descripcion, fecha_str, frecuencia):
        super().__init__(nombre, descripcion, fecha_str)
        if frecuencia not in ("semanal", "mensual"):
            raise FrecuenciaInvalidaError(f"La frecuencia '{frecuencia}' no es válida. Use 'semanal' o 'mensual'.")
        self.frecuencia = frecuencia

    def proxima_ocurrencia(self):
        if self.frecuencia == "semanal":
            return self.fecha + timedelta(weeks=1)
        elif self.frecuencia == "mensual":
            return self.fecha + timedelta(days=30)