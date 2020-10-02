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

'''
Solution1 dfs的拓展
这版代码易于理解
'''
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(A,B):
            if not A and not B:
                return True
            elif not A or not B:
                return False
            return A.val == B.val and dfs(A.left,B.right) and dfs(A.right,B.left)
        if not root:
            return True
        return dfs(root.left,root.right)