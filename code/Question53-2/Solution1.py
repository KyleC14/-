'''
遍历 查找出第一个与下标不相同的数 不是最佳做法
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i+1