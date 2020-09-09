'''
非递归 层次遍历 每层层数加1
'''
from collections import deque
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        depth = 0
        #如果root为None,此时队列加入一个None,也为True
        if not root:
            return depth
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth