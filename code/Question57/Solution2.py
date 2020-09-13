'''
头尾指针互相夹击 钳形战术
由于数组是有序的 当前两指针之和大于目标值时，尾指针进1，否则则头指针进1
尾指针与头指针不会后退 因为数组的有序性决定 之前元素已经检查过
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end = 0,len(nums)-1
        while start<end:
            if nums[start]+nums[end] == target:
                return [nums[start],nums[end]]
            elif nums[start]+nums[end]>target:
                end -= 1
            else:
                start+=1