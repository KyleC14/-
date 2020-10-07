'''
按照先序遍历的方式遍历二叉树，使用path列表记录复合要求的路径，每次回溯上层时删除当前节点路径

还有BFS方式 参照 https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/san-chong-fang-fa-dfs-bfs-hui-su-di-gui-die-dai-by/
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root,sum):
            path.append(root.val)
            nextsum = sum-root.val
            if nextsum == 0 and not root.left and not root.right:
                #记录路径时若直接执行 res.append(path) ，则是将 path 对象加入了 res ；后续 path 改变时， res 中的 path 对象也会随之改变。
                #或者使用深拷贝
                result.append(list(path))
            if root.left:
                dfs(root.left,nextsum)
            if root.right:
                dfs(root.right,nextsum)
            path.pop()
            return
        if not root:
            return []
        result = []
        path = []
        dfs(root,sum)
        return result
'''
改良版
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        def dfs(root,arr,total):
            #确保到达叶子节点并且符合目标
            if sum - total == 0 and not root.left and not root.right:
                self.res.append(arr)
                return
            if root.left:
                dfs(root.left,arr+[root.left.val],total+root.left.val)
            if root.right:
                dfs(root.right,arr+[root.right.val],total+root.right.val)
            return
        if not root:
            return self.res
        dfs(root,[root.val],root.val)
        return self.res