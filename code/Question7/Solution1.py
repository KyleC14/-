'''
根据前序遍历的特点（第一个为根节点）和中序遍历的特点（根节点左边为左子树，右边为右子树），递归重建二叉树
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0 or len(inorder)==0:
            return None
        center = preorder[0]
        #当前序号代表当前节点的左子树节点有几个
        index = inorder.index(center)
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[1:1+index]
        preorder_right = preorder[1+index:]
        Node = TreeNode(center)
        Node.left = self.buildTree(preorder_left,inorder_left)
        Node.right = self.buildTree(preorder_right,inorder_right)
        return Node