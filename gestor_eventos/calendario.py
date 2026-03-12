from datetime import datetime, timedelta
from excepciones import EventoNoEncontradoError, EventoDuplicadoError, CalendarioVacioError

class Calendario:
    def __init__(self):
        self.__eventos = []

    @property
    def eventos(self):
        return self.__eventos

    def agregar_evento(self, evento):
        # Verificar si el evento ya existe (mismo nombre y fecha)
        for e in self.__eventos:
            if e.nombre == evento.nombre and e.fecha == evento.fecha:
                raise EventoDuplicadoError(f"El evento '{evento.nombre}' ya existe en esta fecha.")
        self.__eventos.append(evento)

    def eliminar_evento(self, nombre):
        for i, e in enumerate(self.__eventos):
            if e.nombre == nombre:
                return self.__eventos.pop(i)
        raise EventoNoEncontradoError(f"No se encontró el evento '{nombre}'.")

    def buscar_evento(self, nombre):
        for e in self.__eventos:
            if e.nombre == nombre:
                return e
        raise EventoNoEncontradoError(f"No se encontró el evento '{nombre}'.")

    def eventos_futuros(self):
        ahora = datetime.now()
        return [e for e in self.__eventos if e.fecha > ahora]

    def proximas_24h(self):
        ahora = datetime.now()
        limite = ahora + timedelta(hours=24)
        return [e for e in self.__eventos if ahora < e.fecha <= limite]

    def listar_todos(self):
        if not self.__eventos:
            print("No hay eventos en el calendario.")
            return
        print("=" * 50)
        print("LISTADO DE EVENTOS")
        print("=" * 50)
        for e in self.__eventos:
            print(e)
            print("-" * 50)

    def eventos_pasados(self):
        ahora = datetime.now()
        return [e for e in self.__eventos if e.fecha <= ahora]