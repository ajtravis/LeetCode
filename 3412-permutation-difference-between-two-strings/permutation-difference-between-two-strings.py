class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dif = 0
        s1 = {v: i for i, v in enumerate(s)}
        t1 = {v: i for i, v in enumerate(t)}
        for x in s:
           dif += abs(s1[x] - t1[x])     
        return dif
    
#     