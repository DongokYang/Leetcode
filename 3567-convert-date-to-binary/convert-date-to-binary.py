class Solution:
    def convertDateToBinary(self, date: str) -> str:


        year, month, day = map(int,date.split('-'))


        year= bin(year)[2:]
        month= bin(month)[2:]
        day= bin(day)[2:]
    
        return year+'-'+month+'-'+day