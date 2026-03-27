cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)

palabras = ["Python", "Java", "C++", "JavaScript"]
mayusculas = [palabra.upper() if len(palabra) >4 else palabra for palabra in palabras]
print(mayusculas)

temperaturas_celsius = [0, 10, 20, 30, 40, -10, 0, 15, 23, -35, -37, 100]
temperatura_fahrenheit = [celcius * 9/5 + 32 if celcius >= 0 else "Temperatura negativa" for celcius in temperaturas_celsius]
print(temperatura_fahrenheit)