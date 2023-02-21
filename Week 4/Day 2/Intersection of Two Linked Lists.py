# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        pA = headA
        pB = headB
        while pA is not pB: 
            """
            # if pA == pB:
                # return pA
            if pA is None:
                PA = headB
            else:
                PA = pA.next
            if pB is None:
                pB = headA
            else:
                pB = pB.next
                """
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA
            
            