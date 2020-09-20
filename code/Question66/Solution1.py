'''
遍历创建 超时 43 / 44 
O(n**2)
'''
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        B = []
        for i in range(len(a)):
            num = 1
            for j in range(len(a)):
                if j!=i:
                    num*=a[j]
            B.append(num)
        return B