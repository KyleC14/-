
'''
动态规划做法 参考 https://www.bilibili.com/video/BV1Tt4y1U7QP
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #初始化动态规划数组
        dp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        #对第一列做特殊处理 针对 s=None p='*'可以匹配
        for i in range(1,len(p)):
            dp[i+1][0] = dp[i-1][0] and p[i] == "*"
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i-1][j+1]
                    if s[j] == p[i-1] or p[i-1] == '.':
                        dp[i+1][j+1] = dp[i+1][j+1] or dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]