'''
运用字典提高检索效率 第一次遇到字符在字典中标注True 之后标注False
找到字符串中第一个在字典中为True的字符
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        re = ' '
        for i in s:
            if i in dic:
                dic[i] = False
            else:
                dic[i] = True
        for i in s:
            if dic[i]:
                re = i
                break
        return re
'''
有序哈希表
在哈希表的基础上，有序哈希表中的键值对是 按照插入顺序排序 的。基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 11 的字符”。
哈希表是 去重 的，即哈希表中键值对数量 \leq≤ 字符串 s 的长度。因此，相比于方法一，方法二减少了第二轮遍历的循环次数。当字符串很长（重复字符很多）时，方法二则效率更高。
Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
'''
class Solution2:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] = False
            else:
                dic[i] = True
        #不需要遍历字符串，只需要遍历字典就可以了，因为字符串可能会有重复字符，当字符串很长时间，遍历字典更有效率
        for k,i in dic.items():
            if i:
                return k
        return ' '