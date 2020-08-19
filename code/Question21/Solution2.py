'''
只找奇数，然后从第一位开始交换
'''
class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
        return nums