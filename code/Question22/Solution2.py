'''
双指针法 第一个指针先走k步，然后第二个指针开始同时走，等到第一个指针走完时，返回第二个指针
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        result = head
        for _ in range(k):
            result = result.next
        while result!=None:
            result = result.next
            head = head.next
        return head