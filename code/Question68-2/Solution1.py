'''
对于非二叉搜索数 上一题同样方法可以适用 本质应该算DFS
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