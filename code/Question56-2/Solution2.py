'''
如果一个数字出现三次，那么它的二进制上的每一位加起来的和都能被三整除
把数组中所表示的每一都加起来，如果该和能被3整除，那么只出现一次的数字这一位就为0，否则为1
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        for num in nums:
            index = 1
            for i in range(32):
                if num&index != 0:
                    count[i]+=1
                index = index << 1
        result = 0
        for i in range(len(count)):
            if count[i]%3 != 0:
                result += 2**i
        return result