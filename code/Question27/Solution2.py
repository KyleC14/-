'''
非递归 利用栈（或队列）遍历树 同样交换左右节点
这里顺序不是最关键的 关键是要遍历每一个节点 并交换其左右节点
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/
'''
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root