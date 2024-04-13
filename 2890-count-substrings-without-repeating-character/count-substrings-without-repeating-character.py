class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        r = 0
        res = 0
        for i in range(len(s)):
            r = max(r, d[s[i]])
            res += i-r+1
            d[s[i]] = i+1
        return res 