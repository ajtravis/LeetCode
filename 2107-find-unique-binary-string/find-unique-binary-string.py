class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def inc(s: str, l: int) -> str:
            s = list(s)
            i = l-1
            while i >= 0:
                if s[i] == "1":
                    s[i] = "0"
                else:
                    s[i] = "1"
                    break
                i -= 1
            return ''.join(s)

        s = set(nums)
        ls = len(s)
        ans = "0" * ls

        while ans in s:
            ans = inc(ans, ls)

        return ans