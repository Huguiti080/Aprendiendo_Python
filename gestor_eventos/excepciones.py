class FechaInvalidaError(Exception):
    """Excepción personalizada para indicar que la fecha proporcionada es inválida."""
    pass


class EventoNoEncontradoError(Exception):
    """Excepción cuando no se encuentra un evento en el calendario."""
    pass


class EventoDuplicadoError(Exception):
    """Excepción cuando se intenta agregar un evento que ya existe."""
    pass


class FrecuenciaInvalidaError(Exception):
    """Excepción cuando la frecuencia de un evento recurrente no es válida."""
    pass


class CalendarioVacioError(Exception):
    """Excepción cuando se opera sobre un calendario sin eventos."""
    pass