'''
逐个遍历 超时
'''
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
        return count