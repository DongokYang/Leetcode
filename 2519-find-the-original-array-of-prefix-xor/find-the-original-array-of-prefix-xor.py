class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """

        outp = [pref[0]]

        for i in range(0,len(pref)-1):
            outp.append(pref[i]^pref[i+1])
        
        return outp