# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:  # Use or
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:  # Check fast
            slow = slow.next
            fast = fast.next.next

        end = slow.next
        slow.next = None  # Split the list into two halves

        # Reverse the second half
        prev = None
        curr = end

        while curr:
            num = curr.next
            curr.next = prev
            prev = curr
            curr = num

        # Merge the two halves
        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second



        
            



        