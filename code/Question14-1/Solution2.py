'''
思路2大致与思路1一致，只不过把两个特殊长度包含到了计算处理中。
设第一段绳子长度为i，第二段绳子长度为n-i。第一端的最大乘积为max(result[i],i)即继续剪和不剪的最大值。同理第二段的最大乘积为max(result[n-j],n-j)。

'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        #存储结果
        result = [0]*(n+1)
        result[1] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                #第一段j,继续剪与不剪取最大值
                #第二段i-j,继续剪与不剪取最大值
                tmp = max( result[j],j)*max( result[i-j],i-j)
                #这里与result[i]比较为更新最大值
                result[i] = max(result[i],tmp)
        return result[n]