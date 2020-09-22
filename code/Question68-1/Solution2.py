'''
针对当前节点 有三种情况 
1.两个节点比当前节点值大 则两个节点在当前节点的右子树
2.两个节点比当前节点值小 则两个节点在当前节点的左子树
3.若不符合以上两种情况 则说明两个节点分别在左，右子树 则当前节点就是我们要找的祖先节点
参考 
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-i-er-cha-sou-suo-shu-de-zui-jin-g-7/
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #两个节点都在左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        #两个节点都在右子树
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        #否则就是我们要找的节点
        return root
'''
非递归
'''
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root