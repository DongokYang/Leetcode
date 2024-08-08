class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)   
        cnt = 0
        temp =0
        rst = []
        for i in range(len(s)):
            if s[i] =='(':
                cnt +=1
            else:
                cnt -=1
            if cnt ==0:
                print(temp,i)
                rst.append("".join(s[temp+1:i]))
                temp = i+1
        rst = "".join(rst)
        return rst
