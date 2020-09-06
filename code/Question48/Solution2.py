'''
动态规划
dp[j] 代表以字符 s[j] 为结尾的 “最长不重复子字符串” 的长度
固定右边界 j ，设字符 s[j] 左边距离最近的相同字符为 s[i] ，即 s[i] = s[j] 
1.当 i < 0 ，即 s[j] 左边无相同字符，则 dp[j] = dp[j-1] + 1；
2.当 dp[j - 1] < j - i ，说明字符 s[i] 在子字符串 dp[j-1] 区间之外 ，则 dp[j] = dp[j - 1] + 1；
3.当 dp[j - 1] ≥ j−i ，说明字符 s[i] 在子字符串 dp[j-1] 区间之中 ，则 dp[j] 的左边界由 s[i] 决定，即 dp[j] = j - i；
当 i < 0 时，由于 dp[j - 1] ≤j 恒成立，因而 dp[j - 1] < j−i 恒成立，因此分支 1. 和 2. 可被合并。
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/mian-shi-ti-48-zui-chang-bu-han-zhong-fu-zi-fu-d-9/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #存储字符位置索引的字典
        dic = {}
        #最大值 存储每轮最大的dp[j]值
        maxVal = tmp = 0
        for j in range(len(s)):
            #寻找对应字符的索引值，没有则返回-1
            i = dic.get(s[j],-1)
            #更新索引值
            dic[s[j]] = j
            #更新dp[j]
            tmp = tmp+1 if tmp < j-i else j-i
            #更新最大值
            maxVal = max(tmp,maxVal)
        return maxVal