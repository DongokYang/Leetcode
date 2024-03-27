class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from collections import Counter

        x = Counter(sentence)
        x_keys = list(x.keys()) 
        x_values = list(x.values())

        if len(x_keys) == 26:
            return True
        else:
            return False