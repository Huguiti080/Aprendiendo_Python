# ====================================
# PROGRAMA: Aventura en la Isla Misteriosa
# TEMA: Condicionales (if, elif, else)
# ====================================

print("🏝️ === AVENTURA EN LA ISLA MISTERIOSA === 🏝️\n")
print("Has naufragado en una isla desconocida...")
print("Tus decisiones determinarán tu destino.\n")

# ====================================
# INICIO DE LA AVENTURA
# ====================================

nombre = input("¿Cuál es tu nombre, aventurero? ")
print(f"\nBienvenido, {nombre}. Tu aventura comienza ahora...\n")

# ====================================
# CONDICIONAL SIMPLE (IF)
# ====================================
# Un IF simple solo tiene una condición
# Si se cumple (True), ejecuta el código dentro
# Si NO se cumple (False), salta todo ese bloque

edad = int(input("¿Cuántos años tienes? "))

# Aquí preguntamos: ¿la edad es menor a 18?
if edad < 18:
    # Este bloque SOLO se ejecuta si edad < 18 es True
    print("⚠️ Esta aventura puede ser peligrosa para menores.")
    continuar = input("¿Deseas continuar de todos modos? (si/no): ")
    
    # IF ANIDADO: Un if dentro de otro if
    # Primero verifica edad < 18, luego verifica la respuesta
    if continuar.lower() != "si":
        # != significa "diferente de"
        # Si escribió algo diferente a "si", el programa termina
        print("Quizás en otra ocasión. ¡Adiós!")
        exit()  # Termina el programa aquí
    # Si escribió "si", continúa ejecutando el código después del if

# Si la edad >= 18, Python ignora todo el bloque anterior
# y continúa aquí directamente

print("\n" + "="*50)
print("CAPÍTULO 1: El Despertar")
print("="*50)

# ====================================
# CONDICIONALES MÚLTIPLES (IF, ELIF, ELSE)
# ====================================
# IF: Primera condición a verificar
# ELIF: "Else if" - Si el IF anterior fue False, verifica esta nueva condición
# ELSE: Si todas las anteriores fueron False, ejecuta esto

print("\nDespiertas en una playa. Ves tres caminos:")
print("1. Un sendero hacia la selva 🌴")
print("2. Una cueva oscura 🕳️")
print("3. Subir a una colina 🏔️")

camino = input("\n¿Qué camino eliges? (1/2/3): ")

# Python evalúa de arriba hacia abajo
# Solo entra en UNA de estas opciones

if camino == "1":
    # ¿camino es igual a "1"? Si es True, entra aquí
    print("\n🌴 Entras a la selva...")
    print("Encuentras frutas exóticas. Recuperas energía.")
    energia = 100
    # Después de esto, Python SALTA todo lo demás (elif y else)
    
elif camino == "2":
    # Solo llega aquí si el IF anterior fue False
    # ¿camino es igual a "2"? Si es True, entra aquí
    print("\n🕳️ Entras a la cueva oscura...")
    print("Está muy oscuro. Pierdes algo de energía buscando la salida.")
    energia = 70
    # Después de esto, Python SALTA el resto (otros elif y else)
    
elif camino == "3":
    # Solo llega aquí si IF y primer ELIF fueron False
    # ¿camino es igual a "3"? Si es True, entra aquí
    print("\n🏔️ Subes la colina...")
    print("Desde arriba ves toda la isla. Ganas conocimiento del terreno.")
    energia = 85
    # Después de esto, Python SALTA el else
    
else:
    # Solo llega aquí si TODAS las condiciones anteriores fueron False
    # Es el "plan B" cuando nada más funcionó
    print("\n❌ Opción inválida. Te quedas en la playa.")
    energia = 60

# Después del if-elif-else, el código continúa normalmente
# En este punto, 'energia' ya tiene un valor asignado
print(f"\n⚡ Energía actual: {energia}%")

# ====================================
# CAPÍTULO 2: CONDICIONALES ANIDADAS
# ====================================
# Un condicional ANIDADO es un if dentro de otro if
# Piensa en ellos como "niveles" de decisión

