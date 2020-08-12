'''
二进制转换 统计1的个数
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            res = n%2
            n = n//2
            if res == 1:
                count +=1
        return count