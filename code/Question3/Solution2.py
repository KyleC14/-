#以空间换时间，建立一个n-1大小（也可以是原数组的最大值）的数组，然后遍历原数组，如果每个数加一，如果存在重复数，则必然大于1，大于1时输出该数

class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        checkList = []
        for i in range(0,max(nums)+1):
            checkList.append(int(0))
        for i in nums:
            checkList[i] += 1
            if checkList[i]>1:
                return i
        return -1