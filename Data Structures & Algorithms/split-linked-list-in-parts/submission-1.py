# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count the nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        base_size = count // k
        extra = count % k

        parts = []
        current = head

        for i in range(k):
            part_head = current
            part_size = base_size

            # Give one extra node to the first `extra` parts
            if i < extra:
                part_size += 1

            # Move to the end of this part
            for _ in range(part_size - 1):
                if current:
                    current = current.next

            # Cut this part off from the rest of the list
            if current:
                next_part = current.next
                current.next = None
                current = next_part

            parts.append(part_head)

        return parts