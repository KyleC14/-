'''
设置上下左右四条边界 动态调整四条边界
参考 https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        left,top,right,bottom = 0,0,len(matrix[0])-1,len(matrix)-1
        result = []
        while True:
            #从左到右
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top +=1
            #从上到下
            if top>bottom:break
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1
            #从右到左
            if left>right:break
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
            if top>bottom:break
            #从下到上
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
            if left>right:break
        return result