'''
利用与运算与无符号右移
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count