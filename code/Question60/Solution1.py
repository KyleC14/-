'''
递归求解 超时 9 / 11 
每次把n个骰子分成两堆 1堆只有1个，另一堆n-1个
计算第一堆1~6每一种点数与剩下n-1个骰子的点数和
相当于用递归方式计算所有点数出现的次数，最后除以总的排列组合总数
'''
class Solution:
    def twoSum(self, n: int) -> List[float]:
        def sumTotal(sum,time):
            if time == 0:
                res[sum-start]+=1
                return
            for i in range(1,7):
                sumTotal(sum+i,time-1)
            return
        #确定和的范围
        start,end = n,n*6
        #总的排列组合的次数
        total = 6**n
        res = [0]*(end-start+1)
        sumTotal(0,n)
        for i in range(len(res)):
            res[i] /= total
        return res