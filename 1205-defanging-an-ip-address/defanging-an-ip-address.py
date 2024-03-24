class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = list(address)
        nad = []
        for i in address:
            if i =='.':
                i = '[.]'
            nad.append(i)
        
        nadlist = "".join(nad)
        return nadlist 
                