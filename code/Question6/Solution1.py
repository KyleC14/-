'''
递归调用自身
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        if head.next == None:
            return [head.val]
        return self.reversePrint(head.next)+[head.val]