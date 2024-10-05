class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ns = set()
        k = 0

        for i in nums:
            if i not in ns:
                nums[k] = i
                ns.add(i)
                k+=1

        return k       