class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        resultado = 0

        for i in range(len(s)):
            valor_actual = valores[s[i]]

            if i + 1 < len(s) and valores[s[i + 1]] > valor_actual:
                resultado -= valor_actual
            else:
                resultado += valor_actual

        return resultado