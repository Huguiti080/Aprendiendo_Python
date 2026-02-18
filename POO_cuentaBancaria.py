class CuentaBancaria:
    def __init__(self, titular, numero_cuenta):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.__saldo = 0          # Privado, no se puede modificar directamente
        self.__historial = []     # Privado, lista de movimientos

    def depositar(self, cantidad):
        if cantidad <= 0:
            print(" La cantidad a depositar debe ser mayor a 0.")
            return
        self.__saldo += cantidad
        self.__historial.append(f"[+] Depósito: ${cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print(" La cantidad a retirar debe ser mayor a 0.")
            return
        if cantidad > self.__saldo:
            print(f" Saldo insuficiente. Tu saldo actual es ${self.__saldo}")
            return
        self.__saldo -= cantidad
        self.__historial.append(f"[-] Retiro: ${cantidad}")

    def consultar_saldo(self):
        return self.__saldo

    def ver_historial(self):
        print(f"\n=== Historial de {self.titular} ({self.numero_cuenta}) ===")
        if not self.__historial:
            print("No hay movimientos registrados.")
        else:
            for movimiento in self.__historial:
                print(movimiento)
        print(f"Saldo actual: ${self.__saldo}\n")

    def transferir(self, cantidad, cuenta_destino):
        # Validar que el destino sea una cuenta bancaria válida
        if not isinstance(cuenta_destino, CuentaBancaria):
            print(" La cuenta destino no es válida.")
            return
        if cantidad <= 0:
            print(" La cantidad a transferir debe ser mayor a 0.")
            return
        if cantidad > self.__saldo:
            print(f" Saldo insuficiente para transferir. Tu saldo es ${self.__saldo}")
            return

        # Retirar de la cuenta origen y depositar en la destino
        self.__saldo -= cantidad
        self.__historial.append(f"[-] Transferencia enviada a {cuenta_destino.numero_cuenta}: ${cantidad}")

        cuenta_destino.__saldo += cantidad
        cuenta_destino.__historial.append(f"[+] Transferencia recibida de {self.numero_cuenta}: ${cantidad}")


class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, numero_cuenta, tasa_interes):
        super().__init__(titular, numero_cuenta)   # Llama al constructor del padre
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        saldo_actual = self.consultar_saldo()
        if saldo_actual <= 0:
            print(" No hay saldo para aplicar interés.")
            return
        interes = saldo_actual * self.tasa_interes
        self.depositar(interes)
        # Reemplaza el último registro del historial para que sea más descriptivo
        self._CuentaBancaria__historial[-1] = f"[+] Interés aplicado ({self.tasa_interes*100}%): ${interes}"


# ===================== PRUEBA DEL SISTEMA =====================

print("=" * 50)
print("        SISTEMA BANCARIO - PRUEBA COMPLETA")
print("=" * 50)

# Crear cuentas
cuenta1 = CuentaBancaria("Juan", "001")
cuenta2 = CuentaAhorros("Sofia", "002", tasa_interes=0.05)

# Operaciones en cuenta1
cuenta1.depositar(5000)
cuenta1.depositar(-200)       # Debe mostrar error
cuenta1.retirar(1000)
cuenta1.retirar(9999)         # Debe mostrar error de saldo insuficiente
cuenta1.transferir(500, cuenta2)

# Operaciones en cuenta2
cuenta2.depositar(1000)
cuenta2.aplicar_interes()

# Intentar transferir a algo que no es una cuenta
cuenta1.transferir(100, "esto_no_es_una_cuenta")  # Debe mostrar error

# Ver historiales
cuenta1.ver_historial()
cuenta2.ver_historial()