'''
递归对比 最好对图理解 参考https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/
每一个节点需要对比三件事
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def rec(L,R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return rec(L.left,R.right) and rec(L.right,R.left)
        if not root:
            return True
        return rec(root.left,root.right)