class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        cnt = 0
        for i in operations:
            if i =='--X':
                cnt -=1
            elif i =='X--':
                cnt -=1
            else:
                cnt +=1
        return cnt
