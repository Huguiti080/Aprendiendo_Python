class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pares = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for caracter in s:

            if caracter in "([{":
                stack.append(caracter)

            else:

                if not stack:
                    return False

                ultimo = stack[-1]

                if ultimo != pares[caracter]:
                    return False

                stack.pop()

        return not stack