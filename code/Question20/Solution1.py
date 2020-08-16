'''
参考剑指offer书解答
数值字符串的格式
A[.[B]][e|EC] or .B[e|EC]
A和C部分允许出现正负号 C部分不允许出现正负号 因此A、C调用扫描有符号数函数，B调用扫描无符号数函数
数字范围为0-9
大前提 凡是要访问字符串元素必须保证不越界
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        def scanUnsignedInteger():
            #记录初始指针位置
            before = self.start
            #确保连续都是数字 如果有非数字 会马上跳出 函数结束后指针位置会不对
            while self.start<len(s) and s[self.start]>='0' and s[self.start]<='9':
                self.start+=1
            return self.start>before

        def scanInteger():
            #扫描有符号数 本质就是处理 正负号
            #遇到'+/-'指针加1，但是只做一次判断 因为符号只能出现一次
            if self.start<len(s) and (s[self.start] == '+' or s[self.start] == '-'):
                self.start+=1
            #处理完正负号 开始扫描数字
            return scanUnsignedInteger()

        #去掉头尾空格 中间的空格不能去掉
        s = s.strip()
        #如果为空字符串 直接返回结果
        if not s:
            return False
        #字符串指针
        self.start = 0
        #扫描A部分
        result = scanInteger()
        #扫描小数部分
        if self.start<len(s) and s[self.start] == '.':
            self.start += 1
            #这里使用or 是因为A、B两部分可以任一不存在 .1  9. 都算数字
            result = scanUnsignedInteger() or result
        #扫描指数部分
        if self.start<len(s) and (s[self.start] == 'e' or s[self.start] == 'E') :
            self.start+=1
            #这里使用and 是为因为指数前面部分不能没有数字
            result = result and scanInteger()
        #确保指针走完整个字符串
        return result and self.start == len(s)