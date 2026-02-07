#Crear lista
numeros = [12, -5, 8, -3, 0, 7, -1, 4, 20]

for numero in numeros:
    if numero == 0:
        break
    elif numero < 0:
        continue
    else:
        print(numero)
#Salida esperada:
#12
#8
#7
#4
