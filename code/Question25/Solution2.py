'''
非递归写法
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
        result = head
        while l1 and l2:
            if l1.val<=l2.val:
                head.next,l1 = l1,l1.next
            else:
                head.next,l2 = l2,l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return result

'''
优化后的非递归写法 参考https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/solution/mian-shi-ti-25-he-bing-liang-ge-pai-xu-de-lian-b-2/
增加一个头结点，也巧妙把传入有空链表的情况融合在一起
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head = ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                head.next,l1 = l1,l1.next
            else:
                head.next,l2 = l2,l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return result.next