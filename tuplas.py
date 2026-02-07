#tupla
coordenadas = [(0,0), (3,4),(1,2),(0,5),(6,8)]

for coordenada in coordenadas:
    x, y = coordenada #desempaquetado de tupla
    if x==0 and y==0:
        pass #no hacer nada
    else:
        distancia = (x**2 + y**2)**0.5
        print(f"Coordenada: {coordenada}, Distancia al origen: {distancia:.2f}")
#Salida esperada:
#Coordenada: (3, 4), Distancia al origen: 5.