class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0

        brknlst = list(brokenLetters)
        txtlst = list(text.split())

        for i in txtlst:
            flag = 0
            for ii in brknlst:
                if ii in i:
                    flag = 1
            if flag:
                cnt +=1

        return (len(txtlst) -cnt)

