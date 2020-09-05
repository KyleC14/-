'''
其实等同于青蛙跳台阶的思路
f(n)=f(n-1)+f(n-2) 当两个字符可翻译，
f(n) = f(n-1) 当两个字符不可翻译
关于ASCII码的转换 https://blog.csdn.net/yzy_1996/article/details/89556049
'''
class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        num_str = str(num)
        for i in range(2,len(num_str)+1):
            #ASCII码对比只在两个字符时进行 形式为两个数的矩阵
            a,b = b,a+b if '10'<=num_str[i-2:i]<='25' else b
        return b
'''
如果逆序进行结果也是一致的 可以节省O(N)的空间
'''
class Solution2:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num%10
        while num!=0:
            num = num//10
            #取第二个数字
            x = num%10
            a,b = b,a+b if 10<=10*x+y<=25 else b
            y = x
        return b