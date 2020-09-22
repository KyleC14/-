'''
参考
https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #遇到空节点或者目标节点则返回
        if not root or root == p or root == q:
            return root
        #左子树的递归展开
        left = self.lowestCommonAncestor(root.left,p,q)
        #右子树的递归展开
        right = self. lowestCommonAncestor(root.right,p,q)
        #如果两个结果都为空 则说明不存在公共节点(两个目标节点都不在二叉树中)
        #这里的判断可以省略 融合到下面的判断条件中
        # if not left and not right:
        #     return
        #如果左空 右不空
        if not left:
            return right
        if not right:
            return left