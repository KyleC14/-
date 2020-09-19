'''
详见
https://blog.csdn.net/u011500062/article/details/72855826
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        last = 0
        for i in range(2,n+1):
            last = (last+m)%i
        return last