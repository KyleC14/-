'''
直球思路 检测数字出现的次数是否超过一半 不检测重复数字
笨比做法 即使不检测重复数字 还是要遍历数组统计次数
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count(val):
            re = 0
            for i in nums:
                if i==val:
                    re+=1
            return re
            return
        limit = len(nums)//2
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                time = count(nums[i])
                if time > limit:
                    return nums[i]
        return
#提高检索效率
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        def count(val):
            re = 0
            for i in nums:
                if i==val:
                    re+=1
            return re
            return
        #set()效率高
        dic = set()
        limit = len(nums)//2
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic.add(nums[i])
                time = count(nums[i])
                if time > limit:
                    return nums[i]
        return