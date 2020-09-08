'''
剑指offer书上的另一种做法 利用0~n-1与实际数组的和的差值即为缺失的数
等差数列求和 n(a1+an)/2
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        sum1 = (length+1)*(length)/2
        sum2 = sum(nums)
        return sum1-sum2