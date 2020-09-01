'''
规律（动态规划）
逐个加数字 在当前和为负数时，加上下一个数的和一定会会比当前和小 因此在这种情况下抛弃之前的和 从下一位数开始重新计算
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        addsum  = 0
        maxSum = nums[0]
        for i in nums:
            if addsum<=0:
                addsum = i
            else:
                addsum+=i
            if addsum>maxSum:
                maxSum = addsum
        return maxSum