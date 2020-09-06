'''
动态规划
https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
当一个丑数都经历过*2 *3 *5 那么它对于产生新的丑数就没有作用了
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        #*2 *3 *5 的指针
        a = b = c = 0
        for i in range(1,n):
            n1,n2,n3 = dp[a]*2,dp[b]*3,dp[c]*5
            dp[i] = min(n1,n2,n3)
            #三个指针都要检查 为了去重
            if dp[i] == n1:
                a+=1
            if dp[i] == n2:
                b+=1
            if dp[i] == n3:
                c+=1
        return dp[-1]