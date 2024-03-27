class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        item_counts = Counter(nums)
        items_list = list(item_counts.keys())
        counts_list = list(item_counts.values())
        maxnum = max(counts_list)
        al = []
        for i in range(maxnum):
            al.append([])
        for i in range(maxnum):
            for ii in range(len(counts_list)):
                if counts_list[ii] > i:
                    al[i].append(items_list[ii])
        return al
