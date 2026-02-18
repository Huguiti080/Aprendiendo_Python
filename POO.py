class Persona:
    def __init__(self, nombre, edad,ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}."

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 25, "Madrid")
# Usar los métodos de la clase
print(persona1.presentarse())
print(f"¿Es {persona1.nombre} mayor de edad? {'Sí' if persona1.es_mayor_de_edad() else 'No'}")


# Crear otra instancia de la clase Persona
persona2 = Persona("Ana", 17, "Barcelona")
print(persona2.presentarse())
print(f"¿Es {persona2.nombre} mayor de edad? {'Sí' if persona2.es_mayor_de_edad() else 'No'}")

