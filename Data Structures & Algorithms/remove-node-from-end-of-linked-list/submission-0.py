class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy =  ListNode(0)
        curr = dummy

        # first pass: find length'
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        val = len(arr) - n
        for i in range(len(arr)):
            if i == val:
                arr.pop(i)
        
        print(arr)
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
            

       




            
            
            

        
       
    
        