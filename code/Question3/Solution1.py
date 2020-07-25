#数组先进行排序，然后遍历，如果相邻两位数相同，则重复
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if i != len(nums)-1:
                if nums[i] == nums[i+1]:
                    return nums[i]
            else:
                return -1
