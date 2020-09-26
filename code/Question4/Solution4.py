'''
二分查找 这题用二分其实很麻烦 要思考很久的边界条件 因为并非一维数组 要以范围包括的思想来考虑
参考leetcode题解
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        #从右上角开始
        x,y = 0,len(matrix[0])-1
        #在二维数组内的范围查找
        while x < len(matrix) and y >=0:
            #如果范围缩窄到第一行并且目前范围内最小的数依然大于target 返回False
            if y == 0 and matrix[x][0] > target:
                return False
            #行二分查找的范围
            left,right = 0,y
            #在行的二分 目的是找出列的起始数 小于等于 target 因为这是最小的数 如果大于 target 则此列不存在目标数
            while left < right:
                #注意这里由于规定left 等于 mid 所以默认mid的位置要给到右边 否则容易出现死循环
                mid = left + (right - left + 1)//2
                if matrix[x][mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            #已经确定完列的范围
            y = left
            #如果范围缩窄到最后一行 并且目前范围最大的数依然小于target 返回False
            if x == len(matrix)-1 and matrix[x][y] < target:
                return False
            #列二分查找的范围
            left = x
            right = len(matrix)-1
            #在列的二分 为了确定行的的范围 目的为了找出此行的终止数 这是最大的数 如果小于target 则此行不存在target
            while left<right:
                #这里同理
                mid = left + (right - left)//2
                if matrix[mid][y] >= target:
                    right = mid
                else:
                    left = mid + 1
            x = right
            if matrix[x][y] == target:
                return True
        return False