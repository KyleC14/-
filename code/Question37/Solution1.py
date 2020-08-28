'''
序列化即层次遍历 先层次遍历获取序列化
反序列化时同样运用层次化遍历的思想
'''
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return root
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
            else:
                result.append(str(None))
                continue
            queue.append(node.left)
            queue.append(node.right)
        return '['+','.join(result)+']'
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return data
        data = data[1:-1]
        vals = data.split(',')
        queue = deque()
        head = TreeNode(int(vals[0]))
        queue.append(head)
        i = 1
        #用回层次遍历的方法构建树
        while queue:
            node = queue.popleft()
            if vals[i] !='None':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            if vals[i] !='None':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i+=1
        return head
'''
严格序列化
'''
class Codec:
    def serialize(self, root):
        if not root:
            return root
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
            else:
                result.append(str(None))
                continue
            queue.append(node.left)
            queue.append(node.right)
        #去掉多余的None
        j = 0
        for i in range(len(result)-1,-1,-1):
            if result[i]!='None':
                j = i
                break
        result = result[:j+1]
        return '['+','.join(result)+']'

    def deserialize(self, data):
        if not data:
            return data
        data = data[1:-1]
        vals = data.split(',')
        vals_queue = deque()
        for i in vals:
            vals_queue.append(i)
        queue = deque()
        head = TreeNode(int(vals_queue.popleft()))
        queue.append(head)
        i = 1
        while vals_queue:
            node = queue.popleft()
            val = vals_queue.popleft()
            if val !='None':
                node.left = TreeNode(int(val))
                queue.append(node.left)
            if not vals_queue:
                break
            val = vals_queue.popleft()
            if val !='None':
                node.right = TreeNode(int(val))
                queue.append(node.right)
        return head