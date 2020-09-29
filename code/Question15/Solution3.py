'''
巧用n&(n-1)
n-1会使得n最右的1变为0，此1后面的0变为1
n&(n-1)会使得最右的1变为0，其余不变
每次标志位加1
当n归零时跳出
https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n-1
        return count