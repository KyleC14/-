'''
运用递归思想 
遍历A树的每个节点，从每个节点检查是否存在B树的结构 （根、左、右 先序遍历）
检查子结构的时候同样运用递归的思想，每次检查一个节点，然后递归检查剩下的节点
'''
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A,B):
            #B树已经全部检查完毕 无论A树是否为None 此时结果为True
            if B == None:
                return True
            #A树已经全部检查完毕 B树不为None 此时已经不可能存在子结构 返回False
            if A == None:
                return False
            return A.val == B.val and dfs(A.left,B.left) and dfs(A.right,B.right)
        #A树为None,不可能存在子结构 B树为None,规定空树不为任何树的子结构
        if A == None or B == None:
            return False
        return dfs(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)