'''
原版书上应该是这样的
删除前n-1个节点时间复杂度为O(1),删除最后一个节点时间复杂度为O(n)
时间复杂度 (O(1)*n-1+O(n))/n = O(1)
思路 除了最后一个节点以外 删除当前节点 要删除的节点的下一个节点原封不动复制到当前节点即可
'''
class Solution:
    def deleteNode(self, head: ListNode, val: ListNode) -> ListNode:
        if head is None or ListNode is None:
            return None
        #删除节点在开头
        if head.val == val.val:
            return head.next
        #删除节为结尾
        elif val.next is None:
            start = head
            while start:
                if start.next == val:
                    start.next = None
                start = start.next
        #删除节点非结尾
        else:
            val.val,val.next = val.next.val,val.next.next
        return head