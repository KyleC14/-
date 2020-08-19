'''
递归写法 比较两个链表的第一个节点 选择较大的那个
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val<=l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        head.next = self.mergeTwoLists(l1,l2)
        return head