'''
结合27题和26题的思路，先获取镜像二叉树，然后递归遍历两个二叉树对比是否相同
最直观的思路
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(root):
            if not root:
                return root
            root.left,root.right = mirror(root.right),mirror(root.left)
            return root
        def dfs(A,B):
            if not A and not B:
                return True
            elif not A or not B:
                return False
            return A.val == B.val and dfs(A.left,B.left) and dfs(A.right,B.right)
        #注意深拷贝
        root2 = copy.deepcopy(root)
        root2 = mirror(root2)
        return dfs(root,root2)