'''
统计每一位上出现1的可能性
参考: https://www.bilibili.com/video/BV1uJ411573j/ https://www.youtube.com/watch?v=uB7DfQul6GU
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        n_str = str(n)
        n_str = n_str[::-1]
        count = 0
        for i in range(len(n_str)):
            #下界
            count += n//(10**(i+1))*(10**i)
            dig = int(n_str[i])
            #上界 分三种情况 当前位数字>1,=1,=0(等于0时数量也为0)
            if dig > 1:
                count+=10**i
            elif dig == 1:
                count+=n%(10**(i))+1
        return count