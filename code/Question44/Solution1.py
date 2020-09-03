'''
1位数 1-9 数量：1*9
2位数 10-99 数量：2*90 = 99-10+1
3位数 100-999 数量：3*900

n位数 n*9*(10**n-1) 不同位数具有数字数量的规律
利用该规律找出所在区间，然后找出所对应数字，最后返回对应数字的位数
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        count = 9
        step = 1
        #找出在第几个区间
        while n>count:
            step += 1
            count+=step * 9 * int(10 ** (step - 1))
        #距离这个区间有多少位数
        res = n - (count-(step)*9*int(10**(step-1)))
        #代表这个区间第几个数字
        #num_index对应这个区间的第几个数
        #dig_index对应这个数字的第几位数
        if res%(step) == 0:
            num_index = res//step
            dig_index = step
        else:
            num_index = (res//step)+1
            dig_index = res%step
        # 起始点
        start = int(10**(step-1))-1
        #对应的数字
        num = str(start + num_index)
        #返回对应数字的位数
        return int(num[dig_index-1])