'''
动态规划
f(n,k) 表示n个骰子点数和为k时出现的次数
f(n,k)=f(n−1,k−1)+f(n−1,k−2)+f(n−1,k−3)+f(n−1,k−4)+f(n−1,k−5)+f(n−1,k−6)
初始化
f(1,1)=f(1,2)=f(1,3)=f(1,4)=f(1,5)=f(1,6)=1
参考：
https://www.cnblogs.com/wangkundentisy/p/9378886.html
'''
class Solution:
    def twoSum(self, n: int) -> List[float]:
        #确定和的范围
        start,end = n,n*6
        #总的排列组合的次数
        total = 6**n
        #动态规划的两个数组
        #A 1~6 为初始化数据
        #方便写代码 从1开始算
        A = [0]+[1]*6+[0]*(end-6)
        B = [0]+[0]*end

        #N个骰子要进行n-1次计算
        for _ in range(n-1):
            for i in range(1,end+1):
                for j in range(1,7):
                    if i-j>0:
                        B[i] += A[i-j]
            A = list(B)
            B = [0]+[0]*end
        res = A[start:end+1]
        for i in range(len(res)):
            res[i] /= total
        return res