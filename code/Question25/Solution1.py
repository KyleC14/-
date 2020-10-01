'''
递归写法 比较两个链表的第一个节点 选择较大的那个作为当前的头节点
递归的核心思想是选出当前的头节点(有点像DFS)
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #如果两个链表有一为空 返回剩下的那个
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        #选出当前的头结点
        if l1.val<=l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        #当前头结点的下一个节点由下一次递归决定
        head.next = self.mergeTwoLists(l1,l2)
        return head