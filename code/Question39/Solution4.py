'''
利用字典达成“不耗费额外空间”的桶排序
字典的查找时间复杂度为O(1),所以总的时间复杂度为O(n),空间复杂度为O(n)
'''
class Solution5:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return nums
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
            if dic[i]>len(nums)//2:
                return i
        return