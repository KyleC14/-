'''
利用列表或栈存储遍历的链表，然后重新构造
'''


'''
利用列表重新构建顺序
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        rep = []
        while head != None:
            rep.append(head)
            head = head.next
        for i in range(len(rep)-1,0,-1):
            rep[i].next = rep[i-1]
        rep[0].next = None
        return rep[-1]
'''
利用栈
'''
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        rep = []
        while head.next != None:
            rep.append(head)
            head = head.next
        tmp = head
        for i in range(len(rep)-1,-1,-1):
            head.next = rep.pop()
            head = head.next
        head.next = None
        return tmp