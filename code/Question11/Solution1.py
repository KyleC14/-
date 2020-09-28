'''
从右到左暴力循环，直至当前元素比前一个元素小，返回当前元素
'''

class Solution:
    def minArray(self, numbers: List[int]) -> int:
    	#如果数组没有旋转 直接返回第一个
        if numbers[0]<numbers[-1]:
            return numbers[0]
        if numbers:
            for i in range(len(numbers)-1,-1,-1):
                if numbers[i]<numbers[i-1]:
                    return numbers[i]
            return numbers[0]
        return None