'''
压栈 从结尾开始比较 返回最后一个相同的节点
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA, stackB = [] ,[]
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        node = None
        while stackA and stackB and stackA[-1] == stackB[-1]:
            node = stackA.pop()
            stackB.pop()
        return node