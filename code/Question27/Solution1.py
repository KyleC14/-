'''
递归交换每一个节点的左右节点
Python 利用平行赋值的写法（即 a, b = b, aa,b=b,a ），可省略暂存操作。其原理是先将等号右侧打包成元组 (b,a)(b,a) ，再序列地分给等号左侧的 a, ba,b 序列。
'''
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root != None:
            root.left,root.right = root.right,root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
            return root
        return root
# 小修改 交换节点和递归代码可以合并
class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root != None:
            root.left,root.right = self.mirrorTree(root.right),self.mirrorTree(root.left)
        return root