from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        primera_palabra = strs[0]
        prefijo = ""

        for i in range(len(primera_palabra)):
            for palabra in strs:
                if i >= len(palabra):
                    return prefijo

                if palabra[i] != primera_palabra[i]:
                    return prefijo

            prefijo += primera_palabra[i]

        return prefijo


sol = Solution()

resultado = sol.longestCommonPrefix(
    ["flower","flow","flight"]
)

print(resultado)