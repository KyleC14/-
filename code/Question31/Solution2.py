'''
持续压入元素，每压入一个元素对比要弹出的元素，若等于要弹出的元素则弹出元素，并对比当前栈顶元素是否等于要弹出元素，是则继续弹出，否则继续压入元素
直到压入全部元素，若栈为空，则返回True；若栈非空，则返回Fasle
参考 https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/ 
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,i = [],0
        for num in pushed:
            stack.append(num)
            #此处检查stack非空即时终止条件，也有效防止弹出最后一个元素后访问越界
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i+=1
        return not stack