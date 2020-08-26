'''
观察后序遍历可知，列表最后一位一定为根节点，从开头开始元素分为两种，一种比根节点小，一种比根节点大，因此可以采用递归的方法
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        i = 0
        while i<len(postorder)-1:
            if postorder[i]<postorder[-1]:
                i+=1
            else:
                break
        j = i
        while j<len(postorder)-1:
            if postorder[j]>postorder[-1]:
                j+=1
            else:
                break
        #如果当前递归序列正确 j必定指向最后一位元素
        return j == len(postorder)-1 and self.verifyPostorder(postorder[:i]) and self.verifyPostorder(postorder[i:len(postorder)-1])
'''
剑指上的递归
'''
class Solution2:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        last = len(postorder)-1
        i = 0
        #i定位到比根节点大的元素位置
        while i<last:
            if postorder[i]<postorder[last]:
                i += 1
            else:
                break
        j = i
        while j<last:
            #如果遇到元素比根节点大直接返回False
            if postorder[j]<postorder[last]:
                return False
            j+=1
        re1 = re2 = True
        # if i>0:
        re1 = self.verifyPostorder(postorder[:i])
        # if i<last:
        re2 = self.verifyPostorder(postorder[i:j])
        return re1 and re2