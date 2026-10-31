# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2 =[]
        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        arr3 = arr1 + arr2
        arr3.sort()

      
      
      
        # 1. Start with a placeholder node
        dummy = ListNode(0)
        curr = dummy  # This worker pointer will move down the chain

        # 2. Loop through your array
        for i in range(len(arr3)):
            curr.next = ListNode(arr3[i])  # Attach the new node to the end
            curr = curr.next                # Move our worker forward onto the new node

        # 3. Your real list starts right AFTER the dummy placeholder
        head = dummy.next
        return head  # This will print the first real node of your chain


    
      
      
        
    

            

        