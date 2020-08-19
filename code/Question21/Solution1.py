'''
意义不是很大的写法，分别找出来分开再合并（应该限制在一个数组内操作）
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        oushu = []
        jishu = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                oushu.append(nums[i])
            else:
                jishu.append(nums[i])
        return jishu+oushu