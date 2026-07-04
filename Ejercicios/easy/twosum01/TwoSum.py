

def two_sum(nums, target):

    # Primer ciclo for para recorrer la lista de números y obtener el índice y el número correspondiente
    # enumerate() devuelve un objeto enumerado que contiene pares de índice y valor de la lista
    for indice, numero in enumerate(nums):

        # Segundo ciclo for para recorrer la lista de números nuevamente y obtener el índice y el número correspondiente
        for indice2, numero2 in enumerate (nums):
            
            # Condición para verificar si los índices son diferentes y si la suma de los números es igual al objetivo
            if indice != indice2 and numero + numero2 == target:
                return [indice, indice2]
    pass


if __name__ == "__main__":
    
    nums = [2, 7, 11, 15]
    target = 9

    resultado = two_sum(nums, target)

    print(f"Lista: {nums}")
    print(f"Target: {target}")
    print(f"Resultado: {resultado}")