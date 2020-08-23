'''
从要弹出的元素开始，查找要弹出的元素是否在栈中，是则弹出栈顶元素，栈顶元素等于要弹出元素则弹出，并继续循环，否则返回False
若要弹出元素不在栈中，则查找起是否在pushed列表中，否则返回False
是则压入包括该元素与之前的所有元素，继续循环
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ps = 0
        pp = 0
        while pp!=len(popped):
            if popped[pp] in stack:
                if stack.pop() == popped[pp]:
                    pp+=1
                else:
                    return False
            elif popped[pp] in pushed:
                index = pushed.index(popped[pp])
                for i in range(ps,index+1):
                    stack.append(pushed[i])
                ps = index+1
            else:
                return False
        return True