'''
二分法 
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-by-leetcode-s/
'''

class Solution:
    def minArray(self,numbers: List[int]) -> int:
        if numbers:
            #如果数组没有旋转 直接返回第一个
            if numbers[0]<numbers[-1]:
                return numbers[0]
            else:
                #二分法
                left = 0
                right = len(numbers)-1
                while left<right:
                    mid = left+(right-left)//2
                    #当mid>最右，证明mid在左序列，而结果在mid右边，mid不可能是结果
                    if numbers[mid]>numbers[right]:
                        left = mid+1
                    #当mid<最右，证明mid在右序列，而结果在mid左边，mid可能是结果
                    elif numbers[mid]<numbers[right]:
                        right = mid
                    #当mid=最右，无法判断结果在左还是右，缩减范围，由于至少有两个与mid相同的值，不影响结果查找
                    elif numbers[mid] == numbers[right]:
                        right -=1
                return numbers[left]
        return None