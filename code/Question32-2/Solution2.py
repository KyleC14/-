'''
改进写法 直接利用range的特性 每次第一次range()展开的长度都是每一层的长度
参考 https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/solution/mian-shi-ti-32-ii-cong-shang-dao-xia-da-yin-er-c-5/
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            #对于 python ，range() 的工作机制是在开启循环时建立一个列表，然后循环按照这个列表进行，因此“只会在进入循环前执行一次 len(queue) ” ；
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res