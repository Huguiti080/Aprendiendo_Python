class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #crear el nodo dummy y puntero tail
        dummy = ListNode()
        actual = dummy

        #iterar mientrar AMBAS listan tengan nodos
        while list1 and list2:
            if list1.val <= list2.val:
                actual.next = list1
                list1 = list1.next
            else:
                actual.next = list2
                list2 = list2.next
            actual = actual.next
        
        #conectar los nodos restantes
        if list1:
            actual.next = list1
        elif list2:
            actual.next = list2

        #devolcer el inicio de la lista fusionada
        return dummy.next
