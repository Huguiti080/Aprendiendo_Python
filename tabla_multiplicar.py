#========================================================================================
print("=====TABLA DE MULTIPLICAR=====")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
limite = int(input("¿Hasta qué número quieres que aparezcan las multiplicaciones?: "))

print(f"-----TABLA DEL {numero} (del 1 al {limite})-----")

for i in range(1, limite + 1):
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")