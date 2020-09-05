'''
字符串的划分 DFS 注意剪枝的操作
'''
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(num_str):
            if num_str:
                one = num_str[:1]
                dfs(num_str[1:])
                #例如'06'为不合法的切割
                if one != '0':
                    two = num_str[:2]
                    if int(two)<26:
                        #当字符串只剩最后一个字符时，切割一个字符与两个字符会得到相同的结果，防止重复计数
                        if num_str[2:]!=num_str[1:]:
                            dfs(num_str[2:])
                return
            self.count+=1
            return
        self.count = 0
        num_str = str(num)
        dfs(num_str)
        return self.count