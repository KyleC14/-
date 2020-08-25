'''
双端队列 奇数则添加到队列头部 偶数则添加到队列尾部 
参考 https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
需要判断每个节点的所在层奇偶性，即冗余了 N 次判断。
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result,queue = [],deque()
        queue.append(root)
        while queue:
            mid = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                #利用结果数组的长度来判断是第几层
                #需要判断每个节点的所在层奇偶性，即冗余了 N 次判断。
                if len(result)%2 == 1:
                    mid.appendleft(node.val)
                else:
                    mid.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(mid))
        return result