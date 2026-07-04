El objetivo es determinar si un número entero es un palíndromo, es decir, si se lee igual d

# Lógica de la solución

La solución consiste en invertir el número utilizando operaciones matemáticas y compararlo con el valor original.

Pasos del algoritmo:

1. Guardar el número original.
2. Crear una variable para almacenar el número invertido.
3. Mientras el número sea mayor que cero:
   - Obtener el último dígito utilizando `% 10`.
   - Agregar ese dígito al número invertido.
   - Eliminar el último dígito utilizando `// 10`.
4. Comparar el número invertido con el número original.
5. Si ambos son iguales, el número es un palíndromo.