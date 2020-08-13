''' 
不考虑大数问题，直接循环打印
'''
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result = []
        for i in range(1,10**n):
            result.append(i)
        return result