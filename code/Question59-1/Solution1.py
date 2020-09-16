'''
暴力遍历 逐个窗口判断 效率低 数据量大容易超时
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def maxNum(head,end,nums):
            maxnum = nums[head]
            for i in range(head+1,end+1):
                if nums[i] > maxnum:
                    maxnum = nums[i]
            return maxnum
        if not nums:
            return nums
        res = []
        for i in range(len(nums)-k+1):
            b = maxNum(i,i+k-1,nums)
            res.append(b)
        return res
'''
暴力遍历的优化版本
https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/pythonti-jie-shuang-100-by-xiao-xue-66/
'''
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        #双指针初始化为第二个窗口的起始值
        i,j = 1,k
        #先统计第一个窗口的最大值
        maxNum = max(nums[:k])
        res = [maxNum]
        while j<len(nums):
            #最大值滑出窗口 则重新统计当前窗口最大值
            if maxNum == nums[i-1]:
                maxNum = max(nums[i:j+1])
                res.append(maxNum)
            #如果新的数大于最大值 则更新最大值
            elif maxNum < nums[j]:
                maxNum = nums[j]
                res.append(maxNum)
            #如果新的数小于等于最大值 则最大值保持不变
            else:
                res.append(maxNum)
            i+=1
            j+=1
        return res