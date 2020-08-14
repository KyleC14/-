'''
遍历删除，注意考虑删除节点为第一位和最后一位的情况
'''

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        start = head
        # 考虑开头第一位
        if start.val == val:
            return start.next
        while start and start.next:
            if start.next.val == val:
                start.next = start.next.next
            start = start.next