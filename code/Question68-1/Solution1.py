'''
用先序遍历获取到两个节点的路径序列 然后返回最后一个相同节点值即为公共祖先 
缺点：这种方法没有用到二叉搜索树的有序特性
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def preOrder(root,stopNode,res):
            if not root or self.flag:
                return
            res.append(root)
            if root == stopNode:
                self.flag = True
                return
            preOrder(root.left,stopNode,res)
            if self.flag:
                return
            preOrder(root.right,stopNode,res)
            if self.flag:
                return
            res.pop()
            return
        self.flag = False
        self.p_list = []
        self.q_list = []
        preOrder(root,p,self.p_list)
        self.flag = False
        preOrder(root,q,self.q_list)
        sameNode = root
        end = len(self.p_list) if len(self.p_list)<len(self.q_list) else len(self.q_list)
        for i in range(end):
            if self.p_list[i] == self.q_list[i]:
                sameNode = self.p_list[i]
        return sameNode