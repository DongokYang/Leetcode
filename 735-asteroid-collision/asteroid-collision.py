class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            ans.append(i)
            if i<0:
                while len(ans) >1:
                    if ans[-1] * ans[-2] >0:
                        break

                    if ans[-2] + i >0:
                        ans.pop()
                        break
                    elif ans[-2] +i ==0:
                        ans.pop()
                        ans.pop()
                        break
                    elif ans[-2] +i <0:
                        ans.pop()
                        ans.pop()
                        ans.append(i)

        return ans        