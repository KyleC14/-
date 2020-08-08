'''
动态规划，长度为n的绳子，第一刀第一段绳子的可能长度为1-n-1。令最大乘积为f(n),
f(n)=max(f(i)*(n-1)),i从1遍历至n-1。有两个特殊长度，2与3。当绳子长度为2,3时，返回结果应为1,2。但对于后续结果而言，实际这两个长度不继续剪获得的乘积更大。因此结果存储数组对应存储为2,3，而不是1,2

'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        #存储结果
        result = [0 for i in range(n+1)]
        #这里并不是长度2,3绳子剪切后的最大乘积，因为实际不剪值更大，长度2，3为特殊值
        result[1],result[2] = 1,2
        if n > 2:
            result[3] = 3
        #长度为2,3直接返回实际情况
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            #实际只有长度2,3是不剪值最大，其他长度的绳子一定是剪后乘积最大
            for i in range(4,n+1):
                max = 0
                for j in range(1,i//2+1):
                    if max < result[j]*result[i-j]:
                        max = result[j]*result[i-j]
                result[i] = max
        return result[n]