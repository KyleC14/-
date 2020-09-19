'''
模拟环形链表
超时  n = 70866  m = 116922
通过 26 / 36
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        head = 0
        while len(nums)!=1:
            for _ in range(m-1):
                head+=1
                if head == len(nums):
                    head = 0
            nums = nums[head+1:]+nums[:head]
            head = 0
        return nums[0]