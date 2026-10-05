# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        res = new_list
        carry = 0
        while l1 and l2:
            new_list.next = ListNode()
            new_list = new_list.next
            total = l1.val + l2.val + carry
            new_list.val = total % 10
            carry = total // 10
            l1, l2 = l1.next, l2.next
        longer = l1 if l1 else l2
        while longer:
            new_list.next = ListNode()
            new_list = new_list.next
            total = longer.val + carry
            new_list.val = total % 10
            carry = total // 10
            longer = longer.next
        if carry > 0:
            new_list.next = ListNode()
            new_list = new_list.next
            new_list.val = carry
        return res.next