print("\n" + "="*50)
print("CAPÍTULO 2: El Encuentro")
print("="*50)

print("\nEncuentras a un anciano sabio.")

# PRIMER NIVEL: Verificamos la energía
if energia >= 80:
    # Solo entra aquí si energia es mayor o igual a 80
    print("Tienes suficiente energía para hablar con él.")
    
    respuesta = input("\nEl anciano pregunta: '¿Buscas tesoro o sabiduría?' (tesoro/sabiduria): ")
    
    # SEGUNDO NIVEL: Dentro del primer if, hay otro if-elif-else
    # Estos solo se evalúan si ya pasamos el primer nivel (energia >= 80)
    
    if respuesta.lower() == "tesoro":
        # ¿Eligió tesoro? Si es True, entra aquí
        print("\n💰 El anciano te da un mapa del tesoro.")
        tiene_mapa = True
        
        monedas = int(input("¿Cuántas monedas tienes? "))
        
        # TERCER NIVEL: Otro if dentro del segundo if
        # Solo se evalúa si: energia >= 80 Y respuesta == "tesoro"
        if monedas >= 50:
            # ¿Tiene 50 o más monedas? Si es True, entra aquí
            print("✨ Tienes suficientes monedas para comprar equipo.")
            tiene_equipo = True
        else:
            # Si monedas < 50, entra aquí
            print("💸 No tienes suficientes monedas.")
            tiene_equipo = False
            
    elif respuesta.lower() == "sabiduria":
        # Solo llega aquí si energia >= 80 Y respuesta != "tesoro"
        # ¿Eligió sabiduría? Si es True, entra aquí
        print("\n📚 El anciano te enseña antiguos secretos.")
        tiene_mapa = False
        tiene_equipo = False
        sabiduria = True
        
    else:
        # Solo llega aquí si energia >= 80 Y respuesta no es ni "tesoro" ni "sabiduria"
        print("\n🤷 El anciano se confunde y se va.")
        tiene_mapa = False
        tiene_equipo = False
        
else:
    # Solo entra aquí si energia < 80 (primer nivel fue False)
    # Esto significa que NUNCA llegó a preguntar sobre tesoro o sabiduría
    print("😴 Estás muy cansado para hablar. El anciano se va.")
    tiene_mapa = False
    tiene_equipo = False

# ====================================
# CAPÍTULO 3: CONDICIONES COMPLEJAS CON AND/OR
# ====================================
# AND: Ambas condiciones deben ser True
# OR: Al menos UNA condición debe ser True

print("\n" + "="*50)
print("CAPÍTULO 3: El Desafío Final")
print("="*50)

print("\nLlegas a un templo antiguo con un guardián.")

fuerza = int(input("¿Cuál es tu nivel de fuerza? (1-100): "))
inteligencia = int(input("¿Cuál es tu nivel de inteligencia? (1-100): "))

# CONDICIONES COMPLEJAS:
# (A and B) or C significa: (A Y B son True) O (C es True)

if (fuerza > 70 and inteligencia > 70) or energia == 100:
    # Veamos cómo Python evalúa esto:
    # Opción 1: fuerza > 70 AND inteligencia > 70 (ambas deben ser True)
    # Opción 2: energia == 100 (solo esta debe ser True)
    # Si CUALQUIERA de las dos opciones es True, entra aquí
    
    # Ejemplos donde entraría:
    # - fuerza=80, inteligencia=80, energia=50 → (True and True) or False → True
    # - fuerza=50, inteligencia=50, energia=100 → (False and False) or True → True
    # - fuerza=80, inteligencia=80, energia=100 → (True and True) or True → True
    
    print("\n🏆 ¡VICTORIA TOTAL!")
    print("Eres extremadamente poderoso y sabio.")
    print("El guardián te declara digno del tesoro legendario.")
    resultado = "victoria_total"
    
elif fuerza > 80 or inteligencia > 80:
    # Solo llega aquí si el IF anterior fue False
    # OR significa que al menos UNA debe ser True
    # Si fuerza > 80 es True → entra
    # Si inteligencia > 80 es True → entra
    # Si ambas son True → también entra
    
    print("\n✅ Victoria Parcial")
    print("Impresionas al guardián con tus habilidades.")
    print("Te permite entrar, pero con condiciones.")
    resultado = "victoria_parcial"
    
