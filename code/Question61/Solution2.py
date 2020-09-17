'''
核心思想 max-min<5 如果符合这个条件则返回True 原理是如果数组全部是连续的 则必然max-min<5 不用关心0 0可以用来填充
参考
https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
'''
'''
集合set+遍历 （不用排序）
set记录出现的数字 防止重复 遍历寻找最大值与最小值 最后条件判断
'''
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        maxNum,minNum = 0,14
        for i in nums:
            #跳过大小王
            if i == 0:
                continue
            #不能有重复
            if i in repeat:
                return False
            repeat.add(i)
            maxNum = max(i,maxNum)
            minNum = min(i,minNum)
        return maxNum-minNum < 5
'''
排序后寻找最大值和最小值进行条件判断
'''
class Solution2:
    def isStraight(self, nums: List[int]) -> bool:
        #不要写成 nums = nums.sort()
        nums.sort()
        index = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                index+=1
            elif nums[i]==nums[i+1]:
                return False
        return nums[4]-nums[index]<5