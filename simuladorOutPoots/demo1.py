def calcular_odds(pozo, apuesta):
    pot_odds = apuesta / (pozo + apuesta) * 100
    return pot_odds

def calcular_equity(outs, calle):
    if calle == "flop":
        equity = outs * 4
    else:
        equity = outs * 2
    return equity


pozo = 200
pozo = float(input("Cuanto hay en el pozo?: "))
apuesta = float(input("Cuanto aposto el rival?: "))
outs = int(input("Cuantos outs tienes: "))
calle = input("En que calle estás? (flop, turn, river): ")

print("Pozo: ", pozo)
print("Apuesta: ", apuesta)
print("Outs: ", outs)
print("Calle: ", calle)

#FUNCIONES
mis_pot_odds = calcular_odds(pozo, apuesta)
mi_equity = calcular_equity(outs, calle)

print("Mis pot odds: ", mis_pot_odds, "%")
print("Mi equity: ", mi_equity, "%")







