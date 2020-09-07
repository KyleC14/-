'''
双指针 两个链表指针遍历到结尾则返回到另一个链表的头节点 这样相遇时则是第一个相同的节点
当两者无交点时，最后两个节点会同时为None 不会造成死循环
原理 使得两个链表变成等长
https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        Ahead = headA
        Bhead = headB
        while headA!=headB:
            headA = headA.next if headA else Bhead
            headB = headB.next if headB else Ahead
        return headA