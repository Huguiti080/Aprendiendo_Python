# Remove Duplicates from Sorted Array - LeetCode 26

## Descripción del Problema

Dado un arreglo ordenado de números enteros, eliminar los duplicados en el lugar de manera que cada elemento aparezca una sola vez y devolver la nueva longitud del arreglo. La operación debe realizarse sin utilizar espacio adicional y modificando el arreglo original.

## Conceptos Clave Aplicados

### 1. Algoritmo de Dos Punteros

El ejercicio implementa la técnica de dos punteros:
- Puntero de lectura: recorre el arreglo para examinar elementos
- Puntero de escritura: indica la posición donde se debe colocar el siguiente elemento único

Esta técnica permite modificar el arreglo en el lugar mientras se recorre una sola vez.

### 2. Manipulación In-place

- Modificación directa del arreglo original sin crear copias
- Uso de memoria constante O(1) adicional
- Preservación del orden relativo de los elementos

### 3. Estrategia de Recorrido

- El primer elemento siempre se considera único
- Se inicia el recorrido desde el índice 1
- Comparación con el último elemento único almacenado

### 4. Validación de Casos Borde

- Arreglo vacío: retornar 0
- Arreglo con un solo elemento: retornar 1
- Arreglo sin duplicados: todos los elementos se mantienen


## Ejemplo de Ejecución

Entrada: [0,0,1,1,1,2,2,3,3,4]

Pasos:
1. escribir = 1
2. leer = 1: 0 == 0 → sin cambios
3. leer = 2: 1 != 0 → nums[1]=1, escribir=2
4. leer = 5: 2 != 1 → nums[2]=2, escribir=3
5. leer = 7: 3 != 2 → nums[3]=3, escribir=4
6. leer = 9: 4 != 3 → nums[4]=4, escribir=5

Resultado: retorna 5, arreglo: [0,1,2,3,4,2,2,3,3,4]

## Análisis de Complejidad

- Complejidad Temporal: O(n) - un solo recorrido
- Complejidad Espacial: O(1) - sin memoria adicional

## Consideraciones de Implementación

- Validar arreglo vacío antes de acceder a índices
- El índice escribir-1 siempre apunta al último elemento único
- Mantener invariante: los elementos antes de escribir son únicos

## Errores Comunes

- No considerar el arreglo vacío
- Inicializar escribir en 0 en lugar de 1
- Comparar con nums[leer-1] en lugar de nums[escribir-1]
- No actualizar nums[escribir] antes de incrementar

## Aplicaciones Prácticas

- Limpieza de datos duplicados en conjuntos ordenados
- Compresión de datos manteniendo elementos únicos
- Preparación de datos para algoritmos que requieren elementos no repetidos
