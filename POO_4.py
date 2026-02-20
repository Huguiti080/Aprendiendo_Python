class SaldoInsuficienteError(Exception):
    pass

class MontoInvalidoError(Exception):
    pass

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial):
        self.titular = titular # Atributos publicos
        self.numero_cuenta = numero_cuenta # Atributos publicos
        self.__saldo = saldo_inicial # Atributo privado, solo accesible dentro de la clase
    
    def depositar(self, monto): # Metodo para DEPOSITAR dinero en la cuenta
        if monto <=0:
            raise MontoInvalidoError("El monto a depositar debe ser mayor a cero.")
        else:
            # Se accede al atributo privado __saldo dentro de la clase para sumar el monto depositado al saldo actual
            self.__saldo +=monto 
    def retirar(self, monto): # Metodo para RETIRAR dinero de la cuenta
        if monto <=0:
            raise MontoInvalidoError("El monto a retirar debe ser mayor a cero.")
        elif monto > self.__saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar la operación.")
        else:
            # Se accede al atributo privado __saldo dentro de la clase para restar el monto retirado al saldo actual
            self.__saldo -= monto
    
    def mostrar_saldo(self): # Metodo para MOSTRAR el saldo actual de la cuenta, devuelve el valor del atributo privado __saldo
        return self.__saldo

    def _ajustar_saldo(self, monto): # Metodo protegido para ajustar el saldo, utilizado por las clases hijas para modificar el saldo sin exponerlo directamente
        self.__saldo += monto

    def __str__(self):
        return f"Cuenta de {self.titular} - Número: {self.numero_cuenta} - Saldo: {self.__saldo}"

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, saldo_inicial, tasa_interes) :
        super().__init__(titular, numero_cuenta, saldo_inicial)
        self.tasa_interes = tasa_interes
    
    def aplicar_interes(self):
        interes = self.mostrar_saldo()*self.tasa_interes
        self.depositar(interes)

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, saldo_inicial, limite_descubierto):
        super().__init__(titular, numero_cuenta, saldo_inicial)
        self.limite_descubierto = limite_descubierto
    def  retirar (self, monto):
        if monto <= 0:
            raise MontoInvalidoError("El monto a retirar debe ser mayor a cero.")
        elif monto > self.mostrar_saldo() + self.limite_descubierto:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar la operación, incluso con el límite de descubierto.")
        else:
            self._ajustar_saldo(-monto)

class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = [] # Lista vacia, aqui guardaremos las cuentas
    def agregar_cuenta(self, cuenta):                
        self.cuentas.append(cuenta) #Agrega al final de la lista
    def buscar_cuenta (self, numero_cuenta):
        for cuenta in self.cuentas: # Recorre todas las cuentas
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta # encontro -> la retorna y sale
            return None # No encontro -> retorna None
    def reporte_total(self):
        total = 0
        for cuenta in self.cuentas:
            print(cuenta) # Lllama automaticamente a __str__ de la cuenta
            total += cuenta.mostrar_saldo()
        print(f"Total de fondos en el banco {self.nombre}: {total}")

# ---- PRUEBAS ----
banco = Banco("Banco Central")
c1 = CuentaAhorros("Alice", "12345", 1000, 0.10)
c2 = CuentaCorriente("Bob", "67890", 500, 200)

banco.agregar_cuenta(c1)
banco.agregar_cuenta(c2)

# Prueba de depósito
c1.depositar(500)
print(c1)  # Saldo debería ser 1500

# Prueba interes
c1.aplicar_interes()
print(c1)  # Saldo debería ser 1650

# Prueba sobregiro valido
c2.retirar(600)
print(c2)  # Saldo debería ser -100

# Prueba sobregiro invalido - debe lanzar error
try:
    c2.retirar(200)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")  # Debería indicar saldo insuficiente

# Prueba monto invalido
try:
    c1.depositar(-100)
except MontoInvalidoError as e:
    print(f"Error: {e}")  # Debería indicar monto inválido

# Prueba buscar cuenta
cuenta = banco.buscar_cuenta("12345")
print(f"Cuenta encontrada: {cuenta}")  # Debería ser la cuenta de Alice

# Reporte total del banco
banco.reporte_total()