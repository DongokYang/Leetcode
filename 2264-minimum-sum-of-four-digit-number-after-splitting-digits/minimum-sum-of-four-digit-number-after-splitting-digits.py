class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int, str(num)))
        num = sorted(num)
        return 10*(num[0]+num[1])+num[2]+num[3]
        