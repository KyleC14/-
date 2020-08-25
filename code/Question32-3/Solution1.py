from collections import deque
'''
增加一个控制逆序与否的变量开关
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result,queue=[],deque()
        queue.append(root)
        even = True
        while queue:
            mid = []
            for _ in range(len(queue)):
                node = queue.popleft()
                mid.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if even:
                result.append(mid)
            else:
                mid.reverse()
                result.append(mid)
            even = not even
        return result
'''
题解版逆序
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result,queue=[],deque()
        queue.append(root)
        while queue:
            mid = []
            for _ in range(len(queue)):
                node = queue.popleft()
                mid.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(result)%2==0:
                result.append(mid)
            else:
                result.append(mid[::-1])
        return result