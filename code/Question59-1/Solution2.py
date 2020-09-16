'''     
双端队列 滑动窗口 详细参考链接或者剑指offer书本
参考 https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/python3-jian-ming-shi-xing-dai-ma-dai-zhu-shi-jie-/
'''
from collections import deque
class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i in range(len(nums)):
            #如果新的数比前一个数大 则前一个数不可能为最大值 弹出
            while queue and nums[i]>nums[queue[-1]]:
                queue.pop()
            #加入新的数 比前一个数小也没关系 因为随着窗口滑动这个新的数依然可能为最大值
            queue.append(i)
            #如果头部数超出窗口范围则弹出
            if i-queue[0]>k-1:
                queue.popleft()
            #记录最大数 保证队列最前端为最大值
            if i>=k-1:
                res.append(nums[queue[0]])
        return res