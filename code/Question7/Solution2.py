'''
也是利用前序遍历和中序遍历的特点，利用栈而非递归重建二叉树，参考leetcode 32ms时标准题解
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionPractice:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        center = preorder[0]
        length = len(preorder)
        root_node = TreeNode(center)
        stack = []
        stack.append(root_node)
        boundary_index = 0

        for i in range(1,length):
            preorderval = preorder[i]
            node = stack[-1]
            if node.val != inorder[boundary_index]: # 每次比较栈顶元素和inorder[index]
                node.left = TreeNode(preorderval)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[boundary_index]: # 栈顶元素等于inorder[index],弹出；并且index += 1
                    node = stack[-1]
                    stack.pop()
                    boundary_index+=1
                node.right = TreeNode(preorderval)
                stack.append(node.right)
        return root_node