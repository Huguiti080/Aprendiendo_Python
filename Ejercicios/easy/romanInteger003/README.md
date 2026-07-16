# 13. Roman to Integer

## Descripción

Dado un número romano, convertirlo a su representación como número entero.

## Enfoque

- Almacenar el valor de cada símbolo romano en un diccionario.
- Recorrer la cadena de izquierda a derecha.
- Si el valor actual es menor que el siguiente, restarlo del resultado.
- En caso contrario, sumarlo al resultado.
- Devolver el resultado final.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)

## Conceptos practicados

- Diccionarios (`dict`)
- Recorrido de cadenas
- Condicionales
- Manejo de índices