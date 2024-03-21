class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        nl = [] 
        al=[]
        for i in image:
            nl = i[::-1]
            tl = []
            for i in nl:
                if i==0:
                    tl.append(1)
                elif i==1:
                    tl.append(0)
            al.append(tl)
            
        return al