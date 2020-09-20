'''
以矩阵的方式来构建数组 O(n)
参考下面的链接
'''
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return a
        C = [1]
        D = [1]
        k = len(a)-1
        for i in range(0,len(a)-1):
            C.append(C[i]*a[i])
            D.append(D[i]*a[k])
            k -= 1
        D = D[::-1]
        for j in range(len(C)):
            C[j] = C[j]*D[j]
        return C
'''
进一步进行空间优化为O(1)
参考：
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/
'''
class Solution2:
    def constructArr(self, a: List[int]) -> List[int]:
        B = [1]*len(a)
        tmp = 1
        #由上往下
        for i in range(1,len(a)):
            B [i] = B[i-1]*a[i-1]
        #由下往上
        for i in range(len(a)-2,-1,-1):
            tmp *= a[i+1]
            B[i] = B[i]*tmp
        return B