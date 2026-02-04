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

# Condicional simple (IF)
edad = int(input("¿Cuántos años tienes? "))

if edad < 18:
    print("⚠️ Esta aventura puede ser peligrosa para menores.")
    continuar = input("¿Deseas continuar de todos modos? (si/no): ")
    if continuar.lower() != "si":
        print("Quizás en otra ocasión. ¡Adiós!")
        exit()

print("\n" + "="*50)
print("CAPÍTULO 1: El Despertar")
print("="*50)

# Condicionales múltiples (IF, ELIF, ELSE)
print("\nDespiertas en una playa. Ves tres caminos:")
print("1. Un sendero hacia la selva 🌴")
print("2. Una cueva oscura 🕳️")
print("3. Subir a una colina 🏔️")

camino = input("\n¿Qué camino eliges? (1/2/3): ")

if camino == "1":
    print("\n🌴 Entras a la selva...")
    print("Encuentras frutas exóticas. Recuperas energía.")
    energia = 100
    
elif camino == "2":
    print("\n🕳️ Entras a la cueva oscura...")
    print("Está muy oscuro. Pierdes algo de energía buscando la salida.")
    energia = 70
    
elif camino == "3":
    print("\n🏔️ Subes la colina...")
    print("Desde arriba ves toda la isla. Ganas conocimiento del terreno.")
    energia = 85
    
else:
    print("\n❌ Opción inválida. Te quedas en la playa.")
    energia = 60

print(f"\n⚡ Energía actual: {energia}%")

# ====================================
# CAPÍTULO 2: Condicionales anidadas
# ====================================

print("\n" + "="*50)
print("CAPÍTULO 2: El Encuentro")
print("="*50)

print("\nEncuentras a un anciano sabio.")

if energia >= 80:
    print("Tienes suficiente energía para hablar con él.")
    
    respuesta = input("\nEl anciano pregunta: '¿Buscas tesoro o sabiduría?' (tesoro/sabiduria): ")
    
    if respuesta.lower() == "tesoro":
        print("\n💰 El anciano te da un mapa del tesoro.")
        tiene_mapa = True
        
        monedas = int(input("¿Cuántas monedas tienes? "))
        
        if monedas >= 50:
            print("✨ Tienes suficientes monedas para comprar equipo.")
            tiene_equipo = True
        else:
            print("💸 No tienes suficientes monedas.")
            tiene_equipo = False
            
    elif respuesta.lower() == "sabiduria":
        print("\n📚 El anciano te enseña antiguos secretos.")
        tiene_mapa = False
        tiene_equipo = False
        sabiduria = True
    else:
        print("\n🤷 El anciano se confunde y se va.")
        tiene_mapa = False
        tiene_equipo = False
        
else:
    print("😴 Estás muy cansado para hablar. El anciano se va.")
    tiene_mapa = False
    tiene_equipo = False

# ====================================
# CAPÍTULO 3: Condiciones complejas
# ====================================

print("\n" + "="*50)
print("CAPÍTULO 3: El Desafío Final")
print("="*50)

print("\nLlegas a un templo antiguo con un guardián.")

fuerza = int(input("¿Cuál es tu nivel de fuerza? (1-100): "))
inteligencia = int(input("¿Cuál es tu nivel de inteligencia? (1-100): "))

# Múltiples condiciones con AND y OR
if (fuerza > 70 and inteligencia > 70) or energia == 100:
    print("\n🏆 ¡VICTORIA TOTAL!")
    print("Eres extremadamente poderoso y sabio.")
    print("El guardián te declara digno del tesoro legendario.")
    resultado = "victoria_total"
    
elif fuerza > 80 or inteligencia > 80:
    print("\n✅ Victoria Parcial")
    print("Impresionas al guardián con tus habilidades.")
    print("Te permite entrar, pero con condiciones.")
    resultado = "victoria_parcial"
    
elif fuerza >= 50 and inteligencia >= 50:
    print("\n⚔️ Desafío Aceptado")
    print("El guardián te propone un duelo de ingenio.")
    
    pregunta = input("\nAcertijo: ¿Qué tiene boca pero no habla? ")
    
    if pregunta.lower() == "rio" or pregunta.lower() == "río":
        print("✨ ¡Correcto! El guardián te deja pasar.")
        resultado = "victoria_acertijo"
    else:
        print("❌ Incorrecto. Debes intentarlo mañana.")
        resultado = "derrota"
        
else:
    print("\n❌ DERROTA")
    print("No estás preparado para este desafío.")
    print("El guardián te sugiere entrenar más.")
    resultado = "derrota"

# ====================================
# FINAL: Resumen de la aventura
# ====================================

print("\n" + "="*50)
print("🎬 FIN DE LA AVENTURA")
print("="*50)

print(f"\nAventurero: {nombre}")
print(f"Energía final: {energia}%")
print(f"Fuerza: {fuerza}")
print(f"Inteligencia: {inteligencia}")

# Condicionales para el resumen
if resultado == "victoria_total":
    puntos = 1000
    rango = "⭐⭐⭐ Maestro Legendario"
elif resultado == "victoria_parcial":
    puntos = 750
    rango = "⭐⭐ Guerrero Destacado"
elif resultado == "victoria_acertijo":
    puntos = 500
    rango = "⭐ Sabio Aprendiz"
else:
    puntos = 250
    rango = "🔰 Novato Valiente"

print(f"Puntos obtenidos: {puntos}")
print(f"Rango alcanzado: {rango}")

# Mensaje personalizado final
if puntos >= 750:
    print("\n🎉 ¡Excelente aventura! Eres un verdadero héroe.")
elif puntos >= 500:
    print("\n👏 Buen trabajo. Sigue mejorando tus habilidades.")
else:
    print("\n💪 No te rindas. Cada aventura es un aprendizaje.")

print("\n¿Quieres jugar de nuevo? ¡Ejecuta el programa otra vez!")