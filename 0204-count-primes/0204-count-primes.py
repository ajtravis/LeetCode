
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        true = [True]*(n)
        true[0], true[1] = False, False
        i = 2
        while i*i < n:
            if true[i] == True:
                for x in range(i*i, n, i):
                    true[x] = False
            i += 1
        return true.count(True)