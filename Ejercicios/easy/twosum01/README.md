# 0001 - Two Sum

##  Problema

Dado un arreglo de enteros `nums` y un número entero `target`, encontrar los índices de los dos números cuya suma sea igual al valor objetivo.

Se asume que:

- Existe una única solución.
- No se puede utilizar el mismo elemento dos veces.

##  Ejemplo

```python
nums = [2, 7, 11, 15]
target = 9

Resultado:
[0, 1]
```

##  Mi solución

Para resolver este problema recorrí la lista dos veces utilizando ciclos `for`.

- El primer ciclo selecciona un número.
- El segundo ciclo compara ese número con todos los demás.
- Se evita comparar un elemento consigo mismo.
- Cuando la suma es igual al `target`, se devuelven los índices correspondientes.

## ️ Complejidad

- Tiempo: **O(n²)**
- Espacio: **O(1)**

##  Próxima mejora

Aprender a resolver este mismo problema utilizando un diccionario (`dict`) para reducir la complejidad a **O(n)**.