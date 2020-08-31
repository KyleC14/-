'''
投票法 把相同的数字视作同一张票 相同的数字可以抵消别的数字的票 因为众数的数量大于一半，因此最后剩下的票数一定是众数的
'''
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for i in nums:
            if votes == 0:
                target = i
                votes +=1
            else:
                votes = votes+1 if target==i else votes-1
        return target