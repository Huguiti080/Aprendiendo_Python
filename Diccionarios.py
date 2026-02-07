#INVENTARIO DE TIENDA

inventario = {
    "manzanas": 10,
    "peras": 0,
    "naranjas": 5,
    "uvas": -1,
    "platanos": 8
}

for producto, cantidad in inventario.items(): #items() para obtener clave y valor del diccionario
    if cantidad == -1:
        pass #no hacer nada
    elif cantidad == 0:
        continue #saltar a la siguiente iteracion
    elif cantidad > 7:
        print(f"{producto}: {cantidad} unidades - Stock Alto")
        break #salir del bucle
    else:
        print(f"{producto}: {cantidad} unidades")

#Salida esperada:
#manzanas: 10 unidades - Stock Alto