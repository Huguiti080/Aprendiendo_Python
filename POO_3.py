class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"[{self.id_empleado}] {self.nombre} - Salario: ${self.calcular_salario():,.2f}"
        
##############################################
class EmpleadoTiempoCompleto(Empleado): #Entre parentesis va la clase padre
    def __init__(self, nombre, id_empleado, salario_base, bono):
        super().__init__(nombre, id_empleado, salario_base) #Llama al constructor del padre
        self.bono = bono # Atributo específico de esta clase hija

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * self.bono) # Sobrescribe el método del padre para incluir el bono
##############################################
class EmpleadoFreelance(Empleado):
    def __init__(self, nombre, id_empleado, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado, 0) # No se usa salario_base en esta clase
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas
    def calcular_salario(self):
        return self.tarifa_por_hora * self.horas_trabajadas # Calcula el salario basado en horas trabajadas

#________CLASE EMPRESA__________
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = [] # Lista para almacenar empleados

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado): # Validar que el objeto sea una instancia de Empleado o sus subclases
            self.empleados.append(empleado) #Si si agrega a la lista de empleados
        else:
            print("Solo se pueden agregar objetos de tipo Empleado.")

    def mostrar_empleados(self):
        print(f"\n=== Empleados de {self.nombre} ===")
        for emp in self.empleados:
            print(emp) #se usa el __str__ de cada empleado para mostrar su información
    def calcular_nomina_total(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.calcular_salario() # Suma el salario de cada empleado usando su método calcular_salario
        print(f"\nTotal de nómina para {self.nombre}: ${total:,.2f}")


#instancia de empresa
empresa = Empresa("Tech Solutions")
#instancias de empleados
emp1 = Empleado("Ana Garcia", "101", 15000)
emp2 = EmpleadoTiempoCompleto("Carlos Perez", "102", 20000, 0.10)
emp3 = EmpleadoFreelance("Maria Torres", "103", 500, 40) # Tarifa por hora y horas trabajadas
#agregar empleados a la empresa
empresa.agregar_empleado(emp1)
empresa.agregar_empleado(emp2)
empresa.agregar_empleado(emp3)
#mostrar empleados de la empresa
empresa.mostrar_empleados()
#calcular nómina total de la empresa
empresa.calcular_nomina_total()

#print(emp1)  # Muestra el salario base
#print(emp2)  # Muestra el salario con bono incluido
#print(emp3)  # Muestra el salario freelance calculado

