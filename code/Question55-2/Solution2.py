'''
利用后序遍历(优点在于可以至下而上 不会重复遍历遍历过的节点) 从叶子的节点开始逐层往上累加判断 并且累加计算高度 如果有一个节点不符合平衡树判断则终止过程
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #标记是否提前终止的符号
        self.flag = True
        def postOrder(root):
            if not root:
                return 0
            left = postOrder(root.left)
            if not self.flag: return
            right = postOrder(root.right)
            if not self.flag: return
            #left,right之后只要一个判断也行 多一个判断可以提前剪枝
            if abs(left-right) <= 1:
                return max(left,right)+1
            self.flag = False
            return
        postOrder(root)
        return self.flag

'''
更优雅一点的写法
参考 https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
'''
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        def postOrder(root):
            if not root:
                return 0
            left = postOrder(root.left)
            if left == -1:return -1
            right = postOrder(root.right)
            if right == -1:return -1
            if abs(left-right)<=1:
                return max(left,right)+1
            return -1
        return postOrder(root) != -1