elif fuerza >= 50 and inteligencia >= 50:
    # Solo llega aquí si los dos IF anteriores fueron False
    # AND significa que AMBAS deben ser True
    # Si fuerza >= 50 es True pero inteligencia < 50 → NO entra
    # Si fuerza < 50 pero inteligencia >= 50 → NO entra
    # Ambas deben ser True para entrar
    
    print("\n⚔️ Desafío Aceptado")
    print("El guardián te propone un duelo de ingenio.")
    
    pregunta = input("\nAcertijo: ¿Qué tiene boca pero no habla? ")
    
    # IF ANIDADO dentro del elif
    if pregunta.lower() == "rio" or pregunta.lower() == "río":
        # Acepta "rio" O "río" (con o sin acento)
        print("✨ ¡Correcto! El guardián te deja pasar.")
        resultado = "victoria_acertijo"
    else:
        # Si la respuesta es cualquier otra cosa
        print("❌ Incorrecto. Debes intentarlo mañana.")
        resultado = "derrota"
        
else:
    # Solo llega aquí si TODAS las condiciones anteriores fueron False
    # Esto significa: fuerza < 50 O inteligencia < 50 (no cumplió ningún requisito)
    print("\n❌ DERROTA")
    print("No estás preparado para este desafío.")
    print("El guardián te sugiere entrenar más.")
    resultado = "derrota"

# ====================================
# FINAL: RESUMEN CON MÚLTIPLES IF-ELIF-ELSE
# ====================================

print("\n" + "="*50)
print("🎬 FIN DE LA AVENTURA")
print("="*50)

print(f"\nAventurero: {nombre}")
print(f"Energía final: {energia}%")
print(f"Fuerza: {fuerza}")
print(f"Inteligencia: {inteligencia}")

# Asignamos puntos y rango según el resultado
# Nota: resultado es una variable string que definimos antes

if resultado == "victoria_total":
    # ¿resultado es igual a "victoria_total"? Si es True, asigna estos valores
    puntos = 1000
    rango = "⭐⭐⭐ Maestro Legendario"
    
elif resultado == "victoria_parcial":
    # Solo verifica esto si el IF anterior fue False
    puntos = 750
    rango = "⭐⭐ Guerrero Destacado"
    
elif resultado == "victoria_acertijo":
    # Solo verifica esto si los dos anteriores fueron False
    puntos = 500
    rango = "⭐ Sabio Aprendiz"
    
else:
    # Si ninguno de los anteriores fue True (resultado == "derrota")
    puntos = 250
    rango = "🔰 Novato Valiente"

print(f"Puntos obtenidos: {puntos}")
print(f"Rango alcanzado: {rango}")

# Mensaje personalizado según los puntos obtenidos
if puntos >= 750:
    # ¿puntos es mayor o igual a 750? (victoria_total o victoria_parcial)
    print("\n🎉 ¡Excelente aventura! Eres un verdadero héroe.")
    
elif puntos >= 500:
    # Solo llega aquí si puntos < 750
    # ¿puntos es mayor o igual a 500? (victoria_acertijo)
    print("\n👏 Buen trabajo. Sigue mejorando tus habilidades.")
    
else:
    # Solo llega aquí si puntos < 500 (derrota)
    print("\n💪 No te rindas. Cada aventura es un aprendizaje.")

print("\n¿Quieres jugar de nuevo? ¡Ejecuta el programa otra vez!")

# ====================================
# RESUMEN DE CONDICIONALES USADOS:
# ====================================
# 1. IF simple: Una sola condición
# 2. IF-ELSE: Dos caminos (si pasa esto, si no pasa)
# 3. IF-ELIF-ELSE: Múltiples opciones mutuamente excluyentes
# 4. IF anidado: Un if dentro de otro if (niveles de decisión)
# 5. Condiciones con AND: Ambas deben ser True
# 6. Condiciones con OR: Al menos una debe ser True
# 7. Condiciones complejas: Combinación de AND y OR con paréntesis