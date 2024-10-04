class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nl = []
        al = []
        for i in nums:
            if i not in nl:
                nl.append(i)
            else:
                al.append(i)

        return al