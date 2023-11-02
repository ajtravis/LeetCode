class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            if s.isnumeric():
                if int(s) > max_val:
                    max_val = int(s)
            else:
                if len(s) > max_val:
                    max_val = len(s)
        return max_val