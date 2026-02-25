class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def __str__(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario Base: {self.salario_base} dolares"
    
    def __repr__(self):
        return f"Empleado(nombre='{self.nombre}', edad={self.edad}, salario_base={self.salario_base})"


    def calcular_salario(self):
        return self.salario_base
    @property
    def salario_base(self):
        return self._salario_base
    @salario_base.setter
    def salario_base(self, valor):
        if valor <= 0:
            raise ValueError("El salario base no puede ser negativo.")
        self._salario_base = valor

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, valor):
        if valor < 18:
            raise ValueError("La edad del empleado debe ser al menos 18 años.")
        self._edad = valor

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, departamento):
        super().__init__(nombre, edad, salario_base)
        self.departamento = departamento

    def calcular_salario(self):
        salario_gerente = self.salario_base * 1.20
        return salario_gerente

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario_base, lenguaje_favorito):
        super().__init__(nombre, edad, salario_base)
        self.lenguaje_favorito = lenguaje_favorito

    def calcular_salario(self):
        salario_desarrollador = self.salario_base * 1.10
        return salario_desarrollador

class Consultor(Empleado):
    def __init__(self, nombre, edad, salario_base, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, edad, salario_base)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_honorarios(self):
        salario_consultor = self.tarifa_hora * self.horas_trabajadas
        return salario_consultor
class FreelancerDev(Desarrollador, Consultor):
    def __init__(self, nombre, edad, salario_base, lenguaje_favorito, tarifa_hora, horas_trabajadas):
        Desarrollador.__init__(self, nombre, edad, salario_base, lenguaje_favorito)
        Consultor.__init__(self, nombre, edad, salario_base, tarifa_hora, horas_trabajadas)

    def calcular_salario(self):
        salario_freelancer = self.calcular_honorarios() + super().calcular_salario()
        return salario_freelancer
# Crear instancias de Gerente y Desarrollador
consultor1 = Consultor("Pedro", 35, 2000, 50, 40)
empleado1 = Empleado("Juan", 30, 3000)
gerente1 = Gerente("Maria", 40, 5000, "Ventas")
desarrollador1 = Desarrollador("Carlos", 25, 4000, "Python")
freelancer1 = FreelancerDev("Ana", 28, 3500, "Java", 60, 35)


print(empleado1)
print(f"Salario de {empleado1.nombre}: {empleado1.calcular_salario()} dolares")

print(gerente1)
print(f"Salario de {gerente1.nombre}: {gerente1.calcular_salario()} dolares")

print(desarrollador1)
print(f"Salario de {desarrollador1.nombre}: {desarrollador1.calcular_salario()} dolares")

print(repr(empleado1))
print(repr(gerente1))
print(repr(desarrollador1))

print(f"Honorarios de {consultor1.nombre}: {consultor1.calcular_honorarios()} dolares")
print(f"Salario total de {freelancer1.nombre}: {freelancer1.calcular_salario()} dolares")

print(f"Orden de resolución de métodos (MRO) de FreelancerDev: {FreelancerDev.__mro__}")

try:
    empleado_invalido = Empleado("Ana", 17, 2500)
except ValueError as e:
    print(f"Error al crear empleado: {e}")
try:
    empleado_invalido1 = Empleado("Luis", 30, -1000)
except ValueError as e:
    print(f"Error al crear empleado: {e}")
        
