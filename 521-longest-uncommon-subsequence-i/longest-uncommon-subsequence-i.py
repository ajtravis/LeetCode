class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
#         l = -1
#         a_char = list(a)
#         c_char = list(b)
#         s1 = a
#         s2 = b
#         i = 0
#         while len(s1) > 0 and len(s1) > l:
            
#         print(a_char, a)
#         return l
        if a == b:
            return -1
        return max(len(a), len(b))