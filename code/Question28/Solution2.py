'''
利用先序遍历和修改的先序遍历做对比 剑指offer书上的思路
'''
class Solution:
    def preOr(self,root):
        if not root:
            self.prelist.append('None')
            return
        self.prelist.append(root.val)
        self.preOr(root.left)
        self.preOr(root.right)
    def repreOr(self,root):
        if not root:
            self.reprelist.append('None')
            return
        self.reprelist.append(root.val)
        self.repreOr(root.right)
        self.repreOr(root.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.prelist,self.reprelist = [],[]
        self.preOr(root)
        self.repreOr(root)
        if self.prelist == self.reprelist:
            return True
        else:
            return False
#修改一下代码
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def preOr(preList,root):
            if not root:
                preList.append('None')
                return preList
            preList.append(root.val)
            preList = preOr(preList,root.left)
            preList = preOr(preList,root.right)
            return preList
        def reOr(reList, root):
            if not root:
                reList.append('None')
                return reList
            reList.append(root.val)
            reList = reOr(reList,root.right)
            reList = reOr(reList,root.left)
            return reList
        if not root:
            return True
        preList,reList = [],[]
        preList,reList = preOr(preList,root),reOr(reList,root)
        if preList == reList:
            return True
        else:
            return False