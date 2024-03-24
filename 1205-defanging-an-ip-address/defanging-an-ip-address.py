class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = list(address)
        address = list(map(lambda x: x.replace('.','[.]'),address))
        address = "".join(address)
        return address 
                