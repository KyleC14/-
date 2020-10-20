'''
依照题意，使用中序遍历，获取链表从小到大的链表排序
对排序链表重新构建 右指针指向后续，左指针指向前驱
'''
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def midOrder(root):
            if root.left:
                midOrder(root.left)
            stack.append(root)
            if root.right:
                midOrder(root.right)
            return
        if not root:
            return root
        stack = []
        midOrder(root)
        for i in range(len(stack)):
            if i!=len(stack)-1:
                stack[i].right = stack[i+1]
            else:
                stack[i].right = stack[0]
        for i in range(len(stack)-1,-1,-1):
            if i!=0:
                stack[i].left = stack[i-1]
            else:
                stack[i].left = stack[-1]
        return stack[0]