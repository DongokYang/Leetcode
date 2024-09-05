class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = [[],[]]

        for i in nums1:
            if i not in nums2:
                if i not in ans[0]:
                    ans[0].append(i)

        for ii in nums2:
            if ii not in nums1:
                if ii not in ans[1]:
                    ans[1].append(ii)              

        return ans