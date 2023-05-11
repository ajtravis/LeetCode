class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        wl = []
        for w in words:
            wl.append(w[::-1])
        return " ".join(wl)