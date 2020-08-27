'''
链接法
1. 遍历原链表，对每个节点构建一个新节点，并链接在原节点后面
2. 构建新节点的随机指针，对于新节点的随机指针，等于原节点随机指针的next
3. 拆分两个链表
'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        newNode = Node(head.val)
        ns = newNode
        os = head
        #把新建的节点构建在每一个节点后面
        while head.next:
            headNext = head.next
            newNextNode = Node(headNext.val)
            newNode.next = headNext
            head.next = newNode
            head = headNext
            newNode = newNextNode
        #补齐最后一步
        head.next,newNode.next = newNode,None
        head = os
        newNode = ns
        #构建random指针
        while newNode.next:
            if head.random:
                newNode.random = head.random.next
            else:
                newNode.random = None
            head = head.next.next
            newNode = newNode.next.next
        #补齐最后一步
        if head.random:
            newNode.random = head.random.next
        else:
            newNode.random = None
        #拆分两个链表：
        newNode = ns
        while newNode.next:
            newNode.next = newNode.next.next
            newNode = newNode.next
        return ns