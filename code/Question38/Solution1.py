''''' 
固定字符串的第一位，然后递归调用固定第二位，... 
当字符串中不存在重复字符时，可以获得全排列 
当字符串中存在重复字符时，全排列中会有重复结果 利用set()进行结果去重 
(直接获取全排列 最后使用list(set(result)也能达到去重结果 不必每次添加时判断) 
'''  
class Solution:  
    def permutation(self, s: str) -> List[str]:  
        def dfs(s_list):  
            for i in range(len(s_list)):  
                s_list[0],s_list[i] = s_list[i],s_list[0]  
                word.append(s_list[0])  
                if len(word) == len(s):  
                    if ''.join(word) not in dic:  
                        result.append(''.join(word))  
                        dic.add(''.join(word))  
                dfs(s_list[1:])  
                word.pop()  
                s_list[0], s_list[i] = s_list[i], s_list[0]  
            return  
        if not s:  
            return s  
        dic = set()  
        word = []  
        result = []  
        dfs(list(s))  
        return result  
''''' 
优化1 
思路与第一种方法一值，先固定第一位数字，再固定第二位数字，... 
不对结果进行去重，而是直接对每一位固定的数字进行去重 用set()记录每一位上的数字 
'''  
class Solution2:  
    def permutation(self, s: str) -> List[str]:  
        def dfs(s_list):  
            dic = set()  
            for i in range(len(s_list)):  
                s_list[0],s_list[i] = s_list[i],s_list[0]  
                if s_list[0] not in dic:  
                    dic.add(s_list[0])  
                    word.append(s_list[0])  
                    if len(word) == len(s):  
                        result.append(''.join(word))  
                    dfs(s_list[1:])  
                    word.pop()  
                s_list[0], s_list[i] = s_list[i], s_list[0]  
            return  
        if not s:  
            return s  
        word = []  
        result = []  
        dfs(list(s))  
        return result  
''''' 
优化2 
不用set 实际也是检查当前位之前的数字是否有重复，有则跳过这一位数 
'''  
class Solution3:  
    def permutation(self, s: str) -> List[str]:  
        def dfs(s_list):  
            for i in range(len(s_list)):  
                if s_list[i] not in s_list[:i]:  
                    s_list[0],s_list[i] = s_list[i],s_list[0]  
                    word.append(s_list[0])  
                    if len(word) == len(s):  
                        result.append(''.join(word))  
                    dfs(s_list[1:])  
                    word.pop()  
                    s_list[0], s_list[i] = s_list[i], s_list[0]  
            return  
        if not s:  
            return s  
        word = []  
        result = []  
        dfs(list(s))  
        return result  