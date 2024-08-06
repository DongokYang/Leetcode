class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_list = list(word1)
        word2_list = list(word2)
        nl = []

        if len(word1_list)>=len(word2_list):
            for i in range(len(word1_list)):
                nl.append(word1_list[i])
                if len(word2_list)>i:
                    nl.append(word2_list[i])
        else:
            for i in range(len(word2_list)):
                if len(word1_list)>i:
                    nl.append(word1_list[i])  
                nl.append(word2_list[i])

        result = ''.join(nl)
        return result