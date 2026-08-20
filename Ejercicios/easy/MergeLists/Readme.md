
fusionar dos listas enlazadas ordenadas en una sola lista ordenada.



Comparar mientras ambas tengan nodos:

Si list1 tiene el valor más pequeño → lo tomo

Si no → tomo de list2

Cuando una lista se vacíe:

Conecto todo lo que queda de la otra lista

El problema: ¿Cómo construyo el resultado sin perder el inicio?

La solución: Usar un nodo dummy como ancla y un puntero tail como constructor.


