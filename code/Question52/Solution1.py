'''
使用哈希表记录第一个链表经过的节点 然后遍历第二个链表并在哈希表中检索 若有相同则返回
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dica = {}
        while headA:
            dica[headA] = headA
            headA = headA.next
        while headB:
            if headB in dica:
                return headB
            headB = headB.next
        return None