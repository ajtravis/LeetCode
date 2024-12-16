class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # sliding window approach
        l = 0
        r = 1
        res = 0
        map = {}
        map[s[l]] = 1

        while r < len(s):
            if s[r] not in map:
                map[s[r]] = 1
            else:
                map[s[r]] += 1
                while map[s[r]] > 2:
                    map[s[l]] -= 1
                    l += 1
            res = max(res, r - l + 1)
            r += 1
        return res