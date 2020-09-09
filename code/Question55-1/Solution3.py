'''
剑指offer方法
一个节点的最大深度是 max(左节点深度，右节点深度)+1
采取递归思路
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def treeDepth(root):
            if not root:
                return 0
            left = treeDepth(root.left)
            right = treeDepth(root.right)
            return max(left,right)+1
        return treeDepth(root)