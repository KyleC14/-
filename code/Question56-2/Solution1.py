'''
哈希表记录数字的出现次数 空间换时间
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = False
            else:
                dic[i] = True
        for i in dic:
            if dic[i] == True:
                return i