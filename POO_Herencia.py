class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "El perro ladra"

# Crear una instancia de la clase Perro
perro1 = Perro("Rex", 5, "Labrador")
# Usar los métodos de la clase Perro
print(perro1.hacer_sonido())
print(f"El perro se llama {perro1.nombre}, tiene {perro1.edad} años y es de raza {perro1.raza}.")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "El perro ladra"