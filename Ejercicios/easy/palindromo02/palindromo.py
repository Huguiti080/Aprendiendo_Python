def isPalindrome(x):

    if x < 0:
        print(f"El número {x} no es un palíndromo porque es negativo.")
        return False

    original = x
    numero = x
    invertido = 0

    while numero > 0:
        # Obtener el último dígito del número
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10

    if original == invertido:
        print(f"El número {original} es un palíndromo.")
        return True
    else:
        print(f"El número {original} no es un palíndromo.")
        return False

if __name__ == "__main__":

    print("Ingrese un número entero para verificar si es un palíndromo:")
    x = int(input())

    # x = int(input("Ingrese un número entero para verificar si es un palíndromo: "))

    resultado = isPalindrome(x)

    print(f"Número: {x}")
    print(f"Resultado: {resultado}")

