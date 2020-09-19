'''
暴力遍历 探寻每一天买入然后卖出的价格和 寻找最大值
超时 199 / 200 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>maxProfit:
                    maxProfit = prices[j]- prices[i]
        return maxProfit