import math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        dif = high-low 
        count = math.floor(dif/2)
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        # if high % 2 == 1:
        #     count += 1
        return count