'''
依靠队列（或者列表）的辅助，依照根、左、右层次遍历的顺序进行遍历
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        stack, i = [], 0
        stack.append(root)
        result = []
        if not root:
            return result
        result.append(root.val)
        #这里必须使用while 如果是range的话 对于 python ，range() 的工作机制是在开启循环时建立一个列表，然后循环按照这个列表进行，因此“只会在进入循环前执行一次 len(queue) ” ；
        while i<len(stack):
            if stack[i].left:
                stack.append(stack[i].left)
                result.append(stack[i].left.val)
            if stack[i].right:
                stack.append(stack[i].right)
                result.append(stack[i].right.val)
            i+=1
        return result
'''
使用队列改进版
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result,de = [],deque()
        de.append(root)
        while de:
            node = de.popleft()
            result.append(node.val)
            if node.left:
                de.append(node.left)
            if node.right:
                de.append(node.right)
        return result