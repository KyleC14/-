'''
先序遍历
递归统计计算并更新最大层数
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth = self.k = 0
        def preOrder(root):
            self.k += 1
            if root:
                self.maxDepth = max(self.k,self.maxDepth)
                preOrder(root.left)
                self.k-=1
                preOrder(root.right)
                self.k-=1
            return
        preOrder(root)
        return self.maxDepth