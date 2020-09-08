'''
对于二叉搜索树 根据右，根，左的顺序遍历(中序遍历的逆序)便可获得有序数组 返回对应数字即可
'''
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        result = []
        def order(root):
            if root:
                order(root.right)
                result.append(root.val)
                order(root.left)
            return
        order(root)
        return result[k-1]
'''
中序逆序遍历的非递归实现
'''
class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            result.append(root.val)
            root = root.left
        return result[k - 1]