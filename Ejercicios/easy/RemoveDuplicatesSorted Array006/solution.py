class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        #paso 1: si el arreglo esta vacio
        if len(nums) == 0:
            return 0
        # inicializar un indice de ecritura
        escritura = 1

        #recorrer desde el segundo elmento
        for leer in range (1, len(nums)):

            #comparar el elemento actyal con el ultimo unico
            if nums[leer] != nums[escritura - 1]:
                #son diferentes, se coloca el elemento en la posicion de escritura
                nums [escritura] = nums[leer]
                #avanza el indice de escritura
                escritura += 1
        # se devuelve el indice de escritura
        return escritura


        