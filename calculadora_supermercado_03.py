# ====================================
# PROGRAMA: Calculadora de Supermercado
# TEMA: Operadores en Python
# ====================================

print("🛒 === BIENVENIDO AL SUPERMERCADO === 🛒\n")

# ====================================
# OPERADORES ARITMÉTICOS
# ====================================

print("--- SECCIÓN 1: COMPRANDO PRODUCTOS ---\n")

# Ingreso de datos
precio_manzanas = float(input("Precio por kg de manzanas: $"))
kg_manzanas = float(input("¿Cuántos kg de manzanas compras? "))

precio_leche = float(input("Precio de la leche: $"))
cantidad_leche = int(input("¿Cuántas leches compras? "))

precio_pan = float(input("Precio del pan: $"))
cantidad_pan = int(input("¿Cuántos panes compras? "))

# Cálculos con operadores aritméticos
subtotal_manzanas = precio_manzanas * kg_manzanas  # Multiplicación
subtotal_leche = precio_leche * cantidad_leche
subtotal_pan = precio_pan * cantidad_pan

total_sin_descuento = subtotal_manzanas + subtotal_leche + subtotal_pan  # Suma

print(f"\n📊 Subtotal manzanas: ${subtotal_manzanas:.2f}")
print(f"📊 Subtotal leche: ${subtotal_leche:.2f}")
print(f"📊 Subtotal pan: ${subtotal_pan:.2f}")
print(f"\n💵 TOTAL SIN DESCUENTO: ${total_sin_descuento:.2f}")

# ====================================
# OPERADORES DE COMPARACIÓN Y LÓGICOS
# ====================================

print("\n--- SECCIÓN 2: DESCUENTOS ESPECIALES ---\n")

# Aplicar descuento si el total es mayor a $100
tiene_descuento = total_sin_descuento > 100  # Operador de comparación >
print(f"¿Califica para descuento? (compra > $100): {tiene_descuento}")

# Descuento adicional si es estudiante o adulto mayor
es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"
es_adulto_mayor = input("¿Eres adulto mayor? (si/no): ").lower() == "si"

# Operador lógico OR
descuento_especial = es_estudiante or es_adulto_mayor

if tiene_descuento and descuento_especial:  # Operador lógico AND
    descuento = total_sin_descuento * 0.20  # 20% de descuento
    print("🎉 ¡Felicidades! Tienes 20% de descuento")
elif tiene_descuento:
    descuento = total_sin_descuento * 0.10  # 10% de descuento
    print("✨ Tienes 10% de descuento por compra mayor a $100")
elif descuento_especial:
    descuento = total_sin_descuento * 0.05  # 5% de descuento
    print("👍 Tienes 5% de descuento especial")
else:
    descuento = 0
    print("Sin descuento esta vez")

# ====================================
# MÁS OPERADORES ARITMÉTICOS
# ====================================

total_con_descuento = total_sin_descuento - descuento  # Resta

# División exacta y división entera
print(f"\n--- SECCIÓN 3: OPCIONES DE PAGO ---\n")
meses = int(input("¿En cuántos meses quieres pagar? (1, 3, 6, 12): "))

pago_mensual = total_con_descuento / meses  # División normal
print(f"💳 Pago mensual: ${pago_mensual:.2f}")

# Módulo (%) - para saber si hay residuo
productos_totales = int(cantidad_leche + cantidad_pan)
productos_por_bolsa = 5
bolsas_necesarias = productos_totales // productos_por_bolsa  # División entera
productos_sobrantes = productos_totales % productos_por_bolsa  # Módulo

print(f"\n📦 Necesitas {bolsas_necesarias} bolsas completas")
print(f"📦 Sobran {productos_sobrantes} productos")

# Potencia (**)
puntos_base = 10
puntos_ganados = puntos_base ** 2  # 10 elevado al cuadrado
print(f"\n⭐ Puntos ganados: {puntos_ganados} puntos")

# ====================================
# TICKET FINAL
# ====================================

print("\n" + "="*50)
print("🧾 TICKET DE COMPRA")
print("="*50)
print(f"Subtotal:          ${total_sin_descuento:.2f}")
print(f"Descuento (-):     ${descuento:.2f}")
print(f"TOTAL A PAGAR:     ${total_con_descuento:.2f}")
print(f"Pago mensual:      ${pago_mensual:.2f} x {meses} meses")
print(f"Puntos ganados:    {puntos_ganados} ⭐")
print("="*50)

# ====================================
# COMPARACIONES FINALES
# ====================================

print("\n--- ANÁLISIS DE TU COMPRA ---\n")

# Operadores de comparación
print(f"Total > $200: {total_con_descuento > 200}")
print(f"Total < $50: {total_con_descuento < 50}")
print(f"Total == $100: {total_con_descuento == 100}")
print(f"Total != $0: {total_con_descuento != 0}")
print(f"Compra >= $100: {total_con_descuento >= 100}")
print(f"Compra <= $500: {total_con_descuento <= 500}")

# Operador lógico NOT
no_es_estudiante = not es_estudiante
print(f"\n¿NO eres estudiante?: {no_es_estudiante}")

print("\n✅ ¡Gracias por tu compra! Vuelve pronto 🛒")