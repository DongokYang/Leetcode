class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ni = [0 for i in range(len(score))]
        nll = sorted(score)
        nll.sort(reverse = True)
        for i in range(len(score)):
            for ii in range(len(score)):
                if score[ii] == nll[i]:
                    ni[ii] = i
        nnnl = []

        for i in ni:
            if i ==0:
                nnnl.append("Gold Medal")
            elif i==1:
                nnnl.append("Silver Medal")
            elif i==2:
                nnnl.append("Bronze Medal")
            else:
                nnnl.append(str(i+1))
        return nnnl