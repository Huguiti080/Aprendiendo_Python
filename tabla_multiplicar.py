#========================================================================================
print("=====TABLA DE MULTIPLICAR=====")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
limite = int(input("¿Hasta qué número quieres que aparezcan las multiplicaciones?: "))
saltar = int(input("¿Quieres saltar alguna multiplicación? Ingresa el número o 0 para no saltar ninguna: "))

print(f"-----TABLA DEL {numero} (del 1 al {limite})-----")

for i in range(1, limite + 1):
    resultado = numero * i
    if i == saltar:
        continue
    
    print(f"{numero} x {i} = {resultado}")