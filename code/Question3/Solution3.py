#关于0到n-1的数组，如果每个数都不同，那么每个数都会与下标相同。
#如果有重复的，那么有的下标会没有数，有的下标则会多出来数。
#从当前数组开始，与下标进行对比，如果相同，则跳至下一位。
#如果与当前下标不同，则把当前数与数组同数下标的数进行比较，如果相同，则有重复，如果不同，则交换两个数，重复以上循环操作。

class Solution3:
    def findRepeatNumber(self,nums:List[int]) -> int:
        for i in range(0,len(nums)):
            while i!=nums[i]:
                if nums[nums[i]] == nums[i]:
                    return b
                b = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = b
        return -1