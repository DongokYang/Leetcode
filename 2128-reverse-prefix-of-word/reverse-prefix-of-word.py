class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                temp = word[:i+1]
                temp.reverse()
                word = temp+word[i+1:]
                return "".join(word)

        return "".join(word)