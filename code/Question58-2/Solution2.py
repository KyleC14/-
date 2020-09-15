'''
三次翻转 要得到 abcdef -> cdef ab
ba fedc -> bafedc
-> cdefab
最优空间复杂度O(1)
'''
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        #进行区间内翻转
        def reverse(head,end):
            while head <= end:
                s[head], s[end] = s[end], s[head]
                head += 1
                end -= 1
            return
        s = list(s)
        reverse(0,n-1)
        reverse(n,len(s)-1)
        reverse(0,len(s)-1) # s = s[::-1]
        return ''.join(s)