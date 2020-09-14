'''
双指针 pA定位到单词前的第一个空格 pB定位到单词的最后一个字符
参考 https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/mian-shi-ti-58-i-fan-zhuan-dan-ci-shun-xu-shuang-z/
'''
class Solution3:
    def reverseWords(self, s: str) -> str:
        #去掉首尾空格
        s = s.strip()
        res = []
        pA = pB = len(s)-1
        #注意这里pA 大于等于号 注意思考开头的情况（开头可以是一个单词 也可以是只有一个字母）
        while pA>=0:
            while pA >=0 and s[pA] != " ":
                pA -= 1
            res.append(s[pA+1:pB+1])
            pB = pA
            while s[pB] == " ":
                pB -=1
            pA = pB
        return " ".join(res)