'''
先遍历链表构建next部分，并用哈希表（字典）构建关系 NN'(N:原节点 N':构建的新节点)
然后构建新节点的随机指针
'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dic = {None:None}
        newnode = Node(head.val)
        ns = newnode
        os = head
        dic[head] = newnode
        #构建next关系以及哈希表(字典)
        while head.next:
            head = head.next
            node = Node(head.val)
            dic[head] = node
            newnode.next = node
            newnode = node
        newnode.next = None
        newnode = ns
        head = os
        #构建新节点的随机指针
        while head:
            newnode.random = dic[head.random]
            head = head.next
            newnode = newnode.next
        return ns