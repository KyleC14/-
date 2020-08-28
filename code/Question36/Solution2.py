'''
递归写法
使用中序遍历链表 同时记录pre前驱节点和cur当前节点，每次修改pre.right和cur.left
当pre为空时，记录头节点，最后遍历完成，pre等于最后一个节点 此时修改头节点和pre节点的指针
'''
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre:
                self.pre.right,root.left = root,self.pre
            else:
                self.head = root
            self.pre = root
            dfs(root.right)
            return
        if not root:
            return root
        self.pre = None
        dfs(root)
        self.head.left,self.pre.right = self.pre,self.head
        return self.head