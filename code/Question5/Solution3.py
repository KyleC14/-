'''
用空格拆分为列表，再用%20合并成字符串
'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        split_list = s.split(" ")
        return ("%20".join(split_list))