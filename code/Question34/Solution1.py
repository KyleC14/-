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