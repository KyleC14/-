'''
增加两个变量 一个记录当前待打印的节点数量 一个记录下一层待打印的节点数量
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result,queue=[],deque()
        queue.append(root)
        toBeprint = 1
        nextlevel = 0
        while queue:
            mid = []
            for _ in range(toBeprint):
                node = queue.popleft()
                mid.append(node.val)
                if node.left:
                    queue.append(node.left)
                    nextlevel+=1
                if node.right:
                    queue.append(node.right)
                    nextlevel+=1
            toBeprint = nextlevel
            nextlevel = 0
            result.append(mid)
        return result