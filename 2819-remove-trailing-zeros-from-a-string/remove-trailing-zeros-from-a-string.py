class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        length = len(num) -1
        i = length
        while i >= 0:
            if num[i] != "0":
                return num[:(i+1)]
            else:
                i-=1