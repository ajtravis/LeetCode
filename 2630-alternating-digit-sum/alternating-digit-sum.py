class Solution:
    def alternateDigitSum(self, n: int) -> int:
        d=list(str(n))
        return sum([int(d[i]) if i%2==0 else -int(d[i]) for i in range(len(d))])