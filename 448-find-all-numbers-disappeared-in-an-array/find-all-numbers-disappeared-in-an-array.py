class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        complist = [i for i in range(1,n+1)]
        nums = set(nums)
        complist = set(complist)
        return list(set.difference(complist, nums))