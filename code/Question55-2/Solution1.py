'''
利用先序遍历 逐个检查每个节点的左右子树是否为平衡树 存在重复遍历存在节点的问题
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #获取节点深度
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left,right)+1
        #先序遍历非递归写法 逐个节点判断左右子树是否为平衡树
        stack = []
        while stack or root:
            while root:
                left = depth(root.left)
                right = depth(root.right)
                if abs(left-right) > 1:
                    return False
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return True
'''
递归写法参考leetcode
https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
'''
class Solution2:
    #获取当前节点深度
    def depth(self,root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1
    #判断当前节点的子树是否为平衡树
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        #当前节点的左右子树是否符合平衡树
        #递归判断当前节点的左节点和右节点
        return abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)