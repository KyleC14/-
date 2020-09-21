'''
从头开始遍历 分区判断
'''
class Solution:
    def strToInt(self, str: str) -> int:
        #去掉首尾空格
        str = str.strip()
        #如果字符串为空 只包含空格 返回0
        if len(str) == 0:
            return 0
        # 界限
        up = (2**31)-1
        down = -2**31
        #确定正负号标志
        flag = False if str[0] == '-' else True
        #开始位置
        start = 0
        if str[0] in '+-':
            start += 1
        #从左向右
        res = 0
        #遍历至最后一位数字
        for i in range(start,len(str)):
            #直到字符不在0~9中 跳出
            if not '0'<=str[i]<='9':
                break
            res = res*10 + ord(str[i])-ord('0') #ord()转换为ascii
        #根据正负号取值
        res = res if flag else -res
        #如果超出两个边界则返回对应边界值
        if res>up:
            return up
        elif res<down:
            return down
        return res