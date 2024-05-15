class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        d = defaultdict(int)
        ans = 0

        for a, b in dominoes:
            mi, ma = min(a, b), max(a, b)
            if (mi, ma) in d:
                ans += d[(mi, ma)]
            d[(mi, ma)] += 1
          
        return ans