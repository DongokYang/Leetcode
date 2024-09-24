class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        cnt = duration
        

        for i in range(1,len(timeSeries)):

            cnt += duration

            if timeSeries[i]  < timeSeries[i-1]+duration:
                cnt -= timeSeries[i-1]+duration - timeSeries[i]


        return cnt