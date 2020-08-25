'''
奇偶逻辑拆分 去掉判断的冗余性 
参考 https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result,queue = [],deque()
        queue.append(root)
        while queue:
            mid = []
            #先从奇数层开始
            for _ in range(len(queue)):
                node = queue.popleft()
                mid.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(mid)
            mid = []
            if not queue:break
            for _ in range(len(queue)):
                node = queue.pop()
                mid.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            result.append(mid)
        return result