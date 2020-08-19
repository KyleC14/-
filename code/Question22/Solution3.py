'''
利用栈先进后出的特性
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        stack = []
        while head!=None:
            stack.append(head)
            head = head.next
        for _ in range(k):
            head = stack.pop()
        return head