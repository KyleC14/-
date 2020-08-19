'''
递归检查每个节点是否为倒数第k个节点
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        check = head
        for _ in range(k):
            check = check.next
        if check == None:
            return head
        return self.getKthFromEnd(head.next,k)