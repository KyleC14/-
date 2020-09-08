'''
稍微优化一下 没必要全部遍历完 只遍历到第k大的数就好了
'''
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        result = []
        def order(root):
            if root:
                order(root.right)
                #达成提前返回的关键
                if len(result) == k:
                    return
                else:
                    result.append(root.val)
                order(root.left)
            return
        order(root)
        return result[-1]
'''
空间还可以进一步优化 只记录最大的数
参考：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
'''
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def order(root):
            if root:
                order(root.right)
                #达成提前返回的关键
                if self.k == 0:
                    return
                else:
                    self.k -= 1
                    self.res = root.val
                order(root.left)
            return
        order(root)
        return self.res
'''
非递归实现
'''
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        k = k
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            if k == 0:
                break
            else:
                res = root.val
                k -= 1
            root = root.left
        return res