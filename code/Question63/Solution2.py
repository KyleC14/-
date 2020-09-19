'''
遍历数组 假设当前是卖出价 只需要记录之前的的最小值就可以了
也是一种动态规划 
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))
'''
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        #只有1天或者0天
        if len(prices)<2:
            return 0
        #记录之前的最小值
        minNum = prices[0]
        #最大利润
        maxNum = 0
        for i in range(1,len(prices)):
            maxNum = max(maxNum,prices[i]-minNum)
            minNum = min(minNum,prices[i])
        return maxNum