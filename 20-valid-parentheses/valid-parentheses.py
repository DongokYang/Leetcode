class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        flag = 1
        temp = []

        for i in s:
            if len(temp) ==0:
                temp.append(i)
            else:
                if temp[-1] =='(':
                    if i ==')':
                        temp.pop()
                    elif i=='}' or i==']':
                        flag = 0
                        break
                    else:
                        temp.append(i) 
                elif temp[-1] =='{':
                    if i =='}':
                        temp.pop()
                    elif i==')' or i==']':
                        flag = 0
                        break
                    else:
                        temp.append(i)
                elif temp[-1] =='[':
                    if i ==']':
                        temp.pop()
                    elif i=='}' or i==')':
                        flag = 0
                        break
                    else:
                        temp.append(i)
        if len(temp) >=1:
            flag = 0
        return flag 