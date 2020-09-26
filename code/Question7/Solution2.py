'''
前序遍历，从根节点root开始，只要有左子节点，就一直会往左下方走，直到最左下角。 而中序遍历，是从最左下角往上（示例中的4-5-8-9-3），如果碰到节点有右子节点，则会转向（示例中的8-10）。

因此，代码中的if块是用前序数组一直构建左子树，如果碰到了inorder[inorderIndex]，表示到了左下角，这时就需要往上走并处理右子树，也就是while代码块。
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