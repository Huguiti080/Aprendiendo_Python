# 20. Valid Parentheses

## Problema

Dada una cadena que contiene únicamente los caracteres:

- `(`
- `)`
- `[`
- `]`
- `{`
- `}`

Determinar si la cadena es válida.

Una cadena es válida si:

- Cada símbolo de apertura tiene un símbolo de cierre del mismo tipo.
- Los símbolos se cierran en el orden correcto.
- No quedan símbolos de apertura sin cerrar.

## Enfoque

Para resolver el problema se utiliza una **pila (Stack)**.

- Si el carácter es de apertura, se agrega a la pila.
- Si el carácter es de cierre:
  - Se verifica que la pila no esté vacía.
  - Se compara con el último símbolo abierto.
  - Si no coincide, la cadena no es válida.
  - Si coincide, se elimina de la pila.
- Al finalizar, si la pila está vacía, la cadena es válida.

## Complejidad

- Tiempo: **O(n)**
- Espacio: **O(n)**

Donde **n** es la longitud del string.