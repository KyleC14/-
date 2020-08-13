'''
参考leetcode题解
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
'''

class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            # 递归终止
            if x == n:
                #从标志位开始组合字符串
                s = ''.join(num[self.start:])
                #排除结果数组中第一个0
                if s != '0':
                    # res.append(s)
                    #为了通过题目，实际代码应该为上一句
                    res.append(int(s))
                #当条件触发，即需要进位时，标志位减少一位
                if n-self.start == self.nine:
                    self.start-=1
                return
            else:
                #遍历0到9
                for i in range(10):
                    #遇到9时，计数器加一位
                    if i == 9:
                        self.nine +=1
                    #转成字符串
                    num[x] = str(i)
                    #递归开始下一位定位
                    dfs(x+1)
                #回溯9的数量
                self.nine -= 1
        #用于全排列的数组
        num = ['0']*n
        #存储结果数组
        res = []
        #统计当前全排列数组里有多少个9 与start联动 当 n-self.start = self.nine时，start需要减少一位
        #初始nine的数量为0
        self.nine = 0
        #初始start标志位为最后一位
        self.start = n-1
        #从第一位数开始递归
        dfs(0)
        # 实际用逗号连接，返回结果 适用于15行一同解开注释
        # return ','.join(res)
        return res