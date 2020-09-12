'''
从头开始异或 最后得到的结果必然是两个只出现一次的数的异或结果（位运算的魅力）
取结果为1的第n位为标准，为1的分到一组，相同的数必然都会分到一组
而只出现一次的两位数这一位必然不同，会分到不同的组
分别对两个组从头到尾异或，取其结果
'''
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #数组逐个异或
        re = 0
        for i in nums:
            re = re^i
        flag = 1
        while flag&re == 0:
            flag = flag << 1
        # index = 0
        #依据flag分组 实际没有必要
        # for i in range(len(nums)):
        #     if flag&nums[i] != 0:
        #         nums[index],nums[i] = nums[i],nums[index]
        #         index += 1
        # re = 0
        # res = []
        #获取结果
        # for i in range(len(nums)):
        #     re = re^nums[i]
        #     if i == index-1 or i == len(nums)-1:
        #         res.append(re)
        #         re = 0
        a = b = 0
        for i in nums:
            if i&flag == 0:
                a = a^i
            else:
                b = b^i
        return [a,b]

'''
leetcode题解
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/
'''
import functools
class Solution2:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #对数组逐个执行异或
